#!/usr/bin/env python3
"""
Phase 1: Batch Wiki Ingest — Source Summarization
Reads raw source files, calls DeepSeek v4 Pro via OpenRouter to draft wiki summary pages.

Usage:
    python phase1_summarize.py [--dry-run] [--category Articles] [--limit 5]

Output:
    - Draft summary pages in wiki/sources/<slug>.md
    - Manifest JSON to stdout listing what was processed
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

# --- Config ---
WIKI_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = WIKI_ROOT / "raw"
WIKI_SOURCES_DIR = WIKI_ROOT / "wiki" / "sources"
SCHEMA_PATH = WIKI_ROOT / "SCHEMA.md"

# Model for summarization
MODEL = "deepseek/deepseek-v4-pro"  # DeepSeek V4 Pro on OpenRouter
OPENROUTER_BASE = "https://openrouter.ai/api/v1"

# Get API key from Hermes auth store or env
def get_api_key():
    key = os.environ.get("OPENROUTER_API_KEY", "")
    if key:
        return key
    auth_path = Path.home() / ".hermes" / "auth.json"
    if auth_path.exists():
        d = json.loads(auth_path.read_text())
        pool = d.get("credential_pool", {})
        for entry in pool.get("openrouter", []):
            token = entry.get("access_token", "")
            if token:
                return token
    return ""

API_KEY = get_api_key()

# --- Tag taxonomy from SCHEMA.md ---
TAG_TAXONOMY = [
    "model", "architecture", "benchmark", "training", "quantization",
    "person", "company", "lab", "open-source",
    "agent_system", "agent_enhancement", "memory", "skills", "orchestration", "governance",
    "developer-tools", "cli", "ide", "tool",
    "optimization", "fine-tuning", "inference", "alignment", "data", "context-engineering",
    "complexity-theory", "llmops", "trading",
    "comparison", "controversy", "prediction", "readme",
    "personal", "career",
]

# --- Slug generation ---
def make_slug(filename: str) -> str:
    """Convert filename to URL-safe slug."""
    name = filename.replace(".md", "").replace(".pdf", "")
    slug = re.sub(r'[^\w\s-]', '', name.lower().replace(' ', '-'))
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug

# --- Source discovery ---
def discover_sources(category: str = None) -> list[dict]:
    """Find all raw source files not yet ingested."""
    # Already ingested slugs
    existing_slugs = set()
    if WIKI_SOURCES_DIR.exists():
        for f in WIKI_SOURCES_DIR.iterdir():
            if f.suffix == '.md':
                existing_slugs.add(f.stem)

    # Scan raw directories
    categories = ["Articles", "Repos", "Releases", "research_papers", "Documentation", "learning", "my_article_ideas"]
    sources = []

    for cat in categories:
        if category and cat != category:
            continue
        cat_dir = RAW_DIR / cat
        if not cat_dir.exists():
            continue
        for f in cat_dir.rglob("*.md"):
            # Skip Personal
            if "/Personal/" in str(f):
                continue
            slug = make_slug(f.name)
            if slug in existing_slugs:
                continue
            sources.append({
                "path": str(f),
                "relative": str(f.relative_to(RAW_DIR)),
                "category": cat,
                "slug": slug,
                "filename": f.name,
            })

    return sources

# --- Frontmatter extraction ---
def extract_frontmatter(content: str) -> tuple[dict, str]:
    """Split YAML frontmatter from body. Returns (frontmatter_dict, body)."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                import yaml
                fm = yaml.safe_load(parts[1]) or {}
            except:
                fm = {}
            return fm, parts[2].strip()
    return {}, content

# --- SHA256 of body ---
def body_sha256(body: str) -> str:
    return hashlib.sha256(body.encode('utf-8')).hexdigest()

# --- LLM summarization prompt ---
SUMMARIZE_PROMPT = """You are summarizing a source document for a personal LLM wiki. Produce a structured wiki summary page following these conventions exactly.

## Output Format

```yaml
---
title: {title}
created: {today}
updated: {today}
type: source
tags: [2-5 tags from the taxonomy below]
sources: [raw/{relative_path}]
---
```

Then the body in markdown with these sections:

## Summary
2-3 sentence overview of what this source covers and why it matters.

## Key Points
- Bullet points of the most important takeaways (5-10 points)
- Focus on **design decisions**, novel insights, and non-obvious findings
- For research papers: emphasize methodology and results
- For articles/guides: emphasize actionable principles and frameworks

## Notable Claims
- Specific claims or predictions worth tracking (with context)

## Connections
Suggest 2-5 wiki pages this source would connect to, formatted as [[PascalCase]] wikilinks. These should be entities or concepts mentioned that deserve their own pages. Use PascalCase (e.g., [[AgentArchitecture]], [[MultiAgentOrchestration]], [[ContextEngineering]]). Prefer existing wiki topics: agent architecture, multi-agent orchestration, context engineering, agent memory, agent skills, agent governance, agent security, RAG, evaluation, harness design, tool use, alignment.

## Source Metadata
- Author: (if available)
- Published: (if available)  
- Type: {category}
- URL: (if available from source frontmatter)

## Tag Taxonomy (use only these tags)
{taxonomy}

## Source Content
```
{content}
```

Produce ONLY the wiki page content (frontmatter + markdown body). No explanations, no preamble."""

