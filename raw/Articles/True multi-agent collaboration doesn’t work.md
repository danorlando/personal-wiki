---
title: "True multi-agent collaboration doesn’t work"
source: "https://www.cio.com/article/4143420/true-multi-agent-collaboration-doesnt-work.html"
author:
  - "[[Grant Gross]]"
published: 2026-03-11
created: 2026-05-03
description: "Individual AI agents can be super reliable, but when grouped together they only appear to work well in concert, producing high failure rates. Chained orchestration may be the answer."
tags:
  - "article"
---
![AI misfires](https://www.cio.com/wp-content/uploads/2026/03/4143420-0-19550200-1773758898-ai-misfires-no-roi-shutterstock_2633982077.jpg?quality=50&strip=all)

AI misfires

Some AI advocates are selling a vision in which dozens of agents [work together](https://cloud.google.com/discover/what-is-a-multi-agent-system) to solve complex problems with little to no human intervention. So far, that scenario is a myth.

AI agents can be effective when working one-by-one on separate tasks, but when grouped together to complete complex assignments, they fail most of the time, according to a [new research study](https://zenodo.org/records/18809207).

Advocates envision a multi-agent future that will lead to huge efficiency gains and major cost savings, thanks to [autonomous agentic AI](https://www.cio.com/article/4003880/how-ai-agents-and-agentic-ai-differ-from-each-other.html?utm=hybrid_search) taking over many of the complex tasks human employees currently perform.

But most organizations deploying multiple agents for a single workflow actually separate them into individual agent silos assigned for specific tasks, handing off their work to an [orchestration layer](https://www.cio.com/article/4021176/ai-agent-orchestration-the-cios-crucial-next-step.html?utm=hybrid_search) before another agent takes over.

True [multi-agent collaboration](https://www.cio.com/article/4132144/from-automation-to-agentic-building-a-workable-autonomous-enterprise.html?utm=hybrid_search) doesn’t work because agents suffer from the same organizational problems humans do, says organizational systems researcher and author [Jeremy McEntire](https://cageandmirror.com/). Agents ignore instructions from other agents, redo work others have already done, fail to delegate, and get stuck in planning paralysis, he says.

“AI systems fail for the same structural reasons as human organizations, despite the removal of every human-specific causal factor,” he writes in his recent research paper. “No career incentives. No ego. No politics. No fatigue. No cultural norms. No status competition. The agents were language models executing prompts. The dysfunction emerged anyway.”

## Complexity fails

Perhaps not surprisingly, the more agents are added to the mix and the more complex the organizational structure of the agents is, the more often they fail to deliver on their assigned tasks, says [McEntire](https://www.linkedin.com/in/jandrewmcentire/?isSelfProfile=false), head of engineering at luxury vacation rental service Wander.

McEntire tested agent outputs based on four organizational structures. When using a single agent to produce the outcome, the agents succeeded in 28 out of 28 attempts. Multiple agents in a hierarchical organization, with one agent assigning tasks to others, failed to deliver the correct outcome 36% of the time.

A [stigmergic emergence](https://en.wikipedia.org/wiki/Stigmergy) approach, with agents working in a self-organized swarm, failed 68% of the time, and an 11-stage gated pipeline, or [org swarm](https://swarm.org/wiki/Swarm_main_page), never produced a good outcome. In fact, the gated pipeline consumed its entire budget for the project on five planning stages without producing a single line of implementation code.

While building an AI agent platform at a former job, [Diptamay Sanyal](https://www.linkedin.com/in/diptamay/) observed similar problems with agents working together. Single agents working on discrete, well-scoped tasks are reliable, but [multi-agent collaboration](https://www.ibm.com/think/topics/multi-agent-collaboration) often fails, says Sanyal, now principal engineer at cybersecurity vendor CrowdStrike.

“Failure rates climb fast as complexity increases, exactly as the study found,” he adds. “The coordination overhead, context passing, and error propagation between agents mirrors human organizational dysfunction at scale.”

However, agent chaining, which isn’t true collaboration, can work, he notes, mirroring observations from some other AI experts.

“Threat detection, alert enrichment, and automated containment work best as discrete, well-scoped modules chained via orchestration layers,” he says. “It looks like multi-agent cooperation from the outside but architecturally, it’s sequential specialization with deterministic handoffs and human checkpoints built in.”

Visions of dozens of agents autonomously collaborating without human intervention isn’t happening yet, he adds. “The real value of AI agents today is automating repetitive, well-defined tasks at scale — augmenting human analysts with rapid data processing and consistent outputs,” Sanyal says. “Not emergent collective intelligence.”

## Same ol’ problems

McEntire’s paper shows how common human communication problems transfer to multi-agent environments, says [Nik Kale](https://www.linkedin.com/in/nikkale/), principal engineer and platform architect working on multi-agent coordination and agentic system design at Cisco.

“Every handoff between systems is a place where meaning gets lost, context gets compressed, and assumptions get made,” he says. “Humans deal with this in organizations by walking over to someone’s desk and saying, ‘Wait, what did you actually mean by that?’ Agents don’t have hallway conversations.”

IT leaders deploying agents should focus on single agents focused on well-scoped tasks, which create “stunningly reliable” results, Kale adds.

“The marketing pitch of ‘dozens of agents working together autonomously’ is selling a fantasy that violates information theory,” he says. “You don’t let agents collaborate. You let agents deliver to a spec, and you let a thin orchestration layer assemble the results.”

Multi-agent systems should start with either a single, highly structured agent working on a specialized task, or multiple agents operating within strict boundaries, shared context models, and evaluation controls, adds [Shanea Leven](https://www.linkedin.com/in/shaneak/), CEO at AI-based app building vendor Empromptu.ai.

- Sponsored Content
	#### [Securing the AI stack: Why embedded security is becoming a CIO imperative](https://jadserve.postrelease.com/trk?ntv_at=3&ntv_ui=8929b2ab-67b1-43dc-939c-f0e28c4fda50&ntv_a=7lMKAP7l3ASlkSA&ntv_fl=1BiSq4jmoK3Yc0xaKEvngzqv0obRslJxmo_woOK4L9occ5Pl_lT_pFJHzM7eUR7_tRgpe3sgwSGJrI2AMYm676W32Ko1rI2URNouXN08Fr4pWaZlp8WZd-KQZ7YzHDmCpEutjch60akhhByFwyDJYbviq9CS2M-GEdXKtQ9N6A-N1zSbN1XzHfLWUFjRBgxKlYreDDNqdDbVHjkEnexX8YD_I26QwIy34IK2SdB2cSNWqo0LQ8K6uCOgiMcMvYOoXd75ozGxwFeruZAf5-rEybV3L8IKtmmziYeUwysiINKnxRC9KlS2M2xbV308J93CrivA3PURkRtkuJiHctmFNd_GIJgya7AZ0_BuBlN0i2tV7xXGzG4GdJY4EtHR7VanjGZx05BC9yQL5-miDxp4wQ==&ord=238914458&ntv_ht=B7L3aQA&prx_referrer=https%3A%2F%2Fwww.perplexity.ai%2F&ntv_rad=16&ntv_r=https://www.cio.com/article/4142378/securing-the-ai-stack-why-embedded-security-is-becoming-a-cio-imperative.html?utm_source=nativo&utm_campaign=cisco2010019&utm_medium=sponsoredpost&utm_content=native)
	By Cisco
	20 Mar, 2026

“The idea that dozens of agents can spontaneously collaborate without supervision or boundaries is as crazy as humans doing it,” she says. “The value of AI agents is real, but it’s not in autonomous swarm behavior. It’s in controlled specialization.”

## Orchestrating results

Some AI users report success with chaining agents together using an orchestration tool in between them.

Workforce orchestration vendor Asymbl has deployed more than 150 agents, but their interactions with one another are highly controlled, says [Shivanath Devinarayanan](https://www.linkedin.com/in/shivanathd/), chief digital labor and technology officer at the company.

“Our 150-plus digital workers interact, hand off work, and collectively deliver outcomes we’ve designed around them, and they are coordinating with each other and their human teammates because we built an orchestration layer around them,” he says. “Before two AI agents interact, we have mapped the handoff — what data passes between them, in what format, under what conditions, what triggers a human review and why.”

An orchestration model controlling agents and defining each agent’s role before deployment are key pieces of the puzzle, he adds.

“We have AI agents specifically for discrete tasks and agents with shared memory and shared task lists to keep track of what the other agents are doing,” Devinarayanan says. “The key in both cases: clarity of role before deployment. What is this digital worker responsible for, where does the work come from, where does it go, and when does a human need to make a call?”

McEntire’s study confirms what Asymbl has seen, that the failure of multi-agent systems is an organizational and orchestration problem, not a technological one, he adds.

“The study found that agents suffer from the same coordination failures humans do when working together,” Devinarayanan says. “Agents are modeled on human reasoning. They inherit human organizational failure modes when the organizational design is weak.”

Vendors or AI advocates championing dozens of agents working together without human intervention are pushing the wrong vision, he adds.

“The right mental model is a hybrid workforce: digital workers with clear roles, human workers with oversight and judgment, and an orchestration layer connecting both,” Devinarayanan says.

- Sponsored Content
	#### [A new infrastructure playbook](https://jadserve.postrelease.com/trk?ntv_at=3&ntv_ui=d65d470c-8ad6-4428-8beb-2519f249bc2c&ntv_a=6lYKA_Oh3ASlkSA&ntv_fl=1BiSq4jmoK3Yc0xaKEvngzqv0obRslJxmo_woOK4L9occ5Pl_lT_pFJHzM7eUR7_tRgpe3sgwSGJrI2AMYm67yXHGIljnPM01_B8yRt7Xsq_9seEZYe_AZGrb7P2ZNMU9JU3v2qB5v94qvQpfn47EZyjiXkUn7bYc3Oqe3mU50w2k0uQyhGQlLdeH6BCTiC6pXFuIZ0G6O1xOhhdMh-3jtVEHBCNCOyMdtSckoaZyExtRH1FR-MMQLS5fiZgjeZBSam5AInOBh8qndWeScpgsI52WskK8fe66X3SXN1Qe_HBLS8pDVuC6-ab8AQia4jkJa4PzNscPnr57Zi2cNqLPCq3IPw9dV5Nc4ak3biW3IkD9A8LfAHUBrJV9gy3bGXG&ord=-2080850488&ntv_ht=B7L3aQA&prx_referrer=https%3A%2F%2Fwww.perplexity.ai%2F&ntv_rad=16&ntv_r=https://www.cio.com/article/4142378/securing-the-ai-stack-why-embedded-security-is-becoming-a-cio-imperative.html?utm_source=nativo&utm_campaign=cisco2010019&utm_medium=sponsoredpost&utm_content=native)
	By Cisco
	31 Mar, 2026