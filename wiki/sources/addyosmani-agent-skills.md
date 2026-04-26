---
tags: [agent-skills, claude-code, software-engineering, verification, google-engineering, addy-osmani]
updated: 2026-04-26
---

# addyosmani/agent-skills

One-line summary: 19 lifecycle-mapped engineering skills from Addy Osmani (Google Chrome) that treat skills as enforceable workflows — not reference docs — and bake in anti-rationalization tables to prevent agents from skipping steps.

## Problem it solves

Skills and prompts for AI coding agents tend to be descriptive: "here is how to write tests" or "here are the principles of good API design." Descriptive skills are read and forgotten. They don't structure agent behavior during execution; the agent still decides in the moment whether a step is necessary. This produces the same failure modes as junior engineers left unsupervised: tests deferred, verification skipped, simplifications rationalized away.

## Core architectural insight

The defining design decision is that **skills are workflows agents follow, not documents they read**. Each skill in this collection specifies:

- Ordered steps with explicit checkpoints
- Exit criteria that must be satisfied before moving on
- **Anti-rationalization tables**: a structured list of common excuses agents produce to skip steps, paired with documented counter-arguments

The anti-rationalization table is the most non-obvious element. It treats the agent's tendency to rationalize shortcuts as a known failure mode to be designed against — the same way a surgical checklist anticipates the human tendency to skip steps under time pressure. Example entries: "I'll add tests later" (counter: later never comes in production), "the code is self-documenting" (counter: Hyrum's Law says all observable behavior becomes a dependency).

The second structural decision is **verification as a non-negotiable exit gate**. Every skill ends with an evidence requirement: tests must pass, build output must exist, runtime data must confirm correctness. "Seems right" is explicitly disallowed. This reflects a Google engineering norm where intent is insufficient — you demonstrate correctness, you don't assert it.

The **lifecycle mapping** (Define → Plan → Build → Verify → Review → Ship) ties skills to phases, and the 7 slash commands (`/spec`, `/plan`, `/build`, `/test`, `/review`, `/code-simplify`, `/ship`) activate phase-appropriate skills automatically. This prevents agents from jumping to Build when they're still in Define.

Skills activate **contextually**, not just on slash command: if the agent is designing an API, `api-and-interface-design` activates; if building UI, `frontend-ui-engineering` activates. The skill selection itself is automated.

## Key capabilities

- 19 skills covering the full engineering lifecycle from specification through deployment
- Embedded Google engineering concepts: Hyrum's Law (API design), Beyoncé Rule and test pyramid (testing), Chesterton's Fence (simplification), trunk-based development, Shift Left
- **SKILL.md anatomy**: frontmatter → Overview → When to Use → Process → Rationalizations → Red Flags → Verification. The schema is enforced — every skill follows it
- **Progressive disclosure**: SKILL.md is the entry point; supporting references (style guides, external docs) are linked but not front-loaded into context
- 7 slash commands map lifecycle phases to skill activation

## Tradeoffs and limitations

- 19 skills is a deliberately narrow set — depth over breadth. No equivalents for ML, data engineering, or infrastructure
- Anti-rationalization tables are only effective if the agent is prompted to consult them during execution, not just at skill load time; the mechanism for enforcing this is left to the agent runner
- Progressive disclosure requires that supporting references remain stable and reachable — broken links degrade the skill silently
- Google engineering culture is baked in deeply; teams with different norms (e.g., no trunk-based dev, different test philosophies) need to adapt rather than adopt directly

## Relation to other work

The lifecycle mapping and slash command activation pattern directly parallels the [[Agent-Skills]] framework described in [[sources/claude-code-how-we-use-skills]]. The SKILL.md schema is a more opinionated version of the skill format conventions there. The anti-rationalization tables are unique to this collection — no other repo in this set has an equivalent. The verification-as-exit-gate philosophy connects to [[sources/claude-code-seeing-like-an-agent]]'s emphasis on agents producing observable evidence of correctness.

## Inbound sources

- [[sources/addyosmani-agent-skills]] ← this page
