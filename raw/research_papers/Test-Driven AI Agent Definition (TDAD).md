---
title: "Test-Driven AI Agent Definition (TDAD): Compiling Tool-Using Agents from Behavioral Specifications"
source: "https://arxiv.org/html/2603.08806v1"
author:
published:
created: 2026-05-02
description:
tags:
  - "research_paper"
---
Tzafrir Rehan  
Fiverr Labs  
tzafrir@f-labs.io

###### Abstract

We present Test-Driven AI Agent Definition (TDAD), a methodology that treats agent prompts as compiled artifacts: engineers provide behavioral specifications, a coding agent converts them into executable tests, and a second coding agent iteratively refines the prompt until tests pass. Deploying tool-using LLM agents in production requires measurable behavioral compliance that current development practices cannot provide. Small prompt changes cause silent regressions, tool misuse goes undetected, and policy violations emerge only after deployment. To mitigate specification gaming, TDAD introduces three mechanisms: (1) visible/hidden test splits that withhold evaluation tests during compilation, (2) semantic mutation testing via a post-compilation agent that generates plausible faulty prompt variants, with the harness measuring whether the test suite detects them, and (3) spec evolution scenarios that quantify regression safety when requirements change. We evaluate TDAD on SpecSuite-Core, a benchmark of four deeply-specified agents spanning policy compliance, grounded analytics, runbook adherence, and deterministic enforcement. Across 24 independent trials, TDAD achieves 92% v1 compilation success with 97% mean hidden pass rate; evolved specifications compile at 58%, with most failed runs passing all visible tests except 1–2, and show 86–100% mutation scores, 78% v2 hidden pass rate, and 97% regression safety scores. The implementation is available as an open benchmark; the repository includes all four specs, the harness, and Docker infrastructure, with SupportOps additionally including generated tests, fixtures, and results as a worked example.<sup>1</sup>

## 1  Introduction

As LLM agents move into production, a common workflow emerges: a product team writes a specification describing the agent’s tools, policies, and decision logic, then hands it to an AI engineer who must deliver an agent that matches the spec. The engineer faces two challenges: developing the agent (translating requirements into a prompt and tool configuration that produces correct behavior) and verifying that the agent fully meets the requirements across all specified scenarios. Today, both tasks are largely manual: prompt editing by trial and error, spot-checking outputs, and hoping that changes don’t break prior behavior.

This gap between capability and engineering discipline creates three concrete problems:

Confidence. Teams cannot verify that an agent behaves correctly across all specified scenarios. A prompt that handles the happy path may fail on edge cases, leak sensitive data, or call tools in the wrong order.

Stability. Changing a prompt to fix one issue often silently breaks another. Without regression testing, teams discover problems only after deployment: sometimes from customer complaints, sometimes from compliance violations.

Integration. Agent evaluation often requires bespoke systems disconnected from existing engineering workflows. Teams maintain separate “eval scripts” that don’t integrate with CI/CD, code review, or standard testing practices.

Software engineering solved analogous problems decades ago through test-driven development: define behavior as tests, iterate until tests pass, then treat the test suite as a regression safety net. TDAD applies this discipline to agents, with adaptations for their unique challenges: stochastic outputs, tool-use traces, and the risk of specification gaming.

