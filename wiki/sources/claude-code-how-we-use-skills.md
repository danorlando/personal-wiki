---
tags:
  - source
  - claude-code
  - skills
  - anthropic
updated: 2026-04-26
---

# Lessons from Building Claude Code: How We Use Skills

**Source:** [X/@trq212, 2026-03-17](https://x.com/trq212/status/2033949937936085378)
**Author:** [[Thariq Shihipar]] (@trq212) — Anthropic

## Summary

An insider account of how Anthropic uses [[Agent Skills]] in Claude Code, with hundreds of skills in active use internally. Covers the 9 recurring categories of useful skills, best practices for writing them, and patterns for distribution and measurement.

## Key Misconception Corrected

> "A common misconception is that skills are 'just markdown files.' The most interesting skills are not just text files — they're **folders** that can include scripts, assets, data, etc. that the agent can discover, explore, and manipulate."

## The 9 Skill Categories

| # | Category | Purpose | Example Skills |
|---|---|---|---|
| 1 | Library & API Reference | Correct usage of internal/external libs | `billing-lib`, `frontend-design` |
| 2 | Product Verification | Test/verify code with external tools | `signup-flow-driver`, `checkout-verifier` |
| 3 | Data Fetching & Analysis | Connect to data/monitoring stacks | `funnel-query`, `grafana`, `cohort-compare` |
| 4 | Business Process & Team Automation | Automate repetitive workflows | `standup-post`, `weekly-recap` |
| 5 | Code Scaffolding & Templates | Generate framework boilerplate | `new-migration`, `create-app` |
| 6 | Code Quality & Review | Enforce standards, adversarial review | `adversarial-review`, `code-style` |
| 7 | CI/CD & Deployment | Build, deploy, babysit PRs | `babysit-pr`, `deploy-<service>` |
| 8 | Runbooks | Symptom → investigation → structured report | `oncall-runner`, `log-correlator` |
| 9 | Infrastructure Operations | Routine maintenance with guardrails | `<resource>-orphans`, `cost-investigation` |

## Best Practices for Writing Skills

### Don't State the Obvious
Focus on information that pushes Claude out of its normal way of thinking. The `frontend-design` skill avoids generic patterns (Inter font, purple gradients) because Claude already knows general design — it needs opinionated corrections.

### Build a Gotchas Section
The highest-signal content. Populated from real failure points Claude hits with your specific skill. Update over time.

### Use the File System & Progressive Disclosure
Skills are folders. Use the filesystem as **context engineering**:
- Split long API docs into `references/api.md`
- Include output templates in `assets/`
- Include helper scripts Claude can compose

### Avoid Railroading Claude
Give Claude the information it needs but preserve flexibility to adapt to each situation. Too-specific instructions break reusability.

### Think Through Setup
For skills requiring config (e.g., which Slack channel to post to), store setup in `config.json` in the skill directory. If missing, Claude asks the user via `AskUserQuestion`.

### The Description Field Is for the Model
Claude scans skill descriptions at session start to decide "is there a skill for this request?" Write the description as a **trigger condition**, not a summary.

### Memory & Storing Data
Skills can maintain state in log files, JSON, or even SQLite within the skill folder. Use `${CLAUDE_PLUGIN_DATA}` for data that should survive skill upgrades.

### Store Scripts & Generate Code
Providing helper libraries/scripts lets Claude spend turns on composition (deciding *what* to do) rather than reconstruction. Claude generates scripts on the fly to compose your library functions.

### On-Demand Hooks
Skills can register hooks that activate for the session duration when the skill is invoked — not globally. Good for opinionated hooks you only want sometimes (e.g., `/careful` blocks `rm -rf`, `DROP TABLE`, force-push).

## Distribution

- **In-repo:** `./.claude/skills/` — simple, but every skill adds context overhead
- **Plugin marketplace:** installable on demand; teams curate what they install

Anthropic's internal marketplace is unmanaged centrally — skills earn their place organically via Slack traction, then a PR moves them to the marketplace.

## Measuring Skills

Use a `PreToolUse` hook to log skill invocations, then find skills that are popular or **undertriggering** relative to expectations. See [example gist](https://gist.github.com/ThariqS/24defad423d701746e23dc19aace4de5).

## Inbound sources
- [[sources/claude-code-how-we-use-skills]] ← this page
