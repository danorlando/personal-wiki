---
title: "How to build an Enterprise AI Agent"
source: "https://www.mindtheproduct.com/how-to-build-an-enterprise-ai-agent/"
author:
  - "[[Lisa Murkin]]"
published: 2025-03-10
created: 2026-05-02
description: "How to build an Enterprise AI Agent — Mind the Product"
tags:
  - "clippings"
---
## The Problem: Knowledge lost in the noise

Every organisation accumulates a vast trove of knowledge over time, distributed across tools like Google Drive, Miro, Notion, and Slack. But how often do team members waste hours searching for this knowledge or recreating it from scratch? This isn’t just a minor inconvenience; it’s a productivity drain and a barrier to innovation.

At Elsewhen, I saw an opportunity to address this inefficiency by using generative AI to create an internal enterprise agent designed to make company knowledge more accessible and actionable. This article explores the journey, challenges, and lessons learned while building a proof of concept.  

## Vision: A Smart workforce companion

Imagine a tool that doesn’t just answer questions but becomes a key ally in your daily workflow. This agent would evolve from searching for past project information into a proactive workforce companion. It could generate tailored workshop boards, flag risks based on historical data, and automate or recommend workflow improvements.

**Three objectives underpinned this mission:**

**Maximise past learnings:** Making institutional knowledge more accessible.  
**Reduce inefficiencies:** Reducing the number of low complexity, repetitive tasks or questions.  
**Demonstrating Innovation:** Inspiring further transformation through AI.

## Sprint 0: Building a proof of concept (PoC)

We first started by uploading a few PDFs on ChatGPT from 2 projects and seeing if we had good enough training materials to answer some sample questions. We've built AI solutions for our clients, so I was confident from an engineering perspective that there were some previous learnings or reusable infrastructure and that we could achieve demonstrable value within just 2 weeks of an AI engineer's time. This phase involved:

## Setting clear goals