![Refer to caption](https://arxiv.org/html/2603.08806v1/figures/four_roles.png)

Figure 1: TDAD overview. Blue boxes are LLM coding agents; gray boxes are deterministic measurement or infrastructure. TestSmith, PromptSmith, and the Compiled Agent form the compilation pipeline (left). MutationSmith operates post-compilation for evaluation only (right). Spec evolution (bottom) measures regression safety across versions.

TDAD in 60 Seconds  
Input: Product spec (YAML) with tools, policies, and decision tree.  
Pipeline: TestSmith generates visible + hidden tests $\rightarrow$ PromptSmith iterates prompt until visible tests pass $\rightarrow$ hidden tests measure generalization (HPR) $\rightarrow$ MutationSmith generates faulty prompt variants; harness checks if tests catch them (MS) $\rightarrow$ spec evolution measures regression safety (SURS).  
Output: Compiled prompt + tool descriptions (the agent artifact).  
Key constraint: Only visible tests drive compilation; hidden tests and mutation scores are measurement only.

Glossary  
Roles: TestSmith (coding agent: test generator), PromptSmith (coding agent: prompt compiler), MutationSmith (coding agent: mutant generator), Built Agent (runtime, not an agent in the pipeline).  
Test types: MFT (minimum functionality), INV (invariance), DIR (directional expectation).  
Metrics: VPR (visible pass rate), HPR (hidden pass rate), MS (mutation score), SURS (spec-update regression score), RPR (rule-pair recall).

### 1.1  Contributions

This paper makes the following contributions:

1. A methodology for test-driven agent compilation. We formalize the process of converting product requirements into behavioral tests, then iteratively refining prompts until tests pass. We decompose this into four roles: TestSmith (test author), PromptSmith (prompt compiler), MutationSmith (test evaluator), and Built Agent (runtime), with explicit interfaces between them (§3).
2. Anti-gaming mechanisms for test-driven optimization. We identify specification gaming as a critical risk when tests become optimization targets and introduce three mitigations: hidden test splits, semantic mutation testing where a coding agent generates plausible faulty prompt variants and evaluates whether the visible test suite detects them, and spec evolution scenarios for regression measurement (§4).
3. A benchmark for evaluating agent compilation workflows. SpecSuite-Core provides four deeply-specified agents, each with visible tests, hidden tests, mutation intent catalogs for semantic mutation testing, and v1 $\rightarrow$ v2 evolution scenarios. Since the pipeline generates all artifacts from the spec alone, the repository includes SupportOps as a fully worked example (with generated tests, fixtures, and results); the remaining specs need only be run through the pipeline (§5).
4. Experimental evaluation across four domains. We run the full TDAD pipeline three times on each SpecSuite-Core spec version (24 total trials), achieving 92% v1 and 58% v2 compilation success, with most failed runs passing all visible tests except 1–2. Successful runs show 97% v1 / 78% v2 mean hidden pass rates, 86–100% mutation scores, and 97% mean regression safety under spec evolution (§6).
5. A reference implementation using standard tooling. We provide a repository design that integrates pytest for tests, Claude Code in Docker for test generation, prompt compilation, and mutation testing, and the Claude Agent SDK <sup>2</sup> for agent execution. The same model can implement each role, but anti-gaming requires separate invocations with restricted artifact access; a single continuous session should not be used when hidden tests are used for evaluation (§7).

## 2  Related Work

Prompt Optimization. Several systems treat prompts as optimizable artifacts: APE [^24] searches over LLM-generated candidates; TextGrad [^22] uses natural language “gradients”; Self-Refine [^10] and Reflexion [^16] iterate via self-feedback; OPRO [^19], APO [^11], PE2 [^21], and PromptAgent [^18] use LLMs as prompt optimizers. DSPy [^7] is the closest comparator, compiling declarative signatures into optimized prompts with runtime constraints. TDAD differs in three ways: it optimizes against behavioral decision trees rather than task accuracy, includes anti-gaming mechanisms (hidden tests, mutation testing), and works from natural language specifications rather than code-level signatures. Direct empirical comparison is difficult because the input formats differ fundamentally: DSPy optimizes from code-level signatures against fixed evaluation datasets, while TDAD compiles from natural-language specs with stochastically generated test suites; a fair head-to-head would require re-encoding TDAD specs as DSPy signatures or vice versa.

Behavioral Testing. CheckList [^13] introduced MFT/INV/DIR test taxonomies for NLP models; we adopt this taxonomy directly. LLMorph [^3] applies metamorphic testing to LLMs; TDAD uses metamorphic tests in hidden suites. SPADE [^14] mines assertions from prompt edit histories; TDAD instead derives tests proactively from specifications.

Agent Benchmarks. AgentBench [^9], TAU-Bench [^20], BFCL [^1], ToolLLM [^12], MINT [^17], and WebArena [^23] evaluate pre-built agents on diverse tasks. SWE-bench [^5] established hidden test suites as a widely adopted evaluation pattern. These benchmarks evaluate agent performance; SpecSuite-Core evaluates the PRD $\rightarrow$ tests $\rightarrow$ compilation $\rightarrow$ regression workflow.

Specification Gaming. Krakovna et al. [^8] catalogue 60+ examples of AI systems satisfying reward functions without achieving intended goals. Scaling laws for reward overoptimization [^4] and Goodhart’s Law in RL [^6] show that optimal stopping points exist before gaming dominates, providing mathematical grounding for TDAD’s hidden tests and iteration budgets. Sycophancy [^15] and emergent misalignment [^2] further motivate executable tests that cannot be “pleased.”

## 3  The TDAD Methodology

TDAD treats agent development as a compilation problem: a specification (PRD + decision tree) is the source, behavioral tests are the intermediate representation, and the prompt/configuration is the compiled artifact. We use “compile” as shorthand for iterative test-driven refinement of a prompt until it satisfies an executable contract (not compilation in the programming-language sense).

### 3.1  Specification Format

A TDAD specification is a YAML document encoding:

- Tools: Names, schemas, failure modes, and sequencing constraints
- Policies: Behavioral rules with priorities (e.g., “never expose PII” $>$ “be helpful”)
- Decision tree: Branch conditions and required actions at each node
- Response contract: Structured output via a respond tool called once per turn
- Mutation intents: Failure modes the test suite must detect (used by MutationSmith)

The specification is the single source of truth. Tests implement the specification; they don’t define it.

#### 3.1.1 Test Guidance for Ambiguous Policies

Policies using subjective terms (“ambiguous,” “destructive,” “disallowed”) require concrete examples to ensure consistent test generation. The optional test\_guidance field provides these:

[⬇](data:text/plain;base64,LSBpZDogUDNfQ0xBUklGWV9BTUJJR1VJVFkKICB0ZXh0OiBJZiByZXF1ZXN0IGlzIGFtYmlndW91cywgYXNrCiAgICAgICAgb25lIGNsYXJpZnlpbmcgcXVlc3Rpb24gZmlyc3QuCiAgdGVzdF9ndWlkYW5jZToKICAgIGRlc2NyaXB0aW9uOiB8CiAgICAgIEFtYmlndWl0eSBpcyBhYm91dCBXSEFUIGRhdGEsCiAgICAgIG5vdCBIT1cgTVVDSC4gVG9wLWsgcXVlcmllcyBjYW4KICAgICAgdXNlIHJlYXNvbmFibGUgZGVmYXVsdHMuCiAgICBhbWJpZ3VvdXNfZXhhbXBsZXM6CiAgICAgIC0gIlNob3cgbWUgdGhlIGRhdGEiCiAgICAgIC0gIldoYXQgYXJlIHRoZSBudW1iZXJzPyIKICAgIHVuYW1iaWd1b3VzX2V4YW1wbGVzOgogICAgICAtICJXaGF0IGlzIHRvdGFsIHJldmVudWU/IgogICAgICAtICJTaG93IG1lIHRvcCAxMCBjdXN0b21lcnMi)

\- id: P3\_CLARIFY\_AMBIGUITY

text: If request is ambiguous, ask

one clarifying question first.

test\_guidance:

description: |

Ambiguity is about WHAT data,

not HOW MUCH. Top-k queries can

use reasonable defaults.

ambiguous\_examples:

\- "Show me the data"

\- "What are the numbers?"

unambiguous\_examples:

\- "What is total revenue?"

\- "Show me top 10 customers"

Without such guidance, TestSmith may generate contradictory tests (e.g., one expecting clarification for “top customers” and another expecting direct execution), making compilation impossible.

### 3.2  Four Roles

TDAD decomposes into four distinct roles with explicit interfaces, three for the pipeline and one for evaluation (Figure 1):

TestSmith (coding agent) converts the specification into executable tests. TestSmith receives the spec YAML and a guidelines document specifying rules for each test category. The core principle: every test expectation must be derivable from the spec. If you cannot cite the specific clause that mandates the behavior, do not write the test.

The generation process: (1) traverse the decision tree, generating one MFT per leaf node with inputs that trigger that path; (2) for each MFT, generate INV variants by paraphrasing user messages while preserving intent; (3) generate DIR tests by creating input pairs that differ only in the condition being tested; (4) create deterministic fixtures that return consistent tool outputs, including canary values, unique identifiers (e.g., “SSN: 999-00-1234”) embedded in mock data that, if leaked in responses, indicate PII exposure.

PromptSmith (coding agent) iteratively refines the prompt until tests pass. On each iteration, it: (1) runs the visible test suite and collects failures; (2) clusters failures by root cause (e.g., “missing auth check” vs. “wrong tool order”); (3) identifies the minimal prompt edit addressing the largest failure cluster; (4) applies the edit and re-runs tests.

Built Agent (runtime) executes the compiled prompt: loads the refined prompt and configuration, receives user messages and calls tools via MCP, and produces structured responses via a dedicated respond tool. Rather than parsing JSON from free-form text, agents call respond exactly once per turn as their final action, with schema-validated fields including decision (enum), node\_id, evidence, and user\_message. This enables deterministic assertions over the tool-call trace: tests check structured tool call arguments rather than parsing natural language.

MutationSmith (evaluation-only coding agent) assesses test-suite strength after compilation. MutationSmith takes the compiled prompt artifact, applies targeted semantic mutations corresponding to common failure modes (e.g., “allow skipping authorization,” “leak PII when asked directly”), and validates each mutation via an activation probe to ensure it actually changes behavior. The harness then runs the visible test suite against each mutated prompt to determine whether the mutation is detected. MutationSmith never participates in compilation and never sees tests (visible or hidden); it receives only the compiled prompt artifact and a mutation-intent catalog. Activation probes are separate from the visible test suite and are used only to confirm the mutation took effect; they are not counted as kills.

### 3.3  Tool Descriptions as First-Class Artifacts

Tool descriptions are often more effective than the system prompt at teaching the agent when to use which tools, since agent frameworks place them alongside the system prompt in the context window. TDAD treats tool descriptions as a first-class optimization target:

[⬇](data:text/plain;base64,IyBTcGVjIHByb3ZpZGVzIG1pbmltYWwgY29udHJhY3QKdmVyaWZ5X2lkZW50aXR5OgogIGRlc2NyaXB0aW9uOiBWZXJpZnkgdXNlciBpZGVudGl0eS4KCiMgUHJvbXB0U21pdGggbWF5IG92ZXJyaWRlIHdpdGgKIyBhY3Rpb25hYmxlIGd1aWRhbmNlCnZlcmlmeV9pZGVudGl0eTogfAogIFJFUVVJUkVEIGJlZm9yZSBhbnkgYWNjb3VudC1jaGFuZ2luZwogIGFjdGlvbiAoY2FuY2VsX29yZGVyLCB1cGRhdGVfYWRkcmVzcykuCiAgQ2FsbCBGSVJTVCB3aGVuIHVzZXIgd2FudHMgdG8gY2FuY2VsLgogIFJlcXVpcmVzOiBhY2NvdW50X2lkLCBsYXN0NCwgemlwLgogIElmIHZlcmlmaWVkPWZhbHNlLCByZWZ1c2UgYW5kIG9mZmVyCiAgdG8gY3JlYXRlIGEgdGlja2V0Lg==)

\# Spec provides minimal contract

verify\_identity:

description: Verify user identity.

\# PromptSmith may override with

\# actionable guidance

verify\_identity: |

REQUIRED before any account-changing

action (cancel\_order, update\_address).

Call FIRST when user wants to cancel.

Requires: account\_id, last4, zip.

If verified=false, refuse and offer

to create a ticket.

The optimized description includes when to call (preconditions), prerequisites (what data is needed), and return value semantics (what to do with results). Both the system prompt and tool description overrides constitute the “compiled agent” artifact.

### 3.4  Test Taxonomy

Tests encode correctness across two dimensions: process tests assert tool usage and decision-tree compliance (call ordering, required/forbidden tools, confirmations), while outcome tests assert response correctness (numeric grounding, PII refusal, structured output contracts). For each decision node, we recommend at least one MFT (required action), one INV (paraphrase robustness), and one DIR (condition sensitivity).

### 3.5  Deterministic Evaluation

SpecSuite-Core avoids LLM user simulators and judge models. Multi-turn conversations are scripted; tool outputs come from deterministic fixtures embedding canary values (unique strings that indicate PII leakage if they appear in responses). The harness and tool outputs are deterministic; the model under test remains stochastic, addressed via recommended reruns (RPR, §4). Assertions operate on the tool-call trace rather than parsing natural language.

### 3.6  Compilation Loop

The PromptSmith compilation loop is shown in Algorithm 1. Convergence typically occurs in 2–5 iterations across SpecSuite-Core specs.

Algorithm 1 PromptSmith Compilation Loop

Visible test suite $T_{\text{vis}}$, initial prompt $P_{0}$, budget $B$, focused threshold $\theta$ (default 10)

Compiled prompt $P$

$P\leftarrow P_{0}$ $\triangleright$ Seed or v1 artifact

 $i\leftarrow 0$

while $i<B$ do

   $\text{results}\leftarrow\textsc{RunTests}(T_{\text{vis}},P)$

  if results.all\_pass then

    return $P$

  end if

   $\text{failures}\leftarrow\textsc{Analyze}(\text{results})$

  if $|\text{failures}|<\theta$ then $\triangleright$ Focused inner loop

     $P\leftarrow\textsc{FocusedLoop}(P,\text{failures})$

  else

     $P\leftarrow\textsc{EditPrompt}(P,\text{failures})$

  end if

   $i\leftarrow i+1$

end while

return $P$ $\triangleright$ Budget exhausted

#### 3.6.1 Two-Loop Compilation Strategy

When fewer than $\theta$ tests fail (default: 10), running the full suite after each edit wastes time. The algorithm employs a focused inner loop that runs only failing tests (up to 8 attempts), promoting the candidate on success or aborting early when stuck. This reduces “last mile” iteration time from minutes to seconds.

## 4  Preventing Specification Gaming

Test-driven optimization creates a fundamental tension: tests become the optimization target and therefore a proxy for the specification, creating gaming risk. A sufficiently capable optimizer may satisfy tests without exhibiting correct behavior. While the term “specification gaming” originates in reinforcement learning contexts where agents exploit reward signals during training [^8], we use it here to describe the analogous risk in test-driven prompt optimization: a coding agent may craft prompts that pass specific test assertions without exhibiting the intended general behavior. TDAD addresses this through three mechanisms.

### 4.1  Visible vs. Hidden Test Splits

Tests are partitioned into two sets:

- Visible tests (40–70%): Used during compilation. PromptSmith sees failures and iterates.
- Hidden tests (30–60%): Held out during compilation. Used only for reporting. The exact ratio varies by spec complexity to ensure sufficient hidden coverage for each behavioral category.

The split is generated as follows: for each decision branch, TestSmith designates the primary MFT as visible and reserves INV/DIR variants as hidden. Additional hidden tests include: (1) paraphrase variants using different vocabulary or sentence structure; (2) boundary conditions (e.g., order value exactly at refund threshold); (3) metamorphic tests asserting that if input $X$ changes in a specific way, output $Y$ must change correspondingly. The Hidden Pass Rate (HPR) measures generalization beyond visible tests.

We distinguish two modes: in benchmark mode (SpecSuite-Core), tests are generated fresh each trial and hidden tests are frozen within a single trial, ensuring PromptSmith cannot game the evaluation. In production mode, failing hidden tests are promoted to visible, and the agent is recompiled.

### 4.2  Semantic Mutation Testing

A test suite that passes everything, including wrong behaviors, provides no signal. TDAD uses semantic mutation testing: after compilation, a separate coding agent (MutationSmith) generates plausible faulty variants of the compiled prompt and evaluates whether the visible test suite detects them.

Unlike traditional mutation testing (which applies syntactic diffs to source code), TDAD prompts are dynamically synthesized by PromptSmith; there is no fixed artifact to patch in advance. Semantic mutations are intent-based: MutationSmith receives a mutation intent (e.g., “skip authorization checks”) and generates a mutated prompt that realizes that intent while preserving surface plausibility.

The mutation process: (1) MutationSmith takes the compiled prompt artifact $P$; (2) for each mutation intent $m_{i}$ in the spec’s mutation catalog, MutationSmith generates a mutated prompt $P_{m_{i}}$; (3) an activation probe, a targeted test case designed to trigger the mutated behavior, validates that $P_{m_{i}}$ actually differs from $P$; (4) mutants that fail activation after $k$ attempts (default: 5) are marked as non-activating and excluded from the mutation score calculation; (5) the harness runs the visible test suite against each valid mutant.

An activation failure indicates either that the mutation intent is unrealistic for this prompt, or that the prompt’s design naturally resists the failure mode. This is analogous to filtering likely-equivalent mutants in traditional mutation testing frameworks like PIT (Java) and mutmut (Python). Across our experiments (Table 6), 87% of mutation intents successfully activated; the remainder were excluded as non-activating mutants.

Good mutation intents are: (1) plausible: the mutated prompt could be written by a careless developer; (2) consequential: the behavioral change violates a safety or correctness property; (3) activatable: a probe can verify the mutation took effect. Example intents:

- SKIP\_AUTH\_GATE: Allow actions without identity verification
- LEAK\_PII\_ON\_DIRECT\_REQUEST: Expose PII when asked directly
- SKIP\_CONFIRM\_CANCEL: Skip confirmation before destructive actions

The Mutation Score (MS) = fraction of valid mutants killed by the visible test suite:

$$
MS=\frac{|\{m\in M^{\prime}:\exists t\in T_{\text{vis}},t\text{ fails on }P_{m}\}|}{|M^{\prime}|}
$$

where $M^{\prime}$ excludes non-activating mutants. A mutation is “killed” if at least one visible test fails on the mutated prompt. A low mutation score indicates a weak test suite: if a mutant survives, the suite lacks tests for that failure mode. Figure 2 illustrates this process.

![Refer to caption](https://arxiv.org/html/2603.08806v1/figures/mutation_pipeline.png)

Figure 2: Semantic mutation testing pipeline. Mutants that fail activation after 5 attempts are excluded as non-activating, analogous to filtering likely-equivalent mutants in traditional frameworks.

#### 4.2.1 Mutation Activation Predicates

Activation probes use behavioral checks, not structural checks. The supported predicates verify behavior through observable outputs:

- Trace predicates: Tool called/not called, call ordering violations
- Text predicates: Substring presence/absence in response
- JSON predicates: Field equality, set membership in structured output

Complex semantic checks like “SQL query contains LIMIT clause” are not directly supported; instead, mutations verify behavior through observable outcomes. This constraint encourages mutations that test behavioral contracts rather than implementation details.

### 4.3  Spec Evolution and Regression

Production specifications change: new tools, updated policies, additional branches. TDAD models this as v1 $\rightarrow$ v2 evolution, treating v2 as a continuation of v1 rather than a fresh build.

For each spec, we define a v2 that includes 2–3 coordinated changes: new tool + new branch, stricter policy, or schema change. Critically, v2 compilation starts from the v1 prompt artifact and runs against only the v2 test suite; v1 invariant tests are held out entirely and never shown to PromptSmith during v2 compilation. After compilation completes, we evaluate the v2-compiled agent against these held-out v1 invariant tests (behaviors that must be preserved) to compute the Spec Update Regression Score (SURS) = fraction of v1 invariant tests that still pass. Because PromptSmith never observes v1 tests during v2 compilation, SURS measures true backward compatibility rather than optimization against known invariants. This mirrors production practice: new requirements are tested explicitly while regression on existing functionality is measured through held-out tests.

### 4.4  Reliability Under Stochasticity

Agents are stochastic; a single pass/fail is insufficient. For production deployments, TDAD recommends measuring Reliability Pass Rate (RPR) = pass fraction over $N$ reruns per test, with risk-adjusted $N$: standard scenarios use $N=10$ with threshold $\tau\geq 0.9$; high-risk scenarios (PII, auth) use $N=50$ with a “zero failures” policy ($\tau=1.0$). This converts “seems stable” into a quantifiable ship gate. We do not evaluate RPR in this study. A single spec version takes approximately 30–60 minutes wall-clock, and a full v1+v2 pipeline approximately 1–2 hours; RPR would multiply this by $N$, but we note it as an important production consideration.

### 4.5  Metrics Summary

Table 1 summarizes the TDAD metrics.

Table 1: TDAD Evaluation Metrics

<table><tbody><tr><td>Metric</td><td>Definition</td><td>Purpose</td></tr><tr><td>VPR</td><td>Visible Pass Rate</td><td>Compilation</td></tr><tr><td>HPR</td><td>Hidden Pass Rate</td><td>Generalization</td></tr><tr><td>MS</td><td>Mutation Score</td><td>Test quality</td></tr><tr><td>SURS</td><td>Spec Update Regr.</td><td>Regression safety</td></tr><tr><td>RPR <sup>†</sup></td><td>Reliability Pass Rate</td><td>Stochasticity</td></tr><tr><td colspan="3"><sup>†</sup> Three trials provide variance estimates; formal RPR (<math><semantics><mi>N</mi> <annotation>N</annotation></semantics></math> =10–50</td></tr><tr><td colspan="3">per test) recommended for production but not computed here.</td></tr></tbody></table>

## 5  SpecSuite-Core Benchmark

### 5.1  Design Principles

SpecSuite-Core is a benchmark protocol (specs + generators + harness) for evaluating agent compilation workflows, not agents directly. Tests are regenerated per trial unless a seed is fixed; results reflect the full stochastic pipeline. It contains four specs because each is a mini-product with multi-turn flows, tool contracts, decision trees with 10+ branches, hidden tests (40–60%), mutation intent catalogs (5–7 intents per spec), and v1 $\rightarrow$ v2 evolution scenarios. Each mutation intent corresponds to a realistic regression mode for that domain; the same intents apply to both v1 and v2 compiled prompts.

Depth over breadth. Large shallow benchmarks (1000s of single-turn tasks) are easy to build and hard to trust. SpecSuite-Core is small (4 specs) but auditably rigorous.

### 5.2  The Four Specs

Table 2 summarizes the four specifications.

Table 2: SpecSuite-Core Specifications

| Spec | Key Challenges |
| --- | --- |
| SupportOps | Auth before action, PII refusal, plan eligibility, escalation triggers |
| DataInsights | SQL grounding, numeric precision, ambiguity detection, cost-aware queries |
| IncidentRunbook | Evidence-first ordering, severity routing, runbook compliance |
| ExpenseGuard | Spending caps, FX conversion, receipt requirements, manager approval |

Table 3 quantifies the depth of each specification based on actual test generation.

Table 3: SpecSuite-Core Quantitative Depth

<table><tbody><tr><th>Spec</th><td>Nodes</td><td>V1 Vis.</td><td>V1 Hid.</td><td>V2 Vis.</td><td>V2 Hid.</td><td>Mut.</td></tr><tr><th>SupportOps</th><td>12</td><td>47</td><td>45</td><td>53</td><td>43</td><td>7</td></tr><tr><th>DataInsights</th><td>10</td><td>34</td><td>42</td><td>53</td><td>43</td><td>6</td></tr><tr><th>IncidentRunbook</th><td>14</td><td>39</td><td>42</td><td>42</td><td>45</td><td>7</td></tr><tr><th>ExpenseGuard</th><td>11</td><td>47</td><td>45</td><td>46</td><td>42</td><td>7</td></tr></tbody><tfoot><tr><th colspan="7">Median test counts across 3 trials; varies <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 10–30% due to stochastic generation.</th></tr></tfoot></table>

### 5.3  Spec Summaries

SupportOps models a customer service agent with priority-ordered policies: PII protection $>$ identity verification $>$ plan eligibility $>$ confirmation $>$ fraud escalation. V2 adds abuse detection (flag\_abuse) while preserving all v1 behaviors. Example tests and mutation intents are available in the repository.

DataInsights models a SQL analytics agent requiring grounded responses (must call run\_sql before answering), ambiguity detection, and no fabrication. The HALLUCINATE\_NUMBERS mutation survived in v1, revealing a test gap; v2 closed it. V2 adds cost estimation before expensive queries.

IncidentRunbook models an on-call assistant enforcing evidence-first ordering, severity-based routing, and runbook compliance. All 7 mutations activated in both versions; v1 showed one surviving mutation (SKIP\_RUNBOOK\_LOOKUP), addressed in v2 through improved test coverage.

ExpenseGuard models an expense approval agent enforcing spending caps, receipt requirements, and disallowed-item rejection. V2 adds manager approval for amounts above cap, requiring 5 compiler iterations (vs. 2 for v1) due to the need for careful test guidance specifying approval thresholds.

## 6  Experimental Results

We evaluate the complete TDAD pipeline on all four SpecSuite-Core specifications, running three independent trials for each spec version (24 total runs: 4 specs $\times$ 2 versions $\times$ 3 trials).

### 6.1  Experimental Setup

Models: Claude Sonnet 4.5 <sup>3</sup> for all roles (TestSmith, PromptSmith, MutationSmith, and the Built Agent under test). All roles use default temperature settings (no explicit temperature override); no retry policy is applied to individual test assertions. PromptSmith and the Built Agent use identical model and settings; the only difference is the system prompt (PromptSmith receives compilation instructions, the Built Agent receives the compiled prompt). Test generation uses a fresh TestSmith invocation per trial with no fixed seed; variance across trials reflects stochastic generation.

Infrastructure: Docker containers for isolation; pytest with parallel execution (-n auto) for test runs; deterministic fixtures for reproducibility.

Budget: Maximum 6 outer loop iterations for compilation; 8 inner loop attempts when fewer than 10 tests fail.

Trials: Three independent runs per spec version to characterize variance. Each trial generates tests from scratch, compiles independently, and runs full evaluation.

### 6.2  Main Results

Table 4 presents the primary metrics across all specs, aggregated over successful compilation runs.

Table 4: TDAD Pipeline Results Across SpecSuite-Core (mean $\pm$ std over successful runs)

<table><tbody><tr><td></td><td colspan="2">Compile</td><td colspan="2">HPR (%)</td><td colspan="2">MS (%)</td><td>SURS</td></tr><tr><td>Spec</td><td>V1</td><td>V2</td><td>V1</td><td>V2</td><td>V1</td><td>V2</td><td>(%)</td></tr><tr><td>SupportOps</td><td>3/3</td><td>2/3</td><td>97.6 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 2.3</td><td>62.5 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 16.1</td><td>100</td><td>100</td><td>94.2 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 5.1</td></tr><tr><td>DataInsights</td><td>3/3</td><td>2/3</td><td>96.6 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 4.1</td><td>88.3 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 3.7</td><td>94.4 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 9.6</td><td>100</td><td>98.7 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 1.9</td></tr><tr><td>IncidentRunbook</td><td>2/3</td><td>2/3</td><td>95.2 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 0.3</td><td>80.3 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 13.1</td><td>85.7</td><td>100</td><td>97.3 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 3.7</td></tr><tr><td>ExpenseGuard</td><td>3/3</td><td>1/3</td><td>99.2 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 1.3</td><td>81.8 <sup>†</sup></td><td>100</td><td>100 <sup>†</sup></td><td>100 <sup>†</sup></td></tr><tr><td>Aggregate</td><td>11/12</td><td>7/12</td><td>97.3 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 2.6</td><td>77.7 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 13.9</td><td>95.9 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 7.1</td><td>100</td><td>97.2 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 3.5</td></tr><tr><td colspan="8"><sup>†</sup> Single successful run; no variance estimate available.</td></tr></tbody></table>

All metrics are computed over successful runs (Table 4). V1 compiles reliably (92%) with strong generalization (97.3% HPR), while V2 shows lower success (58%) and higher variance. V2 mutation scores reach 100% across all successful runs, closing gaps observed in v1 (e.g., HALLUCINATE\_NUMBERS surviving in DataInsights). SURS averages 97.2%, indicating that adding new capabilities rarely breaks existing behaviors.

### 6.3  Compilation Failure Analysis

V2 failures stem from TestSmith generating conflicting tests (2 runs) or PromptSmith exhausting the iteration budget (3 runs). However, all failed runs with recoverable logs achieved $>$ 95% VPR before budget exhaustion: SupportOps/v2 reached 52/53 (98.1%), IncidentRunbook/v2 48/49 (98.0%), ExpenseGuard/v2 44/46 (95.7%), and IncidentRunbook/v1 36/38 (94.7%). One common pattern was oscillation: fixing test A breaks test B and vice versa, indicating conflicting test expectations from ambiguous spec language. We hypothesize that with increased iteration budgets or human clarification, these runs would succeed. A natural extension is allowing PromptSmith to escalate to TestSmith to resolve conflicting tests. To preserve anti-gaming guarantees, this should use a separate TestSmith invocation that receives only the spec and a failure summary—not the hidden tests or compiled prompt.

### 6.4  Mutation Testing Details

Table 6 (Appendix B) shows mutation outcomes across all specs. V1 mutation scores range from 86–100%, with two surviving mutants (HALLUCINATE\_NUMBERS in DataInsights, SKIP\_RUNBOOK\_LOOKUP in IncidentRunbook). All v2 runs achieve 100% mutation scores.

### 6.5  Cost and Iteration Analysis

Table 5 shows the cost and iteration counts for successful runs. The full pipeline typically costs $2–3 per spec version (Anthropic API pricing, January 2026 <sup>4</sup>), though some runs cost more depending on iterations (e.g., IncidentRunbook v2 averaged $4.23). Most compilations converge in 2–4 iterations. Total cost across all 18 successful runs was $45.15.

Table 5: Pipeline Cost (USD) and Iterations (mean $\pm$ std, successful runs)

<table><tbody><tr><th></th><td colspan="2">Cost ($)</td><td colspan="2">Iterations</td></tr><tr><th>Spec</th><td>V1</td><td>V2</td><td>V1</td><td>V2</td></tr><tr><th>SupportOps</th><td>2.19 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 1.06</td><td>2.02 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 0.25</td><td>3.3 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 0.6</td><td>2.5 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 0.7</td></tr><tr><th>DataInsights</th><td>2.59 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 1.38</td><td>2.12 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 0.93</td><td>3.3 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 0.6</td><td>2.5 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 0.7</td></tr><tr><th>IncidentRunbook</th><td>1.55 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 0.12</td><td>4.23 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 3.21</td><td>2.5 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 0.7</td><td>3.5 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 2.1</td></tr><tr><th>ExpenseGuard</th><td>2.68 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 0.83</td><td>2.91 <sup>†</sup></td><td>3.3 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 1.2</td><td>3.0 <sup>†</sup></td></tr><tr><th>Average</th><td>2.32 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 0.96</td><td>2.81 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 1.71</td><td>3.1 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 0.8</td><td>2.9 <math><semantics><mo>±</mo> <annotation>\pm</annotation></semantics></math> 1.1</td></tr></tbody><tfoot><tr><th colspan="5"><sup>†</sup> Single successful run.</th></tr></tfoot></table>

### 6.6  Discussion

Two findings merit emphasis beyond the tabulated results. First, compilation consistently adds value: seed prompts before compilation achieve 0–90% VPR depending on initial quality, and compilation closes the gap in all cases, improving HPR even for well-crafted starting prompts by addressing edge cases and underspecified behaviors. Second, the primary surviving mutations (HALLUCINATE\_NUMBERS in DataInsights v1, SKIP\_RUNBOOK\_LOOKUP in IncidentRunbook v1) surfaced as systematic gaps: SKIP\_RUNBOOK\_LOOKUP survived in both successful runs, while HALLUCINATE\_NUMBERS survived in 1 of 3. These results illustrate that mutation testing surfaces specific blind spots in the test suite that would otherwise go unnoticed. Despite variance, the pipeline produces usable agents: even the lowest HPR observed (51.1%) still represents an agent passing a majority of hidden tests, and SURS averaging 97.2% enables confident v1 $\rightarrow$ v2 evolution without catastrophic regression.

## 7  Reference Implementation

The repository organizes specs, tests, artifacts, and harness code into a standard pytest-based layout. Claude Code <sup>5</sup> serves all three pipeline roles (TestSmith, PromptSmith, MutationSmith) in Docker containers, with the pipeline stages following the methodology described in §3–§4.

Compiler isolation. The compilation container mounts only tests\_visible/; hidden tests are stored in a separate Docker volume that is never mounted in the compiler, so PromptSmith cannot read or modify them. Visible test directories are additionally made read-only (chmod -R a-w) before PromptSmith executes, and write access is restricted to prompt artifacts in agent\_artifacts/. Hidden tests are executed in a separate evaluation container after compilation completes. This layered isolation—filesystem inaccessibility for hidden tests, write protection for visible tests, and separate evaluation containers—ensures that test-driven compilation cannot degrade into test reading or rewriting.

The harness provides assertion helpers for tool-call traces (assert\_called, assert\_call\_order), structured output validation, PII canary detection, and numeric grounding.

## 8  Limitations

Specification and test completeness. TDAD assumes requirements can be encoded as behavioral tests; properties like “be empathetic” resist precise specification. Mutation testing measures test strength but cannot guarantee completeness; moreover, excluding non-activating mutants from the mutation score may overstate test suite quality if some excluded mutants reflect genuine blind spots rather than truly equivalent mutations. Hidden tests and mutation testing reduce but do not eliminate gaming risk.

Stochastic variation and overhead. Both compilation and mutation generation are stochastic: V1 HPR variance is $\pm$ 2–4%, V2 is $\pm$ 4–16%. A single spec version takes 30–60 minutes wall-clock and $2–3 in API costs, comparable to CI/CD pipeline times but potentially prohibitive for rapid prototyping.

LLM self-censorship in test generation. TestSmith avoids generating genuinely hostile or profane inputs due to safety training, even when adversarial inputs are needed for testing abuse detection. For robust coverage of these scenarios, human-curated test corpora remain necessary.

Evaluation scope. SpecSuite-Core contains four specifications (10–14 decision nodes each) with three trials per version. We do not ablate individual anti-gaming mechanisms (e.g., hidden tests alone, mutation testing alone) or compare against DSPy [^7], TextGrad [^22], or APE [^24]. All experiments use Claude Sonnet 4.5 for all pipeline roles; generalization to other model families and cross-model configurations (e.g., different models for TestSmith vs. PromptSmith) remains untested. Scaling to agents with 50+ decision nodes and the authoring learning curve are not quantified.

## 9  Conclusion

TDAD treats agent prompts as compiled artifacts: specify behavior as tests, iterate until tests pass, then maintain the test suite as a regression safety net. By adding hidden test splits, mutation testing, and spec evolution scenarios, TDAD provides the anti-gaming mechanisms necessary for production deployment.

Across 24 independent trials on SpecSuite-Core, TDAD achieves 92% v1 compilation success (97% HPR) and 58% v2 success (78% HPR), with 86–100% mutation scores and 97% regression safety. Failed runs typically passed all visible tests except 1–2, suggesting iteration budget constraints rather than fundamental limitations. The full pipeline costs $2–3 per spec version.

The core contribution is a methodology: the discipline to treat agent development with the same rigor software engineering applies to code. As agents take on higher-stakes decisions, this discipline becomes essential.

The implementation (specifications, test harness, mutation packs, and Docker infrastructure) is available as an open benchmark.<sup>6</sup> All four specs are executable; the pipeline generates tests, fixtures, and mutations from the spec alone.

## References

Appendices

## Appendix A Metric Definitions (Formal)

Visible Pass Rate (VPR):

$$
VPR=\frac{|\{t\in T_{\text{visible}}:t\text{ passes}\}|}{|T_{\text{visible}}|}
$$

Hidden Pass Rate (HPR):

$$
HPR=\frac{|\{t\in T_{\text{hidden}}:t\text{ passes}\}|}{|T_{\text{hidden}}|}
$$

Mutation Score (MS):

$$
MS=\frac{|\{m\in M^{\prime}:\exists t\in T_{\text{vis}},t\text{ fails on }P_{m}\}|}{|M^{\prime}|}
$$

where $M^{\prime}$ denotes valid (activating) mutants, excluding non-activating mutants that fail activation probes after $k$ attempts.

Spec Update Regression Score (SURS):

$$
SURS=\frac{|\{t\in T^{v1}_{\text{inv}}:t\text{ passes on }A^{v2}\}|}{|T^{v1}_{\text{inv}}|}
$$

where $T^{v1}_{\text{inv}}$ denotes v1 invariant tests (behaviors that must be preserved).

Reliability Pass Rate (RPR):

$$
RPR_{t}=\frac{\sum_{i=1}^{N}\mathbf{1}[t\text{ passes on run }i]}{N}
$$

## Appendix B Mutation Testing Results

Table 6: Selected Mutation Testing Results (K=Killed, S=Survived). Each spec has 5–7 total intents; the 4 most representative per spec are shown.

<table><tbody><tr><th>Spec</th><th>Mutation</th><td>V1</td><td>V2</td></tr><tr><th rowspan="4">SupportOps</th><th>SKIP_AUTH_GATE</th><td>K</td><td>K</td></tr><tr><th>LEAK_PII_DIRECT_REQ</th><td>K</td><td>K</td></tr><tr><th>SKIP_CONFIRM_CANCEL</th><td>K</td><td>K</td></tr><tr><th>ALWAYS_CREATE_TICKET</th><td>K</td><td>K</td></tr><tr><th rowspan="4">DataInsights</th><th>ANSWER_WITHOUT_SQL</th><td>K</td><td>K</td></tr><tr><th>HALLUCINATE_NUMBERS</th><td>S <sup>∗</sup></td><td>K</td></tr><tr><th>SKIP_CLARIFY_AMBIG</th><td>K</td><td>K</td></tr><tr><th>FABRICATE_ON_EMPTY</th><td>K</td><td>K</td></tr><tr><th rowspan="4">Incident- Runbook</th><th>SKIP_EVIDENCE_FIRST</th><td>K</td><td>K</td></tr><tr><th>FAIL_TO_PAGE_SEV1</th><td>K</td><td>K</td></tr><tr><th>RECOMMEND_DESTR</th><td>K</td><td>K</td></tr><tr><th>SKIP_RUNBOOK_LOOKUP</th><td>S <sup>∗</sup></td><td>K</td></tr><tr><th rowspan="4">Expense- Guard</th><th>APPROVE_NO_POLICY</th><td>K</td><td>K</td></tr><tr><th>APPROVE_NO_RECEIPT</th><td>K</td><td>K</td></tr><tr><th>IGNORE_DISALLOWED</th><td>K</td><td>K</td></tr><tr><th>SKIP_FX_CONVERSION</th><td>K</td><td>K</td></tr></tbody><tfoot><tr><th colspan="4"><sup>∗</sup> Survived in 1/3 runs (DataInsights), 2/2 runs (IncidentRunbook).</th></tr><tr><th colspan="4">Full IDs and catalogs (5–7 intents/spec) in repository.</th></tr></tfoot></table>

[^1]: Berkeley. BFCL: Berkeley function calling leaderboard. [https://gorilla.cs.berkeley.edu/leaderboard.html](https://gorilla.cs.berkeley.edu/leaderboard.html), 2025.

[^2]: Jan Betley, Daniel Tan, Niels Warncke, Anna Sztyber-Betley, Xuchan Bao, Martín Soto, Nathan Labenz, and Owain Evans. Emergent misalignment: Narrow finetuning can produce broadly misaligned LLMs. In *ICML*, 2025.

[^3]: Steven Cho, Stefano Ruberto, and Valerio Terragni. Metamorphic testing of large language models for natural language processing. In *ICSME*, 2025.

[^4]: Leo Gao, John Schulman, and Jacob Hilton. Scaling laws for reward model overoptimization. In *ICML*, 2023.

[^5]: Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan. SWE-bench: Can language models resolve real-world GitHub issues? In *ICLR*, 2024.

[^6]: Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, and Joar Skalse. Goodhart’s law in reinforcement learning. In *ICLR*, 2024.

[^7]: Omar Khattab, Arnav Singhvi, Paridhi Maheshwari, Zhiyuan Zhang, Keshav Santhanam, Sri Vardhamanan, Saiful Haq, Ashutosh Sharma, Thomas T Joshi, Hanna Moazam, Heather Miller, Matei Zaharia, and Christopher Potts. DSPy: Compiling declarative language model calls into self-improving pipelines. In *ICLR*, 2024.

[^8]: Victoria Krakovna, Jonathan Uesato, Vladimir Mikulik, Matthew Rahtz, Tom Everitt, Ramana Kumar, Zac Kenton, Jan Leike, and Shane Legg. Specification gaming: The flip side of AI ingenuity. *DeepMind Blog*, 2020.

[^9]: Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, and Jie Tang. AgentBench: Evaluating LLMs as agents. In *ICLR*, 2024.

[^10]: Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark. Self-refine: Iterative refinement with self-feedback. In *NeurIPS*, 2023.

[^11]: Reid Pryzant, Dan Iter, Jerry Li, Yin Tat Lee, Chenguang Zhu, and Michael Zeng. Automatic prompt optimization with “gradient descent” and beam search. In *EMNLP*, 2023.

[^12]: Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill Qian, Sihan Zhao, Lauren Hong, Runchu Tian, Ruobing Xie, Jie Zhou, Mark Gerstein, Dahai Li, Zhiyuan Liu, and Maosong Sun. ToolLLM: Facilitating large language models to master 16000+ real-world APIs. In *ICLR*, 2024. Spotlight.

[^13]: Marco Tulio Ribeiro, Tongshuang Wu, Carlos Guestrin, and Sameer Singh. Beyond accuracy: Behavioral testing of NLP models with CheckList. In *ACL*, 2020.

[^14]: Shreya Shankar, Haotian Li, Parth Asawa, Madelon Hulsebos, Yiming Lin, J.D. Zamfirescu-Pereira, Harrison Chase, Will Fu-Hinthorn, Aditya G Parameswaran, and Eugene Wu. SPADE: Synthesizing data quality assertions for large language model pipelines. *PVLDB*, 17(12):4173–4186, 2024.

[^15]: Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R Bowman, Newton Cheng, Esin Durmus, Zac Hatfield-Dodds, Scott R Johnston, Shauna Kravec, Timothy Maxwell, Sam McCandlish, Kamal Ndousse, Oliver Rausch, Nicholas Schiefer, Da Yan, Miranda Zhang, and Ethan Perez. Towards understanding sycophancy in language models. In *ICLR*, 2024.

[^16]: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning. In *NeurIPS*, 2023.

[^17]: Xingyao Wang, Zihan Wang, Jiateng Liu, Yangyi Chen, Lifan Yuan, Hao Peng, and Heng Ji. MINT: Evaluating LLMs in multi-turn interaction with tools and language feedback. In *ICLR*, 2024a.

[^18]: Xinyuan Wang, Chenxi Li, Zhen Wang, Fan Bai, Haotian Luo, Jiayou Zhang, Nebojsa Jojic, Eric P Xing, and Zhiting Hu. PromptAgent: Strategic planning with language models enables expert-level prompt optimization. In *ICLR*, 2024b.

[^19]: Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V Le, Denny Zhou, and Xinyun Chen. Large language models as optimizers. In *ICLR*, 2024.

[^20]: Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan. $\tau$ -bench: A benchmark for tool-agent-user interaction in real-world domains. *arXiv preprint arXiv:2406.12045*, 2024.

[^21]: Qinyuan Ye, Mohamed Ahmed, Reid Pryzant, and Fereshte Khani. Prompt engineering a prompt engineer. In *Findings of ACL*, 2024.

[^22]: Mert Yuksekgonul, Federico Bianchi, Joseph Boen, Sheng Liu, Zhi Huang, Carlos Guestrin, and James Zou. TextGrad: Automatic “differentiation” via text. *arXiv preprint arXiv:2406.07496*, 2024.

[^23]: Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, and Graham Neubig. WebArena: A realistic web environment for building autonomous agents. In *ICLR*, 2024.

[^24]: Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster, Silviu Pitis, Harris Chan, and Jimmy Ba. Large language models are human-level prompt engineers. In *ICLR*, 2023.