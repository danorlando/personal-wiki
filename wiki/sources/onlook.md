---
tags:
  - ai-coding-tools
  - design-tools
  - visual-editing
  - nextjs
  - react
  - open-source
updated: 2026-04-26
source: https://github.com/onlook-dev/onlook
---

# Onlook — Visual-First AI Code Editor

An open-source, AI-first visual editor for Next.js + TailwindCSS that collapses the gap between design and code: edits made in the visual Figma-like interface write directly to source code in real time, and vice versa. Positioned as an open-source alternative to Bolt.new, Lovable, V0, Webflow, and Figma Make.

## Key Design Decisions

**DOM instrumentation as the core architectural bet.** Onlook instruments the user's code to map every rendered DOM element back to its exact location in source. This bidirectional mapping is what makes live visual-to-code editing possible — when you click an element in the browser preview, the editor knows precisely which JSX line to modify. The tradeoff: only works with frameworks that render DOM elements declaratively (JSX/TSX/HTML). Currently scoped to Next.js + TailwindCSS; theoretically extensible to any declarative framework.

**Web container architecture instead of local file editing.** Rather than editing files on disk directly, Onlook loads the user's code into a web container (CodeSandbox SDK), serves it, and displays the output in an iFrame. The editor reads and indexes code from the container. This enables real-time preview in-browser, collaborative editing, and cloud hosting without requiring a local dev environment setup. The tradeoff: dependency on CodeSandbox SDK and Freestyle for hosting.

**Edits flow both ways: iFrame first, then code.** When an element is edited visually, Onlook first updates it in the iFrame (instant visual feedback), then propagates the change back to source code. This "optimistic UI" pattern for code editing keeps the experience feeling immediate, rather than the roundtrip of edit → rebuild → refresh that characterizes traditional code editors.

**AI chat has the same code access as the visual editor.** The AI doesn't operate on a separate abstraction — it has direct code access and uses the same tools as the visual editor to understand and modify the project. This means AI-generated changes and manual visual edits are both first-class citizens in the same codebase, not siloed outputs.

**Design-to-code import paths.** Onlook supports importing from Figma and GitHub repos as starting points, and exporting back to GitHub via PRs. This positions it at the full design → development → deployment workflow rather than just the editing step.

**Open-source with a commercial hosted offering.** The editor is Apache 2.0 licensed and self-hostable; there's also a hosted app at onlook.com. This follows the open-core pattern: contribute to the ecosystem while maintaining a commercial hosting product.

## Architecture

```
Code (in web container)
  → served + displayed in iFrame in editor
  → indexed and instrumented by editor
  → visual edits update iFrame, then source
  → AI chat edits source directly via code tools
```

Tech stack:
- **Front-end:** Next.js + TailwindCSS + tRPC
- **Database/auth:** Supabase + Drizzle ORM
- **AI:** Vercel AI SDK, OpenRouter, Morph Fast Apply, Relace
- **Sandbox:** CodeSandbox SDK; **Hosting:** Freestyle

## Notable Patterns

- **"Cursor for Designers"** framing — captures the positioning precisely: same category of AI-native editor, different primary user (designer/PM vs. developer)
- Right-click any element → jumps to exact source location — the core developer escape hatch that differentiates it from no-code tools
- Branching for design experiments — try a layout variant without committing to it, similar to git branches but for visual design states
- Onlook can use *itself* as a tool call for branch creation and iteration — the editor is recursively self-aware as an MCP-compatible tool
- Still under active development as of the clip date (April 2026); not yet stable for production use

## Concepts Touched

- [[AI-Coding-Tools]]
- [[Visual-Code-Editing]]
- [[Design-Engineering]]
- [[DOM-Instrumentation]]
- [[Web-Containers]]
- [[Agentic-AI]]
- [[No-Code-Low-Code]]
- [[React-Ecosystem]]

## Inbound Sources

- `/raw/Repos/onlook The Cursor for Designers.md`