The primary goal was to create a Slackbot capable of answering questions about past projects, policies, and templates trained upon [Notion](https://www.mindtheproduct.com/beyond-product-led-growth-diversifying-strategies-with-notion-and-figma/). We use Slack every day, so there is a low barrier to adoption. As the product matures and capabilities expand, a Slack bot vs. a standalone tool would be a decision to explore further.

Key objectives included:

**Provide 'useful' responses.** This does not mean every answer needs to be 100% accurate. Giving a summary and linking to a Notion page for further reading would be sufficient.  
**Define a scalable but low maintenance solution architecture.** We aimed to minimise manual overheads. It automatically ingested new content, eliminating the need for engineers to constantly retrain the [LLM](https://www.mindtheproduct.com/llm-workflows-for-product-managers-3-key-takeaways-niloufar-salehi-assistant-professor-at-uc-berkeley-producttank-sf/). We also configured options for different permissions which could be set per project or policy to control access to sensitive information.  
**Create a roadmap with feasible timeframes.** Scraping content from slide decks and Figma provided some of the most interesting insights. We needed a more detailed plan to create a business case and get the budget to sign off on the next phase of work.

## Experimenting with technology

The first question asked was, why can't we just use NotionAI? So whilst training the agent on notion content was the starting point, it wasn't our end goal. NotionAI would solve some immediate problems, it wouldn't unlock the bigger ambition. Plus it's quite expensive to license, and whilst building [software ourselves isn't free](https://www.mindtheproduct.com/figma-and-loveable-team-up-to-increase-no-code-mvps/) – getting stuck into the weeds of scoping out a solution ourselves is also an invaluable experience (and more fun!)

At a high level, there are two key parts to the solution:

- **Retrieval-Augmented Generation (RAG):** For context-aware responses. This is the key differentiator from people today who are just asking ChatGPT. The RAG element vectorising documents and searches through that content rather than generic previous LLM training.
- **ReAct Agent Framework:** To enable decision-making and iterative query refinement. Aka, knowing when to ask an LLM to generate a response and when to follow an automated workflow. Eg, if the user asks Hello, we should respond with Hello – it's not necessary to ask an LLM to generate a response!

## Measuring success

A product is only as good as its ability to deliver value. Whilst we were primarily focused on the goals for Sprint 0. I also considered how we would measure success for an [MVP](https://www.mindtheproduct.com/the-complete-guide-to-building-mvps/). While the ultimate goal is to boost productivity, directly quantifying time saved can be challenging in the short term, especially with a relatively small number of users.

**To get a rounded view of success, we monitored a mix of quantitative and qualitative measures:  
**

- **User Engagement:** Track usage frequency and number of users to gauge initial interest and identify areas for improvement.
- **Response Quality:** Employ user feedback mechanisms like thumbs up/down ratings and periodic surveys to assess user satisfaction
- **LLM-as-a-Judge:** Leverage another LLM to evaluate the accuracy of responses and track improvement over time.
- **User Interviews:** Conduct regular interviews with a diverse user group to gather qualitative feedback and understand how the agent is being used.

I am a fan of having a North Star Metric that can cut through the noise if there are conflicting priorities. My current plan is to use Weekly Active Users because the timeframe is neither too long nor too short, and it is easy to measure. It’s a metric that shouldn’t be that skewed depending on the complexity of user queries either. However, as the product matures and the user base grows, we'll refine our metrics as needed, most likely with a view on returning users. For now, I want to focus on developing the actual product capabilities.

## Key learnings so far

### Start with a narrow scope

By narrowing our initial scope to past project materials accessed via a Slackbot, we achieved quick wins and identified key requirements.

This focused approach allowed us to:

**Curate training materials:** We created a centralised table with backlinks to relevant projects, reducing noise and enabling a simple way to manage access permissions.  
**Improve project structure:** We introduced a new project template to streamline knowledge capture and reinforce best practices.

This [strategy](https://www.mindtheproduct.com/bottom-up-product-strategy-the-state-of-product-by-susana-lopes/) allowed us to deliver value quickly, though it limited our initial exploration of more complex use cases and content types.

### Collaboration is key

Support from the DevOps team was essential to our success. Additionally, getting a day or two of one of our Principal Designers was invaluable with some branding ideas to make the vision feel real. Plus, whilst building a Slackbot is largely an engineering task, it’s important not to underestimate the power of storytelling and a clear narrative. This is how product managers can get buy into the strategy by building a shared understanding of the opportunity.

We presented our work so far at a company-wide Show & Tell. There was positive feedback with a high level of engagement from across the business asking questions or sharing ideas. We even had a Delivery Manager follow up with his own miro board mapping out a workflow where an AI agent could help.

### Review risk appetite

At one point, the TechOps team escalated a concern about a security risk. However, the core project team were really keen to maximise momentum to have the most impactful solution to demonstrate at the end of the sprint. So perhaps we should have prioritised this earlier or raised awareness of the issue, mitigation and timelines for this sooner. But to be honest, I was happy to ask for forgiveness afterwards, rather than wishing we'd focused more here first. However, this is something to consider in future PoCs or at other organisations with different risk appetites.

This is linked to the AI maturity of your organisation and culture of innovation vs fear of failure. In this case, we can’t finalise all details of the solution or quantify the exact impact on the bottom line up front. However, when building AI products, I believe you have to accept there’s more ambiguity to move forwards, and avoid getting left behind in analysis paralysis.

## The road ahead

With the PoC complete, the next steps include mapping out a business case to build the MVP and planning a proper project plan around this. There's further discovery needed from both a technical and product perspective to ensure all important needs and risks are captured and prioritised.

As with many side of desk projects, there’s often slow progress given competing priorities… It took nearly a year from the initial idea to become a PoC. But perseverance is paying off and Sprint 0 alone has given us valuable insights. There's a growing anticipation for what the next phase could look like. So watch this space!

## Discover more great content on Mind the Product

- [What does a product management consultant do anyway?](https://www.mindtheproduct.com/what-does-a-product-management-consultant-do-anyway/)
- [Does product management only work for tech and startups?](https://www.mindtheproduct.com/does-product-management-only-work-for-tech-and-startups/)
- [Product Minds: Building ChatPRD – Claire Vo (CPO, LaunchDarkly, ChatPRD)](https://www.mindtheproduct.com/product-minds-building-chatprd-claire-vo-cpo-launchdarkly-chatprd/)