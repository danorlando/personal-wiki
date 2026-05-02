---
title: "Spec-Driven Development"
created: 2026-04-26
updated: 2026-04-26
type: concept
tags:
  - concept
  - development-workflow
  - agentic-ai
  - claude-code
---

# Spec-Driven Development

A workflow discipline for agentic coding systems where a full specification is written, reviewed, and agreed upon *before* any code generation begins — enforcing a separation between the "what" and the "how" that prevents scope drift, silent requirement drops, and premature implementation.

## The Core Problem

Agents given a vague prompt will make implementation decisions implicitly, often in ways that don't match the user's intent. By the time the mismatch is visible, significant context has been consumed and partial code exists. Spec-driven development surfaces the "what" explicitly before any irreversible action is taken.

## Key Patterns

**Brainstorming before coding.** obra-superpowers enforces a brainstorming skill invocation before any response that leads to code. The brainstorming output becomes the spec — a living document that the agent refers back to throughout implementation. This creates an explicit checkpoint for user redirection ([[sources/obra-superpowers]]).

**Discuss phase captures taste.** GSD asks about preferences (layout, error handling, depth, style) and writes them to `CONTEXT.md` before any research or planning begins. The researcher reads this file — investigation is targeted at *your* vision, not generic best practices ([[sources/get-shit-done]]).

**PRD as a pipeline stage.** oh-my-claudecode's team pipeline enforces `plan → PRD → exec` as a fixed sequence. The Product Requirements Document stage cannot be skipped — it's a structural gate before any execution begins ([[sources/oh-my-claudecode]]).

**Quality gate taxonomy.** GSD defines four canonical gate types — pre-flight, revision, escalation, abort — wired into plan-checker and verifier agents. Schema drift detection and scope reduction detection prevent the planner from silently dropping requirements during wave execution ([[sources/get-shit-done]]).

**Two-stage subagent review.** obra-superpowers uses two sequential review subagents: first checks spec compliance (did we build what was agreed?), then checks code quality (did we build it well?). Separating these concerns prevents quality review from obscuring whether the spec was followed ([[sources/obra-superpowers]]).

## TDD Integration

obra-superpowers enforces true RED-GREEN-REFACTOR cycles: write a failing test, make it pass with minimal code, then refactor. The spec defines what to test; TDD enforces that tests exist before implementation. The combination means every deliverable has both a written spec and automated verification ([[sources/obra-superpowers]]).

## Relation to Other Concepts

- [[Context-Engineering]] — specs are one form of structured context that persists across subagent boundaries
- [[Multi-Agent-Orchestration]] — spec checking is a natural orchestration gate between plan and execution phases
- [[Claude-Code]] — obra-superpowers is available in the official Claude plugin marketplace

## Inbound Sources

- [[sources/get-shit-done]]
- [[sources/obra-superpowers]]
- [[sources/oh-my-claudecode]]
