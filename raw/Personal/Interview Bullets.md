- uniquely positioned for a role with Aledade because of my experience in the healthcare vertical
- medscape biggest revenue driver for IB, so thats where I've been deployed for a large portion of my time with the parent company

- Experience as a TPM and my certifications contributed to my leadership skills

## AI Answer Engine

I'm currently the technical lead and architect on the project for a 15-person team, and it is the **#1 priority for the CEO of Internet Brands**. Every architectural decision on this project goes through me.

- Conversational AI service for Medscape clinicians
- Questions could involve research, drug interactions, diagnostic criteria, treatment protocols, and medical imaging analysis
- system returns a structured, source-grounded response streamed back to the user

### Why this matters for the Aledade role

The role description specifically calls out *"partner, as a peer, with Engineering Managers, Product Managers, and stakeholders"* and *"act as a trusted technical decision-maker."* That is the exact shape of what I do on this team every day. 




## AI Topic Cards Agent API

Designed medical summarization system that produces clinically accurate topic cards for physicians through iterative self-correction

- Sits downstream from an ML recommender, which decides clinical topics based on specialty, claims, browsing, lead concepts, and long-term memory data
- My service generates personalized, clinically accurate topic summaries tailored to that specific user
- Contains a multi-agent evaluation loop from each topic to ensure the output meets a quality bar before being persisted

**Orchestration evolution**
- Initial version had three independent agents with subagents, but highly variable runtime
- Made move toward determinism, which solved the problem

**Eval-as-infrastructure evolution**
- First version had individual metrics as tools, agent reasons about which to call - tools would be re-called unnecessarily 
- second version - more deterministic with a FinalDecisionAgent
- Went with parallel python metric execution - deterministic

Scalability
- maximized throughput by running high-concurrency topic workflow execution - 500 concurrent workflows per celery worker by batching GUIDs, each workflow was 2:30-3 min, was able to get 70,000 topics generated in < 6 hours