# --- Call LLM ---
def summarize_source(source: dict, dry_run: bool = False) -> str | None:
    """Send source to LLM and return the drafted wiki page."""
    content = Path(source["path"]).read_text(encoding='utf-8', errors='replace')
    fm, body = extract_frontmatter(content)

    # Truncate very long sources to ~30K chars to stay within token limits
    if len(body) > 30000:
        body = body[:28000] + "\n\n[... content truncated for summarization ...]"

    today = time.strftime("%Y-%m-%d")
    prompt = SUMMARIZE_PROMPT.format(
        title=fm.get('title', source["filename"].replace('.md', '')),
        today=today,
        relative_path=source["relative"],
        category=source["category"],
        taxonomy=", ".join(TAG_TAXONOMY),
        content=body,
    )

    if dry_run:
        print(f"  [DRY RUN] Would summarize: {source['relative']} ({len(body)} chars)", file=sys.stderr)
        return None

    try:
        from openai import OpenAI
        client = OpenAI(base_url=OPENROUTER_BASE, api_key=API_KEY)
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=4000,
        )
        result = response.choices[0].message.content
        # Strip markdown code fences if the model wrapped the output
        result = re.sub(r'^```(?:yaml|markdown|md)?\n?', '', result)
        result = re.sub(r'\n?```\s*$', '', result)
        # Strip any stray leading/trailing code fence lines
        lines = result.strip().split('\n')
        while lines and lines[0].strip().startswith('```'):
            lines.pop(0)
        while lines and lines[-1].strip().startswith('```'):
            lines.pop()
        result = '\n'.join(lines)
        return result.strip()
    except Exception as e:
        print(f"  [ERROR] LLM call failed for {source['relative']}: {e}", file=sys.stderr)
        return None

# --- Write draft ---
def write_draft(slug: str, content: str) -> Path:
    """Write the drafted wiki page."""
    WIKI_SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    path = WIKI_SOURCES_DIR / f"{slug}.md"
    path.write_text(content + "\n", encoding='utf-8')
    return path

# --- Main ---
def main():
    parser = argparse.ArgumentParser(description="Phase 1: Batch wiki source summarization")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be processed without calling LLM")
    parser.add_argument("--category", type=str, default=None, help="Only process this category (Articles, Repos, etc.)")
    parser.add_argument("--limit", type=int, default=None, help="Max sources to process")
    parser.add_argument("--model", type=str, default=None, help="Override model (e.g. deepseek/deepseek-chat-v3-0324)")
    args = parser.parse_args()

    global MODEL
    if args.model:
        MODEL = args.model

    if not API_KEY:
        print("ERROR: No OpenRouter API key found. Set OPENROUTER_API_KEY or configure ~/.hermes/auth.json", file=sys.stderr)
        sys.exit(1)

    sources = discover_sources(category=args.category)
    if args.limit:
        sources = sources[:args.limit]

    print(f"Found {len(sources)} sources to summarize (model: {MODEL})", file=sys.stderr)

    manifest = []
    for i, source in enumerate(sources):
        print(f"[{i+1}/{len(sources)}] {source['relative']}", file=sys.stderr)

        result = summarize_source(source, dry_run=args.dry_run)
        if result:
            path = write_draft(source["slug"], result)
            manifest.append({
                "slug": source["slug"],
                "relative": source["relative"],
                "category": source["category"],
                "output": str(path),
                "status": "drafted",
            })
            print(f"  → Drafted: {path}", file=sys.stderr)
        elif args.dry_run:
            manifest.append({
                "slug": source["slug"],
                "relative": source["relative"],
                "category": source["category"],
                "output": None,
                "status": "dry_run",
            })

        # Rate limit: small delay between API calls
        if not args.dry_run and i < len(sources) - 1:
            time.sleep(1)

    # Output manifest
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    main()
