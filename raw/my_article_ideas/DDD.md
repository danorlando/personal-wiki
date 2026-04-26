## The core claim

Even with AI coding assistants, Domain-Driven Design still has to be the foundation of your application. AI changes the _speed_ and _altitude_ of abstraction, not the _need_ for a well-modeled domain.

## Breaking it down

1. "DDD will not change much — we are just able to abstract faster and maybe another level up"

AI tools let engineers write more abstraction code, more quickly, and at higher levels of indirection than before. You can scaffold generic "framework-ish" layers (plugin registries, dispatchers, context providers, config-driven pipelines) in hours instead of weeks. That part of engineering has gotten cheaper.

2. "…but an application that has DDD at its core is vastly going to outperform a generic abstraction with context injection"

There's a tempting new pattern: build a very generic engine, then "inject context" (prompts, config, metadata, rules) to make it behave like your domain. In an AI-heavy codebase that's especially seductive — you can just dump domain knowledge into a system prompt or a YAML file and call it done.

His argument: an app whose _code_ actually models the domain — entities, aggregates, bounded contexts, ubiquitous language, invariants enforced in types — will beat that approach on almost every axis (correctness, evolvability, performance, debuggability). Generic engine + context injection looks elegant from a distance, but the domain rules live in prose and config, not in the structure of the code. You lose type safety, compile-time checks, discoverability, and the ability to reason locally.

3. "Basically the floor hasn't changed; the foundation still needs to be DDD"

The _minimum viable foundation_ for a serious application is unchanged. AI hasn't raised the floor — you still owe the system a proper domain model. AI just lets you build on top of that floor faster.

4. "OR the DDD gets added through abstractions, but those abstractions create a mess which is a foot-gun for legibility/scalability/reliability"

This is the failure mode he's warning about. If you _skip_ real domain modeling and instead try to approximate DDD by layering abstractions on top of a generic core — registries, strategy patterns, dynamic dispatch, "pluggable" everything — you end up with:

- Legibility: you can't read the code and understand what the business does. Behavior is assembled at runtime from config/context.
- Scalability (of the codebase, not just traffic): every new domain concept requires threading through N abstraction layers instead of adding one bounded context.
- Reliability: invariants that should be enforced by types are now enforced by hope (or by prompts). Bugs leak between "domains" that share the same generic plumbing.

"Foot-gun" = it looks productive in the short term and blows up later.

## Why he's probably saying this to _you_, on _this_ project

Look at what we're building: an orchestrator graph with model routing, skill loaders, structured output, cleaning nodes, a prompt registry, etc. That's exactly the kind of system where the seduction is real — "just make everything generic and inject context / prompts / skills." His point is:

- Our orchestrator should reflect the _medical answer-engine domain_ (threads, runs, queries, citations, evidence grading, safety checks — whatever the bounded contexts actually are) in its types and module boundaries.
- It should _not_ become a generic "LLM workflow engine" that happens to get medical behavior via prompt strings and a `skills/` folder.

The abstractions are fine (and necessary — model routing, LLM adapters, etc.), but they should sit _underneath_ a domain model, not _replace_ it.

## One-sentence summary

> AI lets us build abstractions faster, but abstractions aren't a substitute for modeling the domain — if you don't do DDD explicitly, you'll either underperform a DDD app or reinvent DDD badly through a tangle of generic layers.