---
title: "Beyond the hype: A real-world guide to building enterprise-grade AI agents"
source: "https://www.thoughtworks.com/en-us/insights/articles/a-real-world-guide-to-building-enterprise-grade-ai-agents"
author:
  - "[[Soumik Choudhury]]"
  - "[[Jaydeep Chakrabarty]]"
published: 2026-02-25
created: 2026-05-03
description: "Everyone talks about AI agents in finance, but how do you actually get them past risk and compliance? Here is the playbook with a real-world example."
tags:
  - "learning"
---
Disclaimer: AI-generated summaries may contain errors, omissions, or misinterpretations. For the full context please read the content below.

### The dawn of agentic AI in finance

The financial services industry has long been at the forefront of digital transformation, and now it stands at the forefront of the AI revolution. From risk management and fraud detection to wealth advisory and customer service, AI is driving new levels of automation, efficiency and insight.

However, beyond traditional machine learning models, a new frontier is emerging: agentic AI — autonomous agents capable of executing tasks, reasoning over goals and dynamically adapting to changing environments.

Agentic AI represents a shift from static models to systems that act, learn and make decisions independently within defined boundaries. In financial services, where real-time decision-making and regulatory compliance intersect, the potential of agentic AI is immense, but so are the complexities of scaling it.

In this blog, we explore the challenges of scaling agentic AI in the financial services space based on lessons learned from real-world experience.

### Understanding agentic AI: A new paradigm for financial services

Agentic AI marks a fundamental shift in how artificial intelligence operates within financial services. Unlike traditional systems that require explicit instructions, these next-generation agents interpret their environment and act autonomously with minimal human intervention. AI is no longer just a passive tool; it’s becoming an active participant in financial workflows.

This is made possible by advances in large language models (LLMs), reinforcement learning, retrieval-augmented generation (RAG) and multi-agent systems. Together, these technologies enable agents to operate independently, handle complexity and scale across dynamic environments.

At their core, agentic systems combine three key capabilities:

- **Autonomy:** Agents can act independently in real time. For example, in trading, an agent might analyze market shifts and execute trades without human intervention, adapting its strategy on the fly.
- **Adaptability:** These agents continuously learn from data, feedback loops and evolving market conditions. A portfolio agent, for instance, can fine-tune asset allocations as a client’s goals or risk appetite changes.
- **Orchestration:** Agentic AI can integrate with APIs, databases and even other agents, collaborating across systems. Imagine a compliance agent flagging suspicious activity and automatically coordinating with fraud detection tools in real time.

Think of agentic AI as a tireless team of analysts, traders and risk officers, working 24/7, learning continuously and coordinating seamlessly. It’s the technological embodiment of "Citi never sleeps."

By uniting autonomy, adaptability and orchestration, agentic AI doesn’t just automate tasks; it reimagines financial operations, enabling institutions to act smarter, faster and more intelligently in an ever-changing environment.

### The immense opportunities: How agentic AI is reshaping finance

Agentic AI isn’t a future promise; it’s already driving real outcomes across financial institutions. From operational efficiency to personalized service delivery, here’s how the industry is evolving:

#### 1\. Autonomous decision-making at scale

Agentic AI is helping firms achieve greater agility and precision, allowing them to react faster and smarter to market dynamics. At JPMorgan Chase, for instance, AI tools like Coach AI helped the firm navigate market volatility and boost asset and wealth management sales by 20% between 2023 and 2024 (Reuters). It’s autonomous optimization in action.

#### 2\. Specialized agents for complex financial tasks

Beyond general automation, agentic systems like FinRobot are now handling intricate functions like portfolio optimization and risk analysis, traditionally reserved for human experts (arxiv.org). These domain-specific agents are redefining what's possible in investment strategy and financial modeling.

#### 3\. Industry-wide adoption signals a strategic shift

It’s not just one or two players experimenting. Giants like Goldman Sachs, Morgan Stanley and Citibank are deploying AI agents for tasks like drafting IPO documentation and enhancing investment strategies (Business Insider). Even hedge funds are using agentic AI to automate high-value, repeatable tasks across the investment lifecycle.

#### 4\. Competitive advantage through early adoption

Firms that move early are seeing tangible benefits. Aviva Investors, for example, created a dedicated investment engineering team to build bespoke agentic tools, enhancing portfolio construction and offering more tailored client services (FN London). The result? A tech-enabled edge in both performance and personalization.

#### 5\. Financial inclusion and intelligent experiences

As the cost of delivering intelligent financial services drops, AI agents are opening up access. In emerging markets, agent-led loan underwriting and credit risk evaluation are already reaching customers who were historically excluded. Meanwhile, adaptive robo-advisors are evolving into 24/7 financial coaches, learning, adjusting and guiding users in real time.

### Scaling a RAG-based chatbot to an autonomous policy rule agent: A real world customer use case

Our journey began with a critical bottleneck in our client's mortgage policy rule engine. The manual process for creating new credit rules was slow and error-prone, sometimes taking hours for a single request. This wasn't just an inconvenience; it was a direct impact on customer response time. In many cases, it took anywhere from 30 minutes to hours, depending on the complexity.

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/infographic/tw_10680080917_scaling_agentic_ai_in_finance_web_1.jpg)

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/infographic/tw_10680080917_scaling_agentic_ai_in_finance_mobile_1.jpg)

Our first strategic response was PoliBot, a RAG-based AI assistant that streamlined the analysis phase and cut development cycles by over 60%. We created a helper file from the underlying source code and trained the LLM with real examples stored in Vector DB, which formed the foundation for the knowledge base/feature creation engine for the engineers and policy designers alike.

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/infographic/tw_10680080917_scaling_agentic_ai_in_finance_web_2.jpg)

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/infographic/tw_10680080917_scaling_agentic_ai_in_finance_mobile_2.jpg)

While a significant win, it was only the first step. True innovation demanded we address the entire value stream, which meant eliminating the "last mile" of manual execution. Developers still had to manually execute the answers of PoliBot provided which were coming in JSON format and deploy to the higher environments.

To illustrate this shift, we will look at how we closed that gap by evolving PoliBot from a system that simply delivered information to an autonomous teammate capable of taking action. We will explore the agentic architecture we built, the ReAct principle that serves as its brain, with actions served through the Model Context Protocol (MCP), and the critical lessons of explainability and interpretability as we built a system that is not only intelligent but also trustworthy and secure.

### Our blueprint for autonomy

To evolve PoliBot from an expert that answers into an agent that acts, we had to do more than just create feature code. We had to fundamentally change its digital DNA. Our goal was to give it the ability to reason, use tool and learn from its actions. In essence, we had to build it a brain.

While our original RAG-based bot was great at finding and creating query response, the new agentic PoliBot needed to act on that information independently. The key that unlocked this for us was ReAct, a simple but powerful principle that stands for Reason + Act. It allows a large language model (LLM) to think like a human and works in a continuous loop:

- **Reason:** First, the agent analyzes the request and its available knowledge to think about what it needs to do next. It forms an internal monologue, a "thought" about its strategy.
- **Act:** Based on that thought, it selects and uses a tool from its pre-approved toolbox to execute the step. It then observes the result of that action.

Let's bring this to life with PoliBot. A Policy manager gives the new agent a goal: "We need a new policy rule to flag any transaction over $10,000 from a high-risk country. Get it ready for review."

Here’s how the ReAct loop works inside PoliBot's "brain":

1. **Thought (Reason):** *“To implement this policy rule, I'll need to:*
	1. *Create a feature configuration that filters transactions based on amount (over $10,000)*
		2. *Create a feature configuration that filters transactions based on country (high-risk countries)*
		3. *Combine these filters to create the final policy rule”  
		*
2. **Action (Act):** PoliBot selects the CodeGenerator tool and feeds it the parameters (transaction > $10,000, source = high-risk country list).
3. **Observation:** The CodeGenerator tool returns a block of code.
4. **Thought (Reason):** *“The code has been generated. Now I must test it to ensure it functions correctly and doesn't break anything. I need to use the testing sandbox.”  
	  
	*
5. **Action (Act):** PoliBot selects the AutomatedTesting tool and runs the new code within a secure, isolated sandbox environment.
6. **Observation:** The tool returns a "Test Passed" result with performance logs.
7. **Thought (Reason):** *“The code is generated and passed all tests. The final step is to package the code, test results, and my reasoning log, then notify the compliance manager for final approval.”  
	  
	*
8. **Action (Act):** PoliBot uses the Notification tool to send a message to the manager with a link to the complete package, ready for a one-click review.

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/infographic/tw_10680080917_scaling_agentic_ai_in_finance_web_3.jpg)

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/infographic/tw_10680080917_scaling_agentic_ai_in_finance_mobile_3.jpg)

This cycle of reasoning and acting is the magic of an agent. It’s not following a script but dynamically thinking through the next steps, while staying within the context of the problem area. This was achieved through effective prompting and by setting boundaries for each agent so that it could work independently without deviating from its intended goal. After several iterations, the process began to work like a well-oiled machine.

Our initial proof-of-concept, which used custom code to connect the agent to each tool, proved the agent could work. However, this approach was not scalable, maintainable, or secure enough for an enterprise environment. To bridge this gap, we adopted the Model Context Protocol (MCP), an emerging open standard for AI launched by Anthropic.

To understand its impact, it's helpful to look at how it works. It functions as a standardized API contract, providing a crucial abstraction layer between the agent's ReAct-driven core and its heterogeneous set of tools (JIRA, GitHub, DB etc). Each tool is exposed as a "Managed Component" with a defined set of capabilities that declares its features. The agent interacts with these components by sending requests with a defined set of verbs (e.g., create, execute) to a central MCP gateway, which then proxies them to the underlying tool-specific APIs. This architecture simplifies agent development and centralizes critical enterprise concerns, such as authentication, authorization and the generation of an immutable, high-integrity audit log for all actions.

In our context, it would look like this:

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/infographic/tw_10680080917_scaling_agentic_ai_in_finance_web_4.jpg)

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/infographic/tw_10680080917_scaling_agentic_ai_in_finance_mobile_4.jpg)

This change of using MCP enabled us to plug new tools into our agent's ecosystem almost instantly, making PoliBot not just smart, but truly adaptable. It was a game-changing shift.

### Overcoming enterprise-scale challenges

Architecturing an agent is one thing; deploying it safely in a high-stakes enterprise environment presented several critical challenges we had to overcome.

A mistake in Policy Rule creation isn't a minor bug; it's a potential multi-million-dollar compliance failure. To bridge this trust gap, we had to prove our agent was not a "black box". Our solution combined transparent reasoning with verifiable actions, made possible by our MCP architecture:

- **Explainability (the "why"):** We engineered PoliBot to log its "thought process," showing each step of its ReAct loop and explaining why it chose a specific tool.
- **Verifiable auditing (the "what"):** Through our MCP gateway, we created an immutable, timestamped Audit Trail of every tool the agent actually used.
- **Human-in-the-loop:** This clear, combined audit trail was presented to a manager for final approval, giving them complete confidence to sign off on the agent's work.

While we were scaling, we discovered a core prompting paradox: as our agent became more autonomous, its "master prompt" — its core operating instructions — became surprisingly brittle. Minor changes often caused unexpected failures, putting us in a loop of manual fixes. Our solution was to treat these prompts like mission-critical code, implementing version control and automated regression testing to catch issues instantly. This taught us that prompt engineering for agents is a continuous engineering discipline, not a one-time task.

Our agent, while perfect in demos, initially struggled with the ambiguous and imperfect requests of real users. To solve this, we engineered an "intent clarification" step that enables the agent to ask follow-up questions when a goal is unclear. We backed this with a robust testing suite focused on these messy edge cases, and we learned a crucial lesson: a production agent must be built for the reality of human interaction, not the perfection of a demo.

### MVP outcomes: Early signs of success

Navigating these challenges required a significant effort, but the payoff from our initial MVP release has been immediate and clear. With our new agentic PoliBot handling the end-to-end process, we are already seeing policy rule tickets resolved ~40% faster than before. This powerful early metric has validated the entire journey, proving the immense operational value of evolving from a simple assistant to a truly autonomous teammate.

### Lessons from our agentic AI journey

Our journey transforming PoliBot taught us invaluable lessons. For any leader looking to harness the power of agentic AI, here is the playbook we wished we had from day one.

#### 1\. Evolve a proven winner

Our biggest advantage was starting with PoliBot, a tool the business already valued and trusted. Instead of building a revolutionary agent from scratch, we upgraded a proven success. This lowered the risk, leveraged existing buy-in, and allowed us to focus on the complex task of automation rather than selling a new concept, and was crucial for us to move from a standalone agent to a proper agentic AI solution.

#### 2\. Build the foundation before the agent

We learned that an agent's reasoning is useless without the right infrastructure to act on it. Assessing the foundational "plumbing" — like APIs and communication protocols such as MCP — is a non-negotiable prerequisite before committing to an agentic solution.

#### 3\. Architect for trust from day one

Trust cannot be an afterthought; it must be the foundation. Making every action transparent and auditable was the only way to earn the deep-seated buy-in from our risk, compliance and business partners who would ultimately rely on the agent.

#### 4\. Test the thinking, not just the code

We quickly discovered that testing an agent means testing its judgment, not just its output. Our quality assurance had to evolve to design tests that challenge the agent’s reasoning with ambiguous requests and unexpected tool errors, ensuring it can handle real-world uncertainty, not just ideal scenarios.

#### 5\. Make It a cross-functional mission

An agentic AI project is a business transformation project, not just a siloed IT project. Our success was only possible through a deep partnership where the business defined the value, security built the guardrails, and technology delivered the "how."

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/infographic/tw_10680080917_scaling_agentic_ai_in_finance_web_5.jpg)

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/infographic/tw_10680080917_scaling_agentic_ai_in_finance_mobile_5.jpg)

### Looking back

In essence, our journey scaling PoliBot was a direct response to a fundamental enterprise challenge: moving a successful AI from simply providing answers to taking autonomous action. This technical foundation was the key to bridging the enterprise trust gap; by pairing the agent's "thought process" with a verifiable log of its actions, we enabled a confident human-in-the-loop approval process, creating a clear blueprint for scaling future agentic Al initiatives. Our "expert librarian" is now a proactive, autonomous teammate, and we are just beginning to explore what's possible with this new class of digital colleague.

What challenges have you faced on your own AI scaling journey? Reach out and share your thoughts.