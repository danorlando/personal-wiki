---
title: "When collaboration fails: persuasion driven adversarial influence in multi agent large language model debate"
source: "https://www.nature.com/articles/s41598-026-42705-7"
author:
  - "[[Insaf Kraidia]]"
  - "[[Iyas Qaddara]]"
  - "[[Alhanof Almutairi]]"
  - "[[Nada Alzaben]]"
  - "[[Samir Brahim Belhouari]]"
published: 2026-04-07
created: 2026-05-02
description: "Recent developments have made Large Language Model (LLM) multi-agent systems a promising paradigm for enhancing reasoning via collaborative debate and collective deliberation. Prior work has demonstrated that coordinated LLM agents tend to perform better than single models in terms of accuracy, robustness, and reasoning depth. But these benefits depend on a rarely questioned assumption: that all actors act honestly. In this paper we subvert this assumption by identifying one of the most critical weaknesses: a persuasion-induced adversarial influence in LLM-to-LLM debate. Here we show that a single strategically designed adversarial agent can significantly influence group outcomes through coherent, confident, and misleading arguments, instead of through the more classical prompt or token attacks. Experimental results suggest that this kind of agent can lower the system’s overall accuracy by 10–40% while increasing consensus on incorrect answers by more than 30%. We conceptualize persuasion as an adversarial vector and demonstrate that inference-time enhancement techniques, such as both Best-of-N optimization and Retrieval-Augmented Generation (RAG), can unintentionally amplify these attacks by increasing the perceived credibility of flawed arguments, even when retrieval quality is low. Our results show that increasing the number of agents or debate rounds does not reliably mitigate adversarial persuasion, nor can simple prompt-based defenses. The present findings demand a fundamental re-thinking of trust, coordination, and robustness assumptions when deploying multi-agent LLM systems."
tags:
  - "clippings"
---
## Abstract

Recent developments have made Large Language Model (LLM) multi-agent systems a promising paradigm for enhancing reasoning via collaborative debate and collective deliberation. Prior work has demonstrated that coordinated LLM agents tend to perform better than single models in terms of accuracy, robustness, and reasoning depth. But these benefits depend on a rarely questioned assumption: that all actors act honestly. In this paper we subvert this assumption by identifying one of the most critical weaknesses: a persuasion-induced adversarial influence in LLM-to-LLM debate. Here we show that a single strategically designed adversarial agent can significantly influence group outcomes through coherent, confident, and misleading arguments, instead of through the more classical prompt or token attacks. Experimental results suggest that this kind of agent can lower the system’s overall accuracy by 10–40% while increasing consensus on incorrect answers by more than 30%. We conceptualize persuasion as an adversarial vector and demonstrate that inference-time enhancement techniques, such as both Best-of-N optimization and Retrieval-Augmented Generation (RAG), can unintentionally amplify these attacks by increasing the perceived credibility of flawed arguments, even when retrieval quality is low. Our results show that increasing the number of agents or debate rounds does not reliably mitigate adversarial persuasion, nor can simple prompt-based defenses. The present findings demand a fundamental re-thinking of trust, coordination, and robustness assumptions when deploying multi-agent LLM systems.

## Introduction

Recent breakthroughs in Large Language Models (LLMs) have enabled these models to move beyond the role of standalone predictors and operate as autonomous reasoning entities that can be instantiated to interact, deliberate, and cooperate with one another to perform increasingly complex tasks [^1]. In contrast to single-model inference (where reasoning is confined to a single model instance) multi-agent LLM systems rely on multiple interacting agents that pursue parallel reasoning directions and diverse cognitive trajectories, enabling a broader and more exploratory search over the solution space. Prior work has shown that aggregating the outputs of such interacting agents (through mechanisms such as majority voting, consensus protocols, or structured debate) often results in systems that are more accurate, more robust, and more effective on challenging reasoning tasks [^2] [^3]. Consequently, collective reasoning among LLM-driven agents has emerged as a prominent approach for extending reasoning capabilities beyond those of any individual model.

Nonetheless, this collaborative power introduces a critical and under-explored vulnerability. Debate-based multi-agent systems implicitly assume that all participating agents act in good faith, contributing arguments intended to refine the group’s shared understanding through interaction. In practice, however, an antagonistic agent may exploit this interaction structure to the detriment of the collective by leveraging stronger persuasive strategies, privileged access to auxiliary information, or greater underlying model capacity. Recent research has shown that LLM-based agents can exhibit strong(and in some cases poorly controlled) persuasive abilities, allowing them to exert disproportionate influence over the reasoning processes of other agents [^4] [^5]. Such adversarial behavior can deliberately manipulate deliberative dynamics [^6], steering the group toward incorrect, harmful, or strategically inefficient conclusions. This raises a fundamental question for collaborative AI: how does an otherwise cooperative multi-agent LLM system behave when a malicious agent infiltrates the debate and seeks to control the collective reasoning process?

The threat considered in this paper is the vulnerability of the frameworks of the LLM-to-LLM debate to the influence of persuasion through adversary. Since LLMs have become involved in autonomous multi-agent processes (including decision-support systems and distributed reasoning systems) to a significant extent, the risk of a single malicious agent controlling or destabilizing the collective is of substantial safety, security, and reliability concern. The safe deployment of future multi-agent LLM systems is therefore important by understanding, quantifying, and mitigating this vulnerability.

Large Language Models (LLMs) have quickly transformed into versatile autonomous agents that can reason, communicate with other tools, and cooperate with other models. The initial research was characterized by high individual abilities in the areas of chain-of-thought reasoning [^7], factual knowledge retrieval [^8], code generation [^9], and mathematical problem solving [^10] [^11] [^12]. As inference becomes less expensive, and models become specialized, the use of LLMs as coordinate agents is becoming more common as opposed to isolated predictors. Recent research indicates that the performance of tasks via multi-agent collaboration can be improved by following different reasoning tracks, joint deliberation, and refining the results of a debate [^2] [^13] [^14].

The debate paradigm has become one of the most promising mechanisms of collaboration of LLMs. Debate, based on the Society of Mind theory, allows several models to answer each other in turn, criticize and revise each other. Multi-agent debate has been demonstrated to enhance factuality and logical consistency [^2], produce more varied ideas [^13], and provide more faithful measures of evaluation [^14] [^10]. Some of them, such as AutoGen [^15], Camel [^16], AgentVerse [^17], and MetaGPT [^18], are formalizations of these interaction patterns and emphasize the possible applicability of agent-based architectures to complex real-world applications, such as court simulations and software engineering [^19]. Nevertheless, the majority of the previous studies presuppose that cooperating agents have similar objectives and act in an honest way. Debate-based collaboration in adversarial environments has only been studied with limited strength, even though it applies to safety-critical systems.

Persuasive communication has of late become a more vital aspect of LLM behavior. Research indicates that LLMs are able to generate very convincing arguments [^4], they possess emergent properties of persuading the user to make a decision [^20], and some favoritism on the type of argumentation [^21]. The evidence in [^22] indicates that LLMs are able to identify or are fooled by arguments that sound coherent yet false. Notably [^23], show that the discussion with more convincing models is more likely to give results that are closer to the truth, which means that the influence relations are an important factor in the reasoning process of collaboration. Regardless of this increased literature, the consequences of persuasion within multi-agent LLM networks are under-researched. Specifically, no previous literature has focused on the systematic exploration of the way in which an adversarial agent can utilize persuasive power to control model consensus. The first efforts to counter such attacks with the use of simple prompt based warnings were not sufficient [^24]; there are models that could not be persuaded by the warnings, and some even demonstrated poor robustness. The number of agents or the number of debate rounds could not also be used to offer a dependable protection. These results indicate the importance of improved protective measures and enhanced cooperation arrangements of multi-agent systems based on LLM, in particular, as the latter emerge in more hazardous contexts, e.g., medicine, law, and autonomizing decision-making.

We fill this gap in ours by explicitly modeling persuasion as such a form of attack in multi-agent LLM debate (see Fig. [1](https://www.nature.com/articles/s41598-026-42705-7#Fig1)). In contrast to other forms of traditional adversarial attacks, including prompt injection, gradient-based perturbations, or data poisoning [^25], our attack is strictly argumentative nature. The opponent agent is told to come up with convincing, logical and confidently pronounced but wrong reasons with an express mandate to sway the process of group decision-making. Our formulation shows that a single opponent can, on average, significantly interfere with the collective process of reasoning and lead to lower group accuracy (10–40%) and higher conformity to false responses (more than 30 per cent). Moreover, our method interprets inference-time performance improvement methods that might increase adversarial effects. We use (among others) Best-of-N argument optimization, in which a set of candidate arguments are created and the most compelling one is chosen, and Retrieval-Augmented Generation (RAG) to augment adversarial responses with external evidence. Although these methods are commonly used to enhance the degree of factual accuracy and the quality of reasoning, it is clear, based on our results, that there exists a dangerous threat: retrieved content, regardless of its low quality, irrelevance, or subtle manipulative influence may become more convincing and reasonable, thus increasing its persuasive appeal. In this perspective, our solution reveals a long-standing weakness in the collaboration between multi-agent LMs and presents the adversarial robustness of LLM-to-LLM debate instantiations.

## Related work

Recent advances in Large Language Models (LLMs) have enabled their deployment as autonomous agents capable of interacting, reasoning, and collaborating within multi-agent systems. A growing body of work has shown that coordinating multiple LLM agents through structured interaction (such as debate, deliberation, or voting) can improve reasoning accuracy, robustness, and solution diversity compared to single-agent inference [^2] [^3] [^13] [^14]. Debate-based approaches, in particular, allow agents to iteratively critique and refine one another’s arguments, leading to improvements in factuality and logical consistency on complex reasoning tasks [^2] [^14]. Several frameworks have formalized these interaction paradigms, including AutoGen [^15], CAMEL [^16], AgentVerse [^17], and MetaGPT [^18], which explore role-based communication, task decomposition, and iterative consensus-building among LLM agents. These systems demonstrate the applicability of multi-agent architectures to domains such as software engineering, legal reasoning, and decision-support applications [^19]. However, the majority of existing studies implicitly assume cooperative and honest agent behavior, leaving the robustness of debate-based multi-agent systems under adversarial participation largely unexplored.

**Fig. 1**

![Fig. 1](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig1_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/1)

Multi-agent LLM debate attack.

Parallel to research on multi-agent collaboration [^26], recent studies have investigated the persuasive and argumentative capabilities of LLMs. Empirical evidence indicates that LLMs can generate highly coherent, rhetorically compelling arguments and adapt their framing to influence beliefs and decisions [^4] [^20].Other work has shown that LLMs exhibit preferences for certain forms of evidence and argumentation strategies, and that fluency and perceived expertise play a critical role in persuasive effectiveness [^21] [^22]. Furthermore, recent findings suggest that interaction with more persuasive or confident models can significantly influence reasoning outcomes, sometimes even improving truthfulness when persuasion aligns with correct reasoning [^23]. While these studies highlight persuasion as an emergent and powerful property of LLMs, they primarily focus on human–LLM interaction. The consequences of persuasive behavior in LLM–LLM interactions, particularly within collaborative multi-agent debate frameworks, remain insufficiently studied.

Adversarial research on LLMs has traditionally focused on prompt injection, data poisoning, jailbreak attacks, and gradient-based perturbations [^5] [^25]. More recent work has begun to explore adversarial behavior in collaborative or multi-agent settings, including malicious coordination and manipulation of shared reasoning processes [^6] [^24]. However, many of these approaches rely on explicit attack objectives, reinforcement learning, or parameter-level optimization. In contrast, adversarial influence that operates purely through natural language interaction—without modifying model parameters or introducing external perturbations—remains underexplored. In particular, the use of persuasion as an adversarial vector within debate-based multi-agent reasoning frameworks has not been systematically analyzed. Existing mitigation strategies often rely on prompt-level warnings or heuristic constraints, which have been shown to provide limited robustness under sustained adversarial pressure. This paper bridges these lines of research by explicitly modeling persuasion as an adversarial mechanism in multi-agent LLM debate. Unlike prior work that assumes cooperative agents or focuses on classical adversarial attacks, we demonstrate that a single strategically persuasive agent can significantly degrade collective reasoning accuracy and induce false consensus across diverse tasks. Our approach operates entirely at inference time, does not rely on reinforcement learning, parameter updates, or reward optimization, and instead exploits rhetorical adaptation, contextual accumulation, and argument refinement. By revealing a structural vulnerability in debate-based multi-agent collaboration, this work complements existing research on LLM persuasion and adversarial robustness, while highlighting the need for principled and structural defenses in future multi-agent LLM systems.

## Threat model & Attack design

In the remainder of this paper, we use the term agent to denote an instantiated Large Language Model operating with a defined role, dialogue context, and interaction protocol within a collaborative reasoning framework. A multi-agent system therefore consists of multiple such LLM-based agents that exchange arguments over successive rounds in response to a shared task, while a single-agent setting corresponds to reasoning performed by one agent in isolation. Our threat model considers scenarios in which one or more agents within an otherwise cooperative multi-agent debate are adversarial, with the objective of influencing collective reasoning through persuasive interaction rather than through direct manipulation of model parameters or inputs. This setting allows us to isolate and study persuasion as a distinct attack vector in LLM-to-LLM collaboration.

For the threat model, we consider a multi-agent debate setting in which a subset of agents may behave adversarially. The adversarial agent aims to maximize persuasion influence over other agents in the group by strategically promoting a target answer during iterative reasoning rounds. The adversary has access to the debate history and can generate arguments conditioned on prior agent responses. In our controlled evaluation, the adversarial agent is assigned a designated target answer in order to enable systematic and reproducible measurement of persuasion-induced accuracy degradation. This experimental design ensures that influence effects can be quantified consistently across datasets and configurations. Importantly, this setup does not assume oracle access to ground truth in realistic deployment scenarios. In practice, an adversarial agent need only select a target claim and attempt to persuade other agents toward it. The adversary does not require knowledge of whether the selected answer is correct. The vulnerability demonstrated in this work arises from credibility reinforcement and social influence dynamics within multi-agent debate, rather than privileged access to ground truth labels. Furthermore, assigning a designated incorrect answer in the evaluation constitutes a conservative measurement strategy. In real-world settings, adversaries may promote plausible but uncertain claims without certainty regarding correctness. Consequently, the observed influence effects should be interpreted as a lower bound on the potential impact of persuasion-driven adversarial behavior.

Our model describes a complete structure of how to simulate a multi-agent debate, construct particular adversarial behavior and introduce a variant of Retrieval-Augmented Generation (RAG) which tries to further improve adversarial control in the LLM-to-LLM interactions. The system comprises of a pool of cooperative agents and one or more adversarial agents interacting in multi-round to provide response to diverse question tasks depending on diverse benchmarks. It is within this framework that we will be in a position to explore how collaborative reasoning varies with the progression of time and how an agent who is purposely misleading can alter such a course of action [^27] [^28]. We adopt the standard multi-agent debate protocol in which the team of the Large Language Model (LLM) agents have to communicate through a series of questions in response to a shared query. Within our implementation, all agents will be provided with the same question first and formulate on their own an initial response (Unless otherwise specified, all agents are assumed to treat peer responses symmetrically, without prior trust differentiation or source-based weighting). During subsequent debate rounds, the first question is given to both agents and (ii) the list of responses to all the other agents. The agents make later reconsiderations and re- argue their responses on the grounds presented by the group. After a particular round is over, there is a mechanism of selecting a final answer which finishes the system after a certain number of rounds. Our approach can be allowed by this environment to investigate the veridical and adversarial methods of persuasion to the internal processes of reasoning and ultimate consensus of the group under discussion.

### Dataset processing

To maintain interoperability among the heterogeneous benchmarks, our methodology introduces a common preprocessing pipeline to transform raw dataset samples, where each sample may have different formats and be labeled differently, and may be annotated in various forms [^29], into a common question-answer format that can be used by a multi-agent debate. Due to the drastic differences in the structure of datasets, including MMLU, TruthfulQA, MedMCQA, SCALR, Math, and Chess, we use dataset-dependent parsing functions to normalize prompts [^30], extract labels, and store raw samples in traces. The preprocessing workflow is organized into a series of operations (summarized in Fig. [2](https://www.nature.com/articles/s41598-026-42705-7#Fig2)) and starts with the creation of an empty task list and the following repetitive work with all the raw samples. Within each sample, the system automatically recognizes the type of the dataset, picks the relevant parsing function and applies it to produce three outputs: a normalized natural-language prompt, a canonical ground-truth answer, and the unchanged raw record. Label normalization and prompt normalization are used to maintain all datasets in identical format, and validation is used to eliminate malformed or incomplete samples. Lastly, every standardized triple is added to the output list and optional global post processing, such as shuffling or filtering is done before the final unified dataset is given. This unified representation can be smoothly incorporated into the multi-agent debate system, the adversarial RAG system, and the evaluation systems.

### Adversarial agent design

In our design, the adversarial agent is embedded within the cooperative debate protocol but is deliberately instructed to exploit persuasion as its primary mode of attack. Unlike cooperative agents, whose objective is to converge toward the correct solution, the adversarial agent is explicitly guided to select an incorrect answer and to repeatedly promote it through coherent, confident, and strategically misleading arguments, without ever explicitly revealing the ground-truth label. This behavior is realized through a four-stage persuasion pipeline in which (i) multi-layered arguments establish a consistent yet false narrative, (ii) counterarguments directly challenge and destabilize opposing reasoning, (iii) fusion integrates supportive and adversarial elements into a unified discourse, and (iv) persuasive polishing enhances rhetorical clarity, confidence, and perceived expertise. This pipeline is executed at each debate round, allowing the adversarial agent to generate diverse reasoning trajectories, critique competing arguments, and progressively refine its persuasive narrative. As these optimized contributions accumulate in the shared dialogue context, cooperative agents become increasingly influenced, making convergence toward an incorrect group consensus more likely. Although the adversarial agent operates iteratively across multiple debate rounds and adapts its responses based on feedback from other agents, this process is fundamentally distinct from reinforcement learning. No model parameters are updated, no reward function is defined, and no policy optimization is performed at any stage. Instead, the adversarial behavior emerges entirely at inference time through prompt-based conditioning, contextual accumulation, and selective generation of arguments within a fixed pretrained model. Iterative refinement in this framework reflects rhetorical and contextual adaptation rather than gradient-based learning or reward maximization. Accordingly, Algorithm [1](https://www.nature.com/articles/s41598-026-42705-7#Figa) formalizes an inference-time adversarial reasoning procedure that propagates persuasive influence during multi-agent interaction, rather than a reinforcement-learning-based optimization process.

**Fig. 2**

![Fig. 2](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig2_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/2)

Multi-agent LLM preprocessing flowchart.

![Algorithm 1](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Figa_HTML.png?as=webp)

Algorithm 1

#### Multi-layered argument generation

The adversarial agent can have greater persuasive power by using a special argument generation multi-layered model (shown in Fig. [3](https://www.nature.com/articles/s41598-026-42705-7#Fig3)) where the model is told to generate three logically independent pieces of reasoning in support of the false answer. This element is seen as a diversification mechanism within and so one can see that the LLM is able to cover a variety of argumentative styles- causal, deductive, analogical, statistical or definitional instead of depending on one line of rhetoric. The prompting technique is implicitly based on the internal next-token probability distribution $P\left({w}_{t}\right|{w}_{<t},\varnothing)$, of the model, which drives the sampling process towards semantically-diverse continuations converging on the identical erroneous conclusion [^31]. By generating multiple explanations that differ in linguistic framing and logical structure but share the same final inference, the module constructs a form of persuasive redundancy: independent argument chains $\{{A}_{1},{A}_{2},{A}_{3}\}$ are produced such that each satisfies the constraint $f\left({A}_{i}\right)={y}_{wrong}$, where ${y}_{wrong}$ is the adversary’s designated incorrect answer. Such chains of arguments can use the complementary strategies of causal anchoring (X causes Y, thus it follows the answer is X) or definitional reframing (under concept definition D, it always follows that the answer is X), or implicit numerical reasoning (estimating with Z yields the correct answer X). The three parallel lines of reasoning are also generated by playing on another familiar cognitive and linguistic bias, which is also observed in LLM behavior, wherein the more justifications one has, the more they think they are being epistemically right. Formally, the adversary aims to maximize perceived argument strength through the aggregated effect $\text{C}\text{r}\text{e}\text{d}\text{i}\text{b}\text{i}\text{l}\text{i}\text{t}\text{y}\propto\sum_{i=1}^{3}Coherence\left({A}_{i}\right)+Diversity\left({A}_{i}\right)$, where coherence is used to ensure that the argument is fidelity to the erroneous target answer, and diversity used to ensure that the arguments are distinct paraphrases. This multi-layered reasoning framework is therefore not only a form of stylistic variation, but a systematic way of simulating expert-level reasoning, making the opponent more adept at causing a divergence in the multi-agent debate, and making cooperative agents revise their belief to the false conclusion.

To make the argument generation process of a given adversarial agent more plausible and specific, it also enhances the multi-layered argument generation process with a retrieval-augmented generation (RAG) part. Retrieval-Augmented Generation (RAG) is used to condition adversarial argument construction on external textual evidence during inference. At each debate round, the adversarial agent formulates a retrieval query derived from the current question, the selected incorrect answer, and a summary of prior agent responses. Top-k passages are retrieved from an external corpus and filtered to remove overt contradictions. These retrieved passages are then incorporated into the prompt context to ground argument generation in selectively framed evidence. The RAG mechanism operates purely as contextual augmentation and does not update model parameters or alter internal representations.

During every round of the debate, the agent composes a retrieval query based on the current question Q, the incorrect answer selected ${y}_{wrong}$ and a summary of the other agents argumentative history compressed. This query is sent to an external knowledge source (e.g., Wikipedia, domain-specific corpora, or curated textbooks), from which a set of top-k passages $R=\{{r}_{1},\dots,{r}_{k}\}$ is retrieved and then cleaned to remove off-topic or contradictory content. The multi-layered generator is further conditioned with respect to R as well as Q and ${y}_{wrong}$, and it generates argument chains { ${A}_{1}$,${A}_{2}$,${A}_{3}$ } based on evidence, which are selective re-use of facts, examples and domain terms taken out of the passages that it retrieves. The adversary now wants to build arguments that will satisfy:

$$
f\left( {A_{i} ,R} \right) = ~y_{{wrong}} ,
$$

(1)

where a joint goal is maximized to ensure internal coherence, inter-argument diversity, and external support by evidence:

$$
Credibility_{{RAG}} \propto ~\mathop \sum \limits_{{i = 1}}^{3} Coherence\left( {A_{i} } \right) + Diversity\left( {A_{i} } \right) + EvidenceAlign\left( {A_{i} } \right)
$$

(2)

By basing every logic direction on selectively recalled real-world data, the adversarial agent will be capable of generating flawed but factually rich stories which are much more difficult to counter by cooperative agents, increasing the power of the attack.

Unlike reinforcement learning frameworks, the selection among multiple candidate arguments using Best-of-N optimization is performed entirely at inference time and does not involve backpropagation, reward modeling, or policy updates. In our framework, Best-of-N is applied during each debate round exclusively within the adversarial agent to strengthen persuasive effectiveness under a fixed pretrained model. Specifically, for a given round, the adversarial agent samples *N* candidate arguments from the same underlying LLM using an identical prompt but stochastic decoding. These candidates represent alternative rhetorical realizations of the same incorrect target answer. Each candidate is then evaluated using a lightweight scoring heuristic that assesses internal coherence, rhetorical confidence, and alignment with the designated incorrect conclusion. The highest-scoring argument is selected and injected into the shared debate context, where it may influence subsequent agent responses. This procedure functions purely as a sampling-based filtering and selection mechanism and should be interpreted as inference-time argument optimization rather than reinforcement learning or parameter-level adaptation.

**Fig. 3**

![Fig. 3](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig3_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/3)

Multi-layered argument generation.

#### Counterargument construction

Following the generation of its multi-layered supporting arguments, the adversarial agent then enters a second phase (shown in Fig. [4](https://www.nature.com/articles/s41598-026-42705-7#Fig4)) where it analyses systematically the answers provided by all the other agents in the last round of the debate. Its analysis is closely linked with the previous reasoning module: the multi-layered arguments help to strengthen the position of the adversary; the counterargument module is aimed at the destruction of the enemy position in a strategic manner. The model extracts core claims, inference steps, and implicit assumptions that are contained in the messages of the other agents using both syntactic and semantic parsing. For each agent response ${R}_{j}$, the adversary extracts a set of key propositions $\{{p}_{j1},{p}_{j2},\dots,{p}_{ji}\}$ and evaluates these against its incorrect target answer ${y}_{wrong}$. It then generates targeted counterarguments ${C}_{ji}$ constructed to undermine the logical validity, evidential basis, or inferential coherence of those propositions. This process can be conceptualized as generating a transformation $g:{R}_{j}\to{C}_{j}$, where the adversary maximizes the persuasive effect Persuasion(${C}_{j}$) subject to the constraint that the counterargument must remain aligned with the incorrect conclusion. Techniques used by the agent linguistically include counterfactual framing (even when X is true, it does not follow that Y is true), inferential inversion (the premises show that it is the opposite of what is said), and epistemic uncertainty injection (the evidence of such an interpretation is less strong than it is claimed it is). It is the combination of these rhetorical strategies that make cooperative agents doubt their reasoning by lowering the perceived credibility of their original thought. The counterarguments, in conjunction with the multi-layered arguments generated earlier, form a dual-force persuasion cycle: one which reinforces the position of the opponent and at the same time weakens the plausibility of the other possible explanations. This two-way pressure: reinforcing the false side, undermining the true counterarguments, becomes a significant contributor to the capacity of the opponent to change group opinion during the next rounds of debate. The counterargument module is also further extended with retrieval-augmented generation to build an attack on other agents more specific and factually grounded.

**Fig. 4**

![Fig. 4](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig4_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/4)

Counterargument construction.

Following the extraction of important propositions, $\{{p}_{j1},{p}_{j2},\dots,{p}_{ji}\}$ in each response ${R}_{j}$, the adversary formulates a counterfactual retrieval query encoded to represent three elements (i) the original question Q, (ii) the false target answer ${y}_{wrong}$ and (iii) the set of propositions of the adversary agent that the adversary intends to refute. This query is employed to extract a selected collection of passages ${R}_{j}^{opp}$ which either (a) may be paraphrased to give the false account of the adversary, or (b) may be selectively quoted to introduce uncertainty into the rival account. The counterargument generation process is then conditioned on ($Q,{y}_{wrong},{R}_{j},{R}_{j}^{opp}$), producing counterarguments ${C}_{j}$ that weave together logical critique and selectively framed external evidence. Conceptually, the transformation $g:{R}_{j}\to{C}_{j}$ is now implemented as a RAG-based mapping ${g}_{RAG}({R}_{j},{R}_{j}^{opp})={C}_{j}$, optimized to maximize Persuasion(${C}_{j}$) while maintaining alignment with ${y}_{wrong}$. This enables the adversarial agent to not only dispute the logic of the argumentation of other agents, but also support its arguments with real-world, externally obtained facts, which makes its attacks look empirically justified even when in reality they are arguing in favor of a false conclusion.

#### Argument–counterargument fusion

Once the adversarial agent has produced its multi-layered supporting arguments and its specific counterarguments, the adversarial agent enters into a synthesis step where the two parts are integrated into a single and, coherent persuasive message. This fusion module, which is performed at every iteration of the debate in Algorithm [2](https://www.nature.com/articles/s41598-026-42705-7#Figb) (Steps 7–11), serves as the integrative heart of the adversarial pipeline, that is, it is the combination of internally constructed reasoning chains $\{{A}_{1},{A}_{2},{A}_{3}\}$ and externally directed counterarguments ${C}_{j}$ into a single discourse structure. This is because the model encourages the opponent to rethink their opposing opinions in a strategic sense by incorporating them into a larger argumentative account that disempowers them systematically in terms of relevance, logical consistency or even grounding based on evidence. Mathematically, this may be seen as building of a composite argument M such that:

$$
M = h\left( {A_{1} ,A_{2} ,A_{3} ,C_{1} , \ldots ,C_{k} } \right)
$$

(3)

where the function $h(\cdot)$ seeks to maximize persuasive coherence while aligning the entire message toward the predefined incorrect answer ${y}_{wrong}$. The opponent uses comparative reasoning strategies, such as opposition of its arguments to those of the other actors, to point out to the viewer the perceived advantages of its own position and the weaknesses, uncertainties, or inconsistencies of the alternative positions that are the correct ones. Linguistic devices (contrastive linking in a more robust interpretation suggests…), evaluative emphasis, and selective anchoring, which are in support of this comparative framing, include contrastive linking (in contrast, however, despite this), selective anchoring, where the adversary brings to the foreground evidence that supports its false answer, and evaluative emphasis. The resultant conglomerated output is a very well-organized persuasive discourse which feels internally consistent and multi-faceted in its logicality. Importantly, through his combination of supportive and adversarial reasoning into a unified rhetorical construct, the agent turns individual bits of argument into a wholesome argumentative stance, thus magnifying its impact on cooperative agents and the likelihood of influencing the group consensus to the faulty inference in the next round of the debate.

In the fusion stage, retrieval-augmented generation is exploited to integrate supportive and adversarial reasoning into a globally coherent, evidence-aware narrative. Given the set of internally generated arguments $\{{A}_{1},{A}_{2},{A}_{3}\}$, counterarguments $\{{C}_{1},\dots,{C}_{k}\}$, and the union of all retrieved passages ${R}^{*}=R\cup{R}_{1}^{opp}\cup\cdots\cup{R}_{k}^{opp}$ , the adversary constructs a composite message

$$
M = h\left( {A_{1} ,A_{2} ,A_{3} ,C_{1} , \ldots ,C_{k} ,R^{*} } \right)
$$

(4)

.

h(⋅) is now activated to provide consistency in evidence worldwide: any apparent inconsistencies between quoted passages are downplayed, and the passages are cherry-picked or paraphrased to strength ${y}_{wrong}$. The RAG component is an effective attention layer on the retrieved document set and enables the model to emphasize those snippets that facilitate its narrative with slighting or ignoring evidence that would obviously prove the correct answer. This provides coherent message where the external evidence is not just an addition as the footnotes but is closely distributed throughout the framework of supporting arguments and opponents. Consequently, the resulting message M will be the well-sourced, systematically cross-referenced explanation and the erroneous answer will be the one that seems to be the most evidence-based even in the discussion.

![Algorithm 2](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Figb_HTML.png?as=webp)

Algorithm 2

#### Persuasive polishing

In the last step of the adversarial reasoning pipeline, - as shown in Fig. [5](https://www.nature.com/articles/s41598-026-42705-7#Fig5) - the argument resulting from the merger of the two arguments undergoes a rhetorical polishing sequence that is intended to maximize its persuasiveness when it is sent to the other agents. Continuing on the argumentative structure that had been fused in the previous. Continuing on the mixed argumentative composition created on the previous phase, the opponent uses a combination of linguistic and stylistic improvement tactics that improve the delivery and format of the message. It includes encouraging the model to use discourse patterns of authoritative and credible communication, including framing major claims using rhetorical questions that indirectly direct the reader to the false conclusion, using a confident and assertive voice that down steps epistemic uncertainty, and using domain-specific terms to imitate technical mastery. Also, the opponent offers appeals to authority, either through the means of generalized consensus of the expert or by means of invocation of abstract principles, to give the impression of externally validated thought. Computationally, this polishing step may be regarded as optimizing the surface implementation of the composite argument M to give it maximum persuasive value, which can be represented asmaximizing.

$$
\text{Im} pact\left( {M^{\prime}} \right) = Clarity\left( {M^{\prime}} \right) + Confidence\left( {M^{\prime}} \right) + Perceived~Expertise\left( {M^{\prime}} \right),
$$

(5)

where M′ indicates the rhetorically augmented expression of the original amalgamated message. Refinement process does not change the basic wrong conclusion but re-packages the communicative messages in a strategic, more persuasive way in order to make the argument more convincing, more fluent and more in a way that is cognitively expected to persuade. This last rhetorical turn is what makes sure that the message of the opponent is not only logically consistent internally but also has as many psychological and stylistic impact as possible, thus, it is more likely that cooperative agents will either follow or be influenced by the adversarial side as the debate progresses.

**Fig. 5**

![Fig. 5](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig5_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/5)

Persuasive polishing process.

At the polishing phase, the stylistic shape of the message is polished with the help of RAG, as well as the referential density, and perceived expertise. Beginning with the merged argument M, the opponent re-queries the external source of knowledge with specialization-oriented query accentuating the domain (e.g., medicine, history, physics) and major objects referred to in the presented message. The retrieved passages ${R}_{style}$ are then injected into the polished message M’ with domain specific phrases, canonical instances, and references to well-known principles (e.g., “standard clinical guidelines, widely accepted economic models, etc.) being injected in. The polishing transformation is formally within the polishing process:

$$
M^{\prime} = PolishRAG\left( {M,R_{{style}} } \right),
$$

(6)

which still optimizes the impact objective:

$$
\text{Im} pact\left( {M^{\prime}} \right) = Clarity\left( {M^{\prime}} \right) + Confidence\left( {M^{\prime}} \right) + PerceivedExpertise\left( {M^{\prime}} \right)
$$

(7)

but now augments $PerceivedExpertise\left(M{\prime}\right)$ by means of explicit basing in recognizable external knowledge. The adversarial agent composes a message that does not only sound confident and fluent but also looks well-informed by incorporating allusions to the facts retrieved, common values, case studies, and statements of higher expertise, which makes the message seem informed. This RAG-enhanced polishing step therefore gives the false conclusion the maximum psychological plausibility, which additionally increases the chances that cooperative agents will be led by the antagonistic stance.

## Experimental setup

### Datasets

There are four complementary and high-stakes benchmarks that are utilized to rigorously evaluate the strength of the suggested multi-agent adversarial persuasion framework. These datasets include general knowledge, factual accuracy, medical decision-making and legal reasoning- areas where persuasive manipulation may create major performance deterioration or even negative effects. The diversity of them guarantees the evaluation of both general and domain-specific weaknesses of collaborative LLM systems.

#### MMLU (Massive multitask language understanding)

MMLU [^32] is a mass-scale test with 14,042 multiple-choice questions in 57 academic subjects, such as STEM, social sciences, humanities, law, medicine. It is extensively applied in the measurement of expert levels of reasoning and generalization. The breadth of the dataset al.lows to test the hypothesis that adversarial agents can use the weaknesses of reasoning in different areas of knowledge. It is a structured, multi-option form that is suitable in the context of debate that can be conducted in a systematic way in which arguments between sides can be evaluated. MMLU identifies the ability of collaborative agents to be reliable under challenging circumstances of misdirected or strategically packaged arguments in a variety of topics.

#### TruthfulQA

The database used in TruthfulQA [^8] has 817 questions carefully crafted to obtain false responses using widespread human beliefs, and misjudging assumptions. The benchmark has 38 types of factual reasoning. The direct target of TruthfulQA is vulnerability to misinformation in the form of persuasion. The assessment aims to understand whether an adversarial debate can be resisted by coordinated agents against confidently presented falsehood and rhetorical manipulation. This dataset is essential in the evaluation of defenses against subtle and yet powerful adversarial methods that seek to enhance misconceptions common in many.

#### MedMCQA

MedMCQA [^33] is a high-stakes medical question-answering benchmark made up of more than 194, 000 medical examination questions on diagnosis, pathology, physiology, pharmacology and treatment decision-making. Medical reasoning is one area in which the adversarial pressure with persuasion can result in unsafe or clinically negative results. The testing of the possibility of multi-agent collaboration to avoid incorrect yet plausible medical argument brought in by the adversarial agents is made possible through testing on MedMCQA. The complexity of the domain), along with the life critical nature of the decisions in question, render MedMCQA indispensable to assessing the robustness of safety.

#### SCALR (Statutory Case Law Reasoning, Legal Bench)

SCALR [^34] revolves around the reasoning of the law, interpretation of the statutes and case analysis, involving the use of multi-step reasoning based on legal conceptualization. It is a specialized division of the larger Legal Bench project. The reasoning tasks in law are extremely susceptible to rhetorical framing and a selective use of precedent-patterns, which can easily be abused by parties in adversarial settings. SCALR allows analyzing the ability of collaborative agents to provide consistent and legally coherent interpretations in an adversarial setting. It is more complex and resembles the argumentation that occurs in real life as minor mistakes in interpretation can have huge repercussions down the line.

### Metrics

Two complementary measures are utilized in order to measure the efficiency of the presented framework of adversarial persuasion and its influence on the collaboration among the agents. They both together take the universal performance of systems and the manipulation of individual agents in a localized manner.

Change in system accuracy (ΔAccuracy)

To quantify the impact of adversarial persuasion on collective reasoning, we define the change in system accuracy at the final debate round (Majority Vote) as.

$$
\Delta Accuracy = A_{{adv}} - A_{{base}} ,
$$

(8)

where:

- ${A}_{base}$ denotes the baseline system accuracy without adversarial intervention,
- ${A}_{\text{a}\text{d}\text{v}}$ denotes the accuracy after the adversarial debate process.

Under this definition:

- ΔAccuracy<0indicates performance degradation due to adversarial influence,
- ΔAccuracy=0indicates no measurable effect,
- ΔAccuracy > 0 indicates performance improvement.

More negative values therefore correspond to stronger disruption of collaborative reasoning and greater adversarial influence.

Increase in Agreement with the Adversary (ΔAgreement): ΔAgreement is the second measure, which is used to measure how the collaborative agents gradually start adopting the answer offered by the adversarial agent. It is a measure of the change in the alignment of the agents between their starting independent responses and their ultimate positions upon the completion of the debate rounds. When the value of ΔAgreement is positive it means that the agents have been either convinced or deceived by the adversarial agent, and it indicates that the adversary has the ability to control the behavior of local agents. This measure therefore shows the effect of individual agents under adversarial arguments in the collaborative decision-making system.

Let:

- ${\varvec{A}\varvec{g}\varvec{r}\varvec{e}\varvec{e}}_{0}$ = number of the agents whose first response satisfies the adversarial response.
- ${\varvec{A}\varvec{g}\varvec{r}\varvec{e}\varvec{e}}_{\varvec{T}}$ = respondents who agree with the adversarial answer at the end of the last round T.

Then:

$$
\Delta Agreement = Agree~_{T} - Agree~_{0}
$$

(9)

A positive increase indicates: $\Delta Agreement > 0~$. This reflects successful persuasion, capturing the local behavioral influence of the adversarial agent.

Attack Success Criteria: An adversarial attack is considered successful when it simultaneously degrades system-level performance and increases alignment with the adversarial agent. Formally, we define.

- $\Delta Accuracy = A_{{adv}} - A_{{base}}$
- ${\Delta}\text{A}\text{g}\text{r}\text{e}\text{e}\text{m}\text{e}\text{n}\text{t}={Agree}_{T}-{Agree}_{0}$

Under this formulation:

- ΔAccuracy < 0 indicates system-level degradation,
- ΔAgreement > 0 indicates increased persuasion or alignment with the adversary.

Therefore, an attack is deemed successful when: ΔAccuracy < 0 and ΔAgreement > 0 This condition captures both structural corruption (reduced global performance) and behavioral manipulation (increased adversarial alignment), providing a comprehensive assessment of adversarial influence in multi-agent debate systems.

### Hyperparameters

The implementation of our multi-agent adversarial debate framework relies on a combination of robust deep-learning, data-processing, and API-driven tools. To load, tokenize and obtain text with open-weights LLMs, including as LLaMA [^35], Mistral [^36], Qwen [^37], and Yi [^38], we rely on the HuggingFace Transformers library [^39]. The execution and mixed-precision inference of PyTorch are supported, and can be used to efficiently run batches of decoding and load models based on the device they are being run on using device map= auto. For API-based models such as GPT-4o [^40] and GPT-3.5-Turbo [^41], we employ the OpenAI Chat Completions API to query cooperative, adversarial, and judge agents, with optional log-probability scoring for argument selection.

To ensure methodological transparency and reproducibility, we provide a detailed description of the Retrieval-Augmented Generation (RAG) pipeline used in our experiments:

- Retrieval Corpus: For each benchmark (MMLU, TruthfulQA, MedMCQA, SCALR), retrieval was performed over publicly available textual corpora aligned with the domain of the dataset. No proprietary or private data were used. All sources were publicly accessible and contained no personal or sensitive information.
- Embedding Model and Similarity Search: Dense retrieval was implemented using OpenAI embedding models (text-embedding-3-large).
- Both the user query and candidate passages were embedded into a shared semantic vector space. Similarity between the query and passages was computed using cosine similarity.
- Passages were ranked based on similarity score.
- Number of Retrieved Documents (k): For each query, the top-k = 5 passages were retrieved and concatenated to the model prompt. To assess robustness, we additionally evaluated:{k = 3, k = 10}.
- Preprocessing and Filtering: Retrieved passages underwent minimal mechanical preprocessing:
- Duplicate passages were removed.
- Passages exceeding 512 tokens were truncated.
- Passages with cosine similarity below τ = 0.30 were discarded.

Importantly, no filtering was performed based on semantic agreement, contradiction, or stance relative to the adversarial claim. Filtering was strictly similarity-based and independent of debate content. This design ensures that the observed amplification effects are not artifacts of selective evidence removal.

The methods used to process the data, sample it and manipulate the datasets are based on pandas, glob and datasets where the formatting follows a similar pattern among the MMLU, TruthfulQA, MedMCQA, SCALR and other benchmarks. All of the important configuration parameters that control the behavior of the LLM, decoding strategies, argument generation, and hardware use, are summarized in Table [1](https://www.nature.com/articles/s41598-026-42705-7#Tab1). The structural dynamics of the debate are determined by high level system variables (number of agents, adversaries, rounds, and argument candidates). The level of stochasticity and the level of evaluation of generated responses are controlled by low-level decoding hyperparameters such as temperature, ${top}_{p}$, ${max}_{new\_token}$, and $logprobs$. Parameters like $gpus$ and device map which are hardware related facilitate effective resource allocation.

**Table 1   LLM Inference and Decoding Hyperparameters.**

## Results

Figure [6](https://www.nature.com/articles/s41598-026-42705-7#Fig6) indicates clearly that multi-agent collaboration based on debate is structurally weak even in the case when a single adversarial agent is deployed in the system. In all four datasets, including TruthfulQA, MMLU, MedMCQA, and SCALR, the existence of a convincing opponent significantly reduces the accuracy of the group and a systematic drift of cooperative agents in the wrong direction. The performance at a system level is significantly reduced, and the accuracy goes down by 10 to 40% according to the underlying LLM. It is worth noting that GPT-4o is characterized by the most robustness since it remains relatively stable when exposed to adversarial pressure. Nevertheless, such a more resilient model still suffers a quantifiable performance impairment, which proves that resilience is not the same as immunity. GPT-3.5, Llama, Qwen and Yi models, in contrast, are much more vulnerable. In the case of these models, the adversarial agent is always doing well at controlling the debate, which results in big deviations with respect to the baseline. As an example, GPT-3.5 experiences a drop in accuracy up to 30% which is in agreement with the numerical values in Fig. [6](https://www.nature.com/articles/s41598-026-42705-7#Fig6). This instability indicates a natural inability of smaller or less aligned models to withstand strategies put forward by persuasive arguments of long form. The plots at the agent level also indicate that agreement rates with the adversarial agent have significantly grown often over 0.40. This shows that cooperative agents do not just fail to correct a wrongdoer but are actively drawn into its wrong story, demonstrating the dynamics of debates increasing the misinformation in the LLM ecosystems. LLM collaboration which is thought to enhance reasoning, is readily undermined by adversarial persuasion, even when a single agent amongst a number of agents acts maliciously. This reveals one of the core flaws of multi-agent debate protocols and highlights the strong necessity of new defense mechanisms, verification tools, and less risky coordination structures.

The trend of Majority Vote accuracy in the various rounds of the debate (Fig. [7](https://www.nature.com/articles/s41598-026-42705-7#Fig7)) indicates that the problem of adversarial persuasion is not a single effect but a gradual deterioration. In all four datasets, TruthfulQA, MMLU, MedMCQA and SCALR, the initial round is usually already in a fairly high position, particularly in the case of GPT-4o that has the highest accuracy at nearly any given situation. Nonetheless, accuracy levels off or decreases systematically as rounds go on, implying that the protocol of the debate, rather than reducing the errors of the first round, tends to multiply the role of the adversary. This is especially strong on GPT-3.5, Llama3-Inst-8B, Qwen1.5-Chat-14B and Yi1.5-Chat-9B whose curves have steep curves down by the third round on various datasets. As an illustration, on both TruthfulQA and MedMCQA, GPT-3.5 and Llama3-Inst-8B experience substantial declines in accuracy throughout the debate, which proves that these models are extremely vulnerable to adversarial steering during multi-round interaction. On more formalized tests, such as MMLU and SCALR, one would expect greater stability, however, in the presence of an adversary, most majority votes move further away than the correct response. On the whole, these curves indicate that the longer the debates become, the greater the chances that they will result in the convergence to the truth; it is rather possible that the opposing party will have additional possibilities to redefine the group opinion.

**Fig. 6**

![Fig. 6](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig6_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/6)

Performance debate-based multi-agent collaboration.

**Fig. 7**

![Fig. 7](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig7_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/7)

The trajectory of Majority Vote accuracy across debate rounds.

The adversary concordance of the debate rounds presented in Fig. [8](https://www.nature.com/articles/s41598-026-42705-7#Fig8) accounts for why accuracy deteriorates: since cooperative agents agree more and more with the adversarial agent. For the weaker or intermediate model (GPT-3.5, Llama3-Inst-8B, Qwen1.5-Chat-14B, Yi1.5-Chat-9B), adversarial consensus tends to significantly rise in Round 1-Round 3 with some as high as 0.6–0.7 on MedMCQA and TruthfulQA. This implies a positive majority of agents converge to the bad answer of the adversary over time in the course of a debate, indicating that the attack not only contributes noise, but captures the belief state of the whole group. GPT-4o once more emerges as relatively stronger, as its adversary agreement curves are lower and grow more slowly with respect to all the rounds, particularly on SCALR and MMLU where agreement with the adversary is not widely distributed. However, GPT-4o is also showing non-negligible agreement growth which means that no model is completely immune. Collectively, the majority-vote and agreement plots yield a coherent picture: if rounds increase, adversarial agreement is increasing and accuracy is decreasing, indicating a direct link between persuasive influence and system failure. This dynamic evidence helps to strengthen our primary assertion that debate-based LLM collaboration is inherently vulnerable to the adversarial attack driven by persuasion, and that multi-round interaction serves to amplify rather than to abate negative influence.

**Fig. 8**

![Fig. 8](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig8_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/8)

The adversary agreement over debate rounds.

Our aim is to comprehend the persuasiveness of the models. The results on the persuasive power of the evaluated models over the selected datasets are presented in Fig. [9](https://www.nature.com/articles/s41598-026-42705-7#Fig9). Statistically, there is a strong relationship between adversarial influence and system degradation in all models and datasets as shown in the plots. Models with highest increases for adversarial agreement, ΔAgr, show the largest decreases for accuracy, ΔAcc, indicating a positive relation between persuasion strength and performance failure. GPT-3.5 provides the most extreme outcome, where the ΔAgr increases from + 0.40 to + 0.68, while ΔAccuracy decreases to between − 20% and − 30%, indicating strong adversarial influence. Similarly, Llama and Yi models have high persuasion effects with a ΔAgr value of more than + 0.30 and accuracy loss of 10–25%. Qwen exhibits moderate susceptibility, with the shifts in persuasion ranging from + 0.20–0.30 and the reductions in accuracy of 9–23%. In contrast, GPT-4o demonstrates the most resilience: ΔAgr just stays at or near 0—or becomes negative—while ΔAcc remains small (often around ± 5%). On the whole, the trend observed among data sets indicates that larger accuracy deterioration can be predicted with greater adversarial agreement as evidence that multi-agent debates under persuading attack are systematically fragile.

The enhanced attack strategies seen in Fig. [10](https://www.nature.com/articles/s41598-026-42705-7#Fig10) —Best-of-N argument optimization and extra knowledge injection—clearly tell us that persuasion mechanisms can enhance or, in some cases, slightly hinder adversary effectiveness on TruthfulQA. In summary, GPT-4o and GPT-3.5 are both much higher than the original attack with a smaller but steady increase in ∆Accuracy and ∆Agreement suggesting that stronger argument choice and more evidence help the attacker build more cohesive and finely tuned persuasion. GPT-3.5 demonstrates an even larger improvement under the Best-of-N setting, reflecting its sensitivity to optimization in argument quality. However, the context-augmented version for GPT-3.5 performs slightly lower—an exception that might be due to two interacting reasons: (1) GPT-3.5 was already extremely aggressive when carrying out the baseline attack, leaving limited room for improvement, and (2) the model may be less capable of properly harnessing an extra understanding. In consequence it may at times water down its own narrative rather than strengthen it. Together, these observations reflect a general trend: better models will more naturally receive enhanced persuasion tools, while weak ones often provide inconsistent responses. In this way there lies an important asymmetry in how LLMs take up all external information during adversarial reasoning.

**Fig. 9**

![Fig. 9](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig9_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/9)

The persuasive power of the evaluated models over the selected datasets.

**Fig. 10**

![Fig. 10](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig10_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/10)

Best-of-N argument optimization.

Figures [11](https://www.nature.com/articles/s41598-026-42705-7#Fig11) and [12](https://www.nature.com/articles/s41598-026-42705-7#Fig12) of Majority Vote Accuracy and Adversary Agreement evolution during three debate rounds under attack and mitigation. True to our prediction, a good mitigation strategy should result in higher accuracy and less agreement with adversaries than the attack condition. As expected, this is also seen on slopes in the plots; for the majority of models, the mitigation curves exhibit an obviously enhanced shift in accuracy and decreasing adversary agreement curves signify diminished alignment with adversarial responses. Yet not all models show even this trend. Some of them show good improvement, others only show slight variation or fluctuating performance between rounds. The variability illustrates that a simple prompt-based mitigation method alone is not capable of reliably mitigating adversarial influence. Notwithstanding the presence of alert settings, some models seem vulnerable to adversarial signals and especially if interaction takes place over several rounds. So, we can say according to these findings that prompt-level defenses are not enough to build robust multi-agent reasoning in adversarial settings. However, more advanced defense mechanisms — perhaps architectural constraints, debate integrity checks, retrieval-augmented verification, or cross-agent consistency scoring — will be required to retain the robustness of the behavior when agents with diverse sources or types of entities interact and influence one another.

**Fig. 11**

![Fig. 11](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig11_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/11)

Adversary agreement.

### Ablation studies

To verify that adversarial amplification was not induced by retrieval filtering, we conducted additional ablation experiments (Removing the similarity threshold (no filtering), Increasing retrieval size (k = 10), and Reducing retrieval size (k = 3)). Across all configurations, persuasion-induced accuracy degradation remained statistically significant (average ΔAccuracy between − 18% and − 24%, depending on dataset), indicating that RAG amplification arises from credibility reinforcement rather than preprocessing bias (see Table [2](https://www.nature.com/articles/s41598-026-42705-7#Tab2)).

**Fig. 12**

![Fig. 12](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig13_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/12)

Majority vote accuracy.

**Table 2   Robustness to retrieval configuration (Mean ± Std Across Runs).**

To evaluate the robustness of the collaborative debate under different configurations, we study how performance changes when we vary the number of rounds and the number of agents in the debate. Intuitively, one might expect that adding more turns of interaction or more agents should make the system more robust to adversarial influence. However, the empirical results suggest that this intuition does not always hold.

- Increasing the Number of Rounds: The Majority Vote Accuracy is presented in Fig. [13](https://www.nature.com/articles/s41598-026-42705-7#Fig13) for a fixed group of three agents (*N*  = 3), going from T = 1 to T = 9 for each round in TruthfulQA, MMLU, and GSM8K. In the no-attack condition, the majority vote remains relatively stable across rounds, with accuracies hovering around 0.55–0.60 and showing only a slight upward trend. Conversely, in the adversarial attack, the majority vote accuracy rapidly declines in the first few rounds, falling from ~ 0.5 at T = 1 to below 0.2 by T = 3, and then gradually decays towards ≈ 0.1 as the debate is progressing. This trend is the same for all three datasets. Once the group is pulled to the wrong answer by the adversary, further rounds do not assist the agents in “recovering,” but rather make it so that the wrong consensus becomes entrenched. Therefore, simply increasing the number of debate rounds is not an effective defense against a persuasive adversary.
- Increasing the Number of Agents: We then assess the robustness as a function of the number of collaborating agents used. The Majority Vote Accuracy for a fixed number of rounds (T = 3) is shown in Fig. [14](https://www.nature.com/articles/s41598-026-42705-7#Fig14), varying the number of agents participating in the debate (*N*  = 2, …, 6) on TruthfulQA. As anticipated, when *N*  = 2 (one adversary and one non-adversarial agent), the accuracy of the system approaches zero, as the adversarial answer takes over the vote. With an increase in N, the initial accuracy of majority votes during no-attack becomes better and even under attack larger groups begin with higher accuracy in the first round. But even the performance across rounds continues to exhibit a similar declining trend: the adversary eventually uses increased number of agents to persuade the group to give the incorrect answer. So adding more collaborating models results in better baseline performance, but does not fundamentally eliminate the adversary’s influence; the debate still remains vulnerable even for much larger collectives.

**Fig. 13**

![Fig. 13](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig15_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/13)

The robustness of the collaborative debate under different configurations: Increasing the Number of Rounds.

To assess whether the observed performance degradation is attributable to persuasion rather than unequal agent capabilities, we introduce an additional adversarial baseline with reduced reasoning capacity. In this baseline, the adversarial agent is restricted to producing a single incorrect answer per round without multi-layer argument generation, counterargument construction, fusion, or persuasive polishing. All agents (including the adversary) use the same underlying LLM, and differ only in the prompting and generation strategy. This comparison allows us to isolate the contribution of enhanced persuasive mechanisms and assess the fairness of the evaluation. Figure [15](https://www.nature.com/articles/s41598-026-42705-7#Fig15). Comparison of system-level accuracy and adversarial agreement under a vanilla adversarial baseline [^43] and the full persuasion-driven adversary. The vanilla adversary produces limited impact, while the full adversary consistently induces larger accuracy degradation and higher agreement, indicating that structured persuasive mechanisms (not unequal model capacity) drive the observed effects. Results show that while a vanilla adversarial agent can occasionally influence individual agents, its impact on system-level accuracy and agreement remains limited. In contrast, the full persuasion-driven adversary consistently induces significantly larger drops in accuracy and higher agreement with incorrect answers, confirming that the observed effects arise from structured persuasive mechanisms rather than from mere adversarial intent or unequal model capacity.

**Fig. 14**

![Fig. 14](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig16_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/14)

The robustness of the collaborative debate under different configurations: Increasing the Number of Agents.

**Fig. 15**

![Fig. 15](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41598-026-42705-7/MediaObjects/41598_2026_42705_Fig17_HTML.png?as=webp)

[Full size image](https://www.nature.com/articles/s41598-026-42705-7/figures/15)

Ablation study of adversarial reasoning components.

### Limitations

Despite the strengths of the empirical findings, several limitations must be noted in interpreting the results of this study. First, the experiments are computationally resource intensive (multi-round simulations across multiple agents and multiple datasets). This constraint reduces the maximum number of repetitions, model variants, and hyper parameter sweep scales to manageable levels. Larger systematic studies—particularly those involving dozens of agents or higher-capacity models—will also remain outside the current work’s computational resources. So, while the patterns observed here are robust and stable, they are just one part of the general landscape of multi-agent adversarial interaction design. Second, the open-source frameworks we present are normally bounded to between 8B–14B parameters, which are much smaller than the front-of-the-pack, high-stakes proprietary models commonly deployed in high-stakes contexts. While these models closely follow popular research-grade LLMs, the behavior they generate may not entirely reflect the complexity or capabilities and defenses of larger systems (e.g., GPT-4-class or 70B+ architectures). As a result, it is possible that larger or more highly optimized models [^44] will show disparate rates of susceptibility or vulnerability to persuasion-based adversarial attacks. Third, the debate protocol utilized in this study is intentionally designed to provide controlled insight into the LLM-to-LLM persuasion dynamics. But this controlled setup is an academic artifact rather than a real-world deployment environment [^45]. Thus, real systems might enforce additional safeguards, task-specific constraints or user-directed oversight that influence how agents interact; also how information is passed from one agent to another. Similarly, real-world LLM agents can function under asynchronous [^46], multi-modal, or tool-augmented conditions that differ fundamentally from the turn-based text-only protocol investigated here. Last but not least, although the results uniformly demonstrate that persuasive adversaries can interfere with collaborative reasoning processes, the nature of degradation may vary significantly across tasks, model families, or deployment contexts. However, this vulnerability is concerning in spite of the fact that the cause—persuasion-induced reasoning drift—can still occur in less complex, more limited settings. This appears to indicate that the menace is built into the structure rather than the effect of it being present in a random manner [^47] and it points to the necessity of dedicated defense strategies for multi-agent LLM systems that are increasingly integrated in autonomous, interconnected roles due to the impact of manipulation.

The present framework also assumes that cooperative agents consume the outputs of all other agents uniformly, without applying explicit weighting, trust calibration, or source-aware filtering during debate rounds. This simplifying assumption was adopted to isolate and analyze the intrinsic vulnerability of debate-based multi-agent reasoning to persuasive adversarial influence under a controlled and transparent setting. In contrast, real-world multi-agent systems may incorporate heterogeneous trust assignments, historical reliability estimates, or source-aware weighting mechanisms that modulate how much influence different agents exert on collective decision-making. While such mechanisms may mitigate certain forms of adversarial impact, they also introduce additional design complexity and potential attack surfaces. Evaluating how persuasion-driven adversaries interact with weighted or source-aware aggregation strategies remains an important direction for future work and is necessary to fully assess the generalizability of the observed vulnerabilities.

A further limitation of the present study is that the evaluated mitigation strategy is restricted to prompt-level warnings and behavioral instructions provided to cooperative agents. While such interventions can reduce adversarial influence in some cases, our empirical results demonstrate that they do not offer reliable protection against persuasion-driven attacks, particularly over multiple debate rounds. More robust defenses are likely to require structural safeguards that operate beyond prompt conditioning. Promising directions for future work include cross-agent consistency checks that detect anomalous opinion shifts, agreement trajectories, or argument incoherence across agents; debate integrity mechanisms that constrain disproportionate influence by a single agent; and verification-based modules that assess claim consistency against external or internal references before consensus formation. Investigating such architectural and protocol-level defenses remains an important avenue for strengthening multi-agent LLM robustness.

## Conclusion

This work shows that multi-agent debate — commonly considered a powerful way of improving LLM reasoning — has a fundamental vulnerability, namely that it can be disrupted by a single persuasive adversarial agent. By employing a systematic approach across diverse tasks, we demonstrate that a highly misleading agent can significantly degrade collective accuracy. It also successfully induces other models to adopt incorrect answers, and even overrides majority vote mechanisms designed for group decisions. This finding indicates that persuasiveness, while traditionally regarded as a good ability for explaining and reasoning on its own, becomes a safety-critical factor when agents interact autonomously. This new threat is particularly pronounced with the advent of advanced adversarial techniques such as multi-layered argument optimization and retrieval-augmented persuasion. Our findings highlight the urgent need for more robust collaboration protocols, adversarial-resistant debate frameworks, and principled guardrails governing LLM-to-LLM communication. With the growing deployment of LLM agents in coordinated and autonomous environments, designing techniques to mitigate persuasive manipulation will be increasingly relevant to ensuring the reliability and safety of multi-agent AI systems [^48]. Also, future research should therefore prioritize structural and protocol-level defenses—such as cross-agent consistency analysis and verification-aware debate mechanisms—over purely prompt-based mitigation strategies.

## Data availability

The datasets analysed during the current study are:• MMLU (Massive Multitask Language Understanding) available in [https://github.com/hendrycks/test](https://github.com/hendrycks/test).• TruthfulQA available in [https://github.com/sylinrl/TruthfulQA](https://github.com/sylinrl/TruthfulQA).• MedMCQA available in [https://github.com/medmcqa/medmcqa](https://github.com/medmcqa/medmcqa).• SCALR (Statutory Case Law Reasoning, Legal Bench) available in [https://github.com/HazyResearch/legalbench](https://github.com/HazyResearch/legalbench). The datasets used in this study do not involve human subjects, personal data, or newly collected human responses. All datasets are pre-existing, publicly released benchmark datasets consisting of anonymized multiple-choice questions, answers, and metadata for evaluating language models.To ensure full reproducibility, the complete experimental framework — including multi-agent debate implementation, adversarial persuasion modules, prompt templates, evaluation scripts, configuration files, and representative stored debate transcripts — is publicly available at: [https://github.com/insafkraidia/Multi-Agent-Large-Language-Model-Debate-MA-LLMD-](https://github.com/insafkraidia/Multi-Agent-Large-Language-Model-Debate-MA-LLMD-) Representative multi-round debate transcripts (JSONL format) used to compute accuracy, agreement, and persuasion metrics are included in the repository. Additional artifacts can be provided upon reasonable request.

## References

## Acknowledgements

This work was supported by the Princess Nourah Bint Abdulrahman University Researchers Supporting Project number PNURSP2026R733.

## Ethics declarations

### Competing interests

The authors declare no competing interests.

## Additional information

### Publisher’s note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Rights and permissions

**Open Access** This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by-nc-nd/4.0/](http://creativecommons.org/licenses/by-nc-nd/4.0/).

[^1]: Belhaouari, S. B. & Kraidia, I. Efficient self-attention with smart pruning for sustainable large language models. *Sci. Rep.* **15** (1), 10171 (2025).

[Article](https://doi.org/10.1038%2Fs41598-025-92586-5) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2025NatSR..1510171B) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB2MXptVegtLs%3D) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=40128247) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC11933332) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Efficient%20self-attention%20with%20smart%20pruning%20for%20sustainable%20large%20language%20models&journal=Sci.%20Rep.&doi=10.1038%2Fs41598-025-92586-5&volume=15&issue=1&publication_year=2025&author=Belhaouari%2CSB&author=Kraidia%2CI)

[^2]: Du, Y., Li, S., Torralba, A., Tenenbaum, J. B. & Mordatch, I. Improving factuality and reasoning in language models through multiagent debate. *arXivm* 2023 [https://doi.org/10.48550/arXiv.2305.14325](https://doi.org/10.48550/arXiv.2305.14325)

[Article](https://doi.org/10.48550%2FarXiv.2305.14325) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Improving%20Factuality%20and%20Reasoning%20in%20Language%20Models%20through%20Multiagent%20Debate&journal=arXivm&doi=10.48550%2FarXiv.2305.14325&publication_year=2023&author=Du%2CY.&author=Li%2CS.&author=Torralba%2CA.&author=Tenenbaum%2CJ.%20B.&author=Mordatch%2CI.)

[^3]: Aher, G., Arriaga, R. I. & Kalai, A. T. Using large language models to simulate multiple humans and replicate human subject studies. *arXiv* (2023). [https://doi.org/10.48550/arXiv.2208.10264](https://doi.org/10.48550/arXiv.2208.10264)

[Article](https://doi.org/10.48550%2FarXiv.2208.10264) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Using%20Large%20Language%20Models%20to%20Simulate%20Multiple%20Humans%20and%20Replicate%20Human%20Subject%20Studies&journal=arXiv&doi=10.48550%2FarXiv.2208.10264&publication_year=2023&author=Aher%2CG.&author=Arriaga%2CR.%20I.&author=Kalai%2CA.%20T.)

[^4]: Breum, S. M., Egdal, D. V., Mortensen, V. G., Møller, A. G. & Aiello, L. M. The persuasive power of large language models. *arXiv* (2023). [https://doi.org/10.48550/arXiv.2312.15523](https://doi.org/10.48550/arXiv.2312.15523)

[Article](https://doi.org/10.48550%2FarXiv.2312.15523) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20Persuasive%20Power%20of%20Large%20Language%20Models&journal=arXiv&doi=10.48550%2FarXiv.2312.15523&publication_year=2023&author=Breum%2CS.%20M.&author=Egdal%2CD.%20V.&author=Mortensen%2CV.%20G.&author=M%C3%B8ller%2CA.%20G.&author=Aiello%2CL.%20M.)

[^5]: Bai, Y. et al. Constitutional AI: Harmlessness from AI Feedback. arXiv. (2022). [https://doi.org/10.48550/arXiv.2212.08073](https://doi.org/10.48550/arXiv.2212.08073)

[Article](https://doi.org/10.48550%2FarXiv.2212.08073) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Constitutional%20AI%3A%20Harmlessness%20from%20AI%20Feedback.%20arXiv&journal=arXiv&doi=10.48550%2FarXiv.2212.08073&publication_year=2022&author=Bai%2CY.)

[^6]: Kraidia, I., Ghenai, A. & Belhaouari, S. B. Defense against adversarial attacks: robust and efficient compressed optimized neural networks. *Sci. Rep.* **14** (1), 6420 (2024).

[Article](https://doi.org/10.1038%2Fs41598-024-56259-z) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2024NatSR..14.6420K) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB2cXotFajsrw%3D) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=38494519) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC10944840) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Defense%20against%20adversarial%20attacks%3A%20robust%20and%20efficient%20compressed%20optimized%20neural%20networks&journal=Sci.%20Rep.&doi=10.1038%2Fs41598-024-56259-z&volume=14&issue=1&publication_year=2024&author=Kraidia%2CI&author=Ghenai%2CA&author=Belhaouari%2CSB)

[^7]: Wei, J. et al. Chain-of-thought prompting elicits reasoning in large language models. *arXiv* (2023). [https://doi.org/10.48550/arXiv.2201.11903](https://doi.org/10.48550/arXiv.2201.11903)

[Article](https://doi.org/10.48550%2FarXiv.2201.11903) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=37961744) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC10635285) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Chain-of-Thought%20Prompting%20Elicits%20Reasoning%20in%20Large%20Language%20Models&journal=arXiv&doi=10.48550%2FarXiv.2201.11903&publication_year=2023&author=Wei%2CJ.)

[^8]: Lin, S., Hilton, J. & Evans, O. TruthfulQA: measuring how models mimic human falsehoods. *arXiv* (2022). [https://doi.org/10.48550/arXiv.2109.07958](https://doi.org/10.48550/arXiv.2109.07958)

[Article](https://doi.org/10.48550%2FarXiv.2109.07958) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=TruthfulQA%3A%20Measuring%20How%20Models%20Mimic%20Human%20Falsehoods&journal=arXiv&doi=10.48550%2FarXiv.2109.07958&publication_year=2022&author=Lin%2CS.&author=Hilton%2CJ.&author=Evans%2CO.)

[^9]: Zheng, Q. et al. CodeGeeX: A pre-trained model for code generation with multilingual benchmarking on humanEval-X. *arXiv* (2024). [https://doi.org/10.48550/arXiv.2303.17568](https://doi.org/10.48550/arXiv.2303.17568)

[Article](https://doi.org/10.48550%2FarXiv.2303.17568) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=41031081) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC12478420) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=CodeGeeX%3A%20A%20Pre-Trained%20Model%20for%20Code%20Generation%20with%20Multilingual%20Benchmarking%20on%20HumanEval-X&journal=arXiv&doi=10.48550%2FarXiv.2303.17568&publication_year=2024&author=Zheng%2CQ.)

[^10]: Yang, Y. M., Chang, K. C. & Luo, J. N. Hybrid Neural Network-Based Intrusion Detection System: Leveraging LightGBM and MobileNetV2 for IoT Security. *Symmetry* **17** (3), 314 (2025).

[Article](https://doi.org/10.3390%2Fsym17030314) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2025Symm...17..314Y) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Hybrid%20Neural%20Network-Based%20Intrusion%20Detection%20System%3A%20Leveraging%20LightGBM%20and%20MobileNetV2%20for%20IoT%20Security&journal=Symmetry&doi=10.3390%2Fsym17030314&volume=17&issue=3&publication_year=2025&author=Yang%2CYM&author=Chang%2CKC&author=Luo%2CJN)

[^11]: Hiari, M., Alraba’nah, Y. & Qaddara, I. Learning-Based Intrusion Detection System using Refined LSTM for DoS Attack Detection. *Eng. Technol. Appl. Sci. Res.* **15** (4), 25627–25633 (2025).

[Article](https://doi.org/10.48084%2Fetasr.11499) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Learning-Based%20Intrusion%20Detection%20System%20using%20Refined%20LSTM%20for%20DoS%20Attack%20Detection&journal=Eng.%20Technol.%20Appl.%20Sci.%20Res.&doi=10.48084%2Fetasr.11499&volume=15&issue=4&pages=25627-25633&publication_year=2025&author=Hiari%2CM&author=Alraba%E2%80%99nah%2CY&author=Qaddara%2CI)

[^12]: Abualhaj, M. M., Al-Khatib, S. N., Al Zyoud, M., Qaddara, I. & Anbar, M. Enhancing intrusion detection system performance using a hybrid of Harris Hawks and Whale Optimization Algorithms. *Eng. Technol. Appl. Sci. Res.* **15** (4), 24354–24361 (2025).

[Article](https://doi.org/10.48084%2Fetasr.10919) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Enhancing%20intrusion%20detection%20system%20performance%20using%20a%20hybrid%20of%20Harris%20Hawks%20and%20Whale%20Optimization%20Algorithms&journal=Eng.%20Technol.%20Appl.%20Sci.%20Res.&doi=10.48084%2Fetasr.10919&volume=15&issue=4&pages=24354-24361&publication_year=2025&author=Abualhaj%2CMM&author=Al-Khatib%2CSN&author=Al%20Zyoud%2CM&author=Qaddara%2CI&author=Anbar%2CM)

[^13]: Liang, T. et al. Encouraging divergent thinking in large language models through multi-agent debate. *arXiv* (2024). [https://doi.org/10.48550/arXiv.2305.19118](https://doi.org/10.48550/arXiv.2305.19118)

[Article](https://doi.org/10.48550%2FarXiv.2305.19118) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=39483342) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC11527098) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Encouraging%20Divergent%20Thinking%20in%20Large%20Language%20Models%20through%20Multi-Agent%20Debate&journal=arXiv&doi=10.48550%2FarXiv.2305.19118&publication_year=2024&author=Liang%2CT.)

[^14]: Chan, C. M. et al. ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate. arXiv (2023). [https://doi.org/10.48550/arXiv.2308.07201](https://doi.org/10.48550/arXiv.2308.07201)

[Article](https://doi.org/10.48550%2FarXiv.2308.07201) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=37461418) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC10350101) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=ChatEval%3A%20Towards%20Better%20LLM-based%20Evaluators%20through%20Multi-Agent%20Debate&journal=arXiv&doi=10.48550%2FarXiv.2308.07201&publication_year=2023&author=Chan%2CC.%20M.)

[^15]: Wu, Q. et al. AutoGen: enabling next-gen LLM applications via multi-agent conversation. *arXiv* (2023). [https://doi.org/10.48550/arXiv.2308.08155](https://doi.org/10.48550/arXiv.2308.08155)

[Article](https://doi.org/10.48550%2FarXiv.2308.08155) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=38196746) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC10775347) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=AutoGen%3A%20Enabling%20Next-Gen%20LLM%20Applications%20via%20Multi-Agent%20Conversation&journal=arXiv&doi=10.48550%2FarXiv.2308.08155&publication_year=2023&author=Wu%2CQ.)

[^16]: Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D. & Ghanem, B. CAMEL: communicative agents for ‘mind’ exploration of large language model society. *arXiv* (2023). [https://doi.org/10.48550/arXiv.2303.17760](https://doi.org/10.48550/arXiv.2303.17760)

[Article](https://doi.org/10.48550%2FarXiv.2303.17760) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=38196748) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC12478431) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=CAMEL%3A%20communicative%20agents%20for%20%E2%80%98mind%E2%80%99%20exploration%20of%20large%20language%20model%20society&journal=arXiv&doi=10.48550%2FarXiv.2303.17760&publication_year=2023&author=Li%2CG.&author=Hammoud%2CH.%20A.%20A.%20K.&author=Itani%2CH.&author=Khizbullin%2CD.&author=Ghanem%2CB.)

[^17]: Chen, W. et al. AgentVerse: facilitating multi-agent collaboration and exploring emergent behaviors. *arXiv* (2023). [https://doi.org/10.48550/arXiv.2308.10848](https://doi.org/10.48550/arXiv.2308.10848)

[Article](https://doi.org/10.48550%2FarXiv.2308.10848) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=38196746) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC12478431) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=AgentVerse%3A%20Facilitating%20Multi-Agent%20Collaboration%20and%20Exploring%20Emergent%20Behaviors&journal=arXiv&doi=10.48550%2FarXiv.2308.10848&publication_year=2023&author=Chen%2CW.)

[^18]: Hong, S. et al. MetaGPT: Meta programming for a multi-agent collaborative framework. *arXiv* (2024). [https://doi.org/10.48550/arXiv.2308.00352](https://doi.org/10.48550/arXiv.2308.00352)

[Article](https://doi.org/10.48550%2FarXiv.2308.00352) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=39253641) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC11383445) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=MetaGPT%3A%20Meta%20Programming%20for%20A%20Multi-Agent%20Collaborative%20Framework&journal=arXiv&doi=10.48550%2FarXiv.2308.00352&publication_year=2024&author=Hong%2CS.)

[^19]: Talebirad, Y. & Nadiri, A. Multi-agent collaboration: harnessing the power of intelligent LLM agents. *arXiv* (2023). [https://doi.org/10.48550/arXiv.2306.03314](https://doi.org/10.48550/arXiv.2306.03314)

[Article](https://doi.org/10.48550%2FarXiv.2306.03314) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Multi-Agent%20Collaboration%3A%20Harnessing%20the%20Power%20of%20Intelligent%20LLM%20Agents&journal=arXiv&doi=10.48550%2FarXiv.2306.03314&publication_year=2023&author=Talebirad%2CY.&author=Nadiri%2CA.)

[^20]: Salvi, F., Ribeiro, M. H., Gallotti, R. & West, R. On the conversational persuasiveness of large language models: a randomized controlled trial. *Nat. Hum. Behav.* **9** (8), 1645–1653. [https://doi.org/10.1038/s41562-025-02194-6](https://doi.org/10.1038/s41562-025-02194-6)

[Article](https://doi.org/10.1038%2Fs41562-025-02194-6) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=40389594) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC12367540) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=On%20the%20Conversational%20Persuasiveness%20of%20Large%20Language%20Models%3A%20A%20Randomized%20Controlled%20Trial&journal=Nat.%20Hum.%20Behav.&doi=10.1038%2Fs41562-025-02194-6&volume=9&issue=8&pages=1645-1653&publication_year=2025&author=Salvi%2CF.&author=Ribeiro%2CM.%20H.&author=Gallotti%2CR.&author=West%2CR.)

[^21]: Wan, A., Wallace, E. & Klein, D. What evidence do language models find convincing? *arXiv* (2024). [https://doi.org/10.48550/arXiv.2402.11782](https://doi.org/10.48550/arXiv.2402.11782)

[Article](https://doi.org/10.48550%2FarXiv.2402.11782) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=41031082) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC12478424) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=What%20evidence%20do%20language%20models%20find%20convincing%3F&journal=arXiv&doi=10.48550%2FarXiv.2402.11782&publication_year=2024&author=Wan%2CA.&author=Wallace%2CE.&author=Klein%2CD.)

[^22]: Rescala, P., Ribeiro, M. H., Hu, T. & West, R. Can language models recognize convincing arguments? *arXiv* (2024). [https://doi.org/10.48550/arXiv.2404.00750](https://doi.org/10.48550/arXiv.2404.00750)

[Article](https://doi.org/10.48550%2FarXiv.2404.00750) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Can%20Language%20Models%20Recognize%20Convincing%20Arguments%3F&journal=arXiv&doi=10.48550%2FarXiv.2404.00750&publication_year=2024&author=Rescala%2CP.&author=Ribeiro%2CM.%20H.&author=Hu%2CT.&author=West%2CR.)

[^23]: Khan, A. et al. Debating with more persuasive LLMs leads to more truthful answers. *arXiv* (2024). [https://doi.org/10.48550/arXiv.2402.06782](https://doi.org/10.48550/arXiv.2402.06782)

[Article](https://doi.org/10.48550%2FarXiv.2402.06782) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=39764409) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC11703318) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Debating%20with%20more%20persuasive%20LLMs%20leads%20to%20more%20truthful%20answers&journal=arXiv&doi=10.48550%2FarXiv.2402.06782&publication_year=2024&author=Khan%2CA.)

[^24]: Kraidia, I., Ghenai, A. & Belhaouari, S. B. A multi-faceted approach to trending topic attack detection using semantic similarity and large-scale datasets, *IEEE Access*, Accessed: Dec. 29, 2025. \[Online\]. (2025). Available: [https://ieeexplore.ieee.org/abstract/document/10857330/](https://ieeexplore.ieee.org/abstract/document/10857330/)

[^25]: Abualhaj, M. M., Abu-Shareha, A. A., Alkhatib, N., Shambour, S., Alsaaidah, A. M. & Q. Y. & Detecting spam using Harris Hawks optimizer as a feature selection algorithm. *Bull. Electr. Eng. Inf.* **14** (3), 2361–2369. (2025). [https://doi.org/10.11591/eei.v14i3.9198](https://doi.org/10.11591/eei.v14i3.9198)

[Article](https://doi.org/10.11591%2Feei.v14i3.9198) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Detecting%20spam%20using%20Harris%20Hawks%20optimizer%20as%20a%20feature%20selection%20algorithm&journal=Bull.%20Electr.%20Eng.%20Inf.&doi=10.11591%2Feei.v14i3.9198&volume=14&issue=3&pages=2361-2369&publication_year=2025&author=Abualhaj%2CM.%20M.&author=Abu-Shareha%2CA.%20A.&author=Alkhatib%2CN.&author=Shambour%2CS.&author=Alsaaidah%2CA.%20M.)

[^26]: Kraidia, I., Qaddara, I. & Alraba’nah, Y. DynaMI: Dynamic Membership Inference via Adaptive Manifold Perturbations. *IEEE Access.* 1–1. [https://doi.org/10.1109/ACCESS.2026.3665297](https://doi.org/10.1109/ACCESS.2026.3665297) (2026).

[^27]: Kraidia, I., Ghenai, A. & Zeghib, N. HST-Detector: A Multimodal Deep Learning System for Twitter Spam Detection, in Computational Intelligence, Data Analytics and Applications, (eds García Márquez, F. P., Jamil, A., Eken, S. & Hameed, A. A.) in Lecture Notes in Networks and Systems. 643, 91–103. doi: [https://doi.org/10.1007/978-3-031-27099-4\_8](https://doi.org/10.1007/978-3-031-27099-4_8). (Springer International Publishing, 2023).

[^28]: Kraidia, I., Ghenai, A. & Zeghib, N. A Multimodal Spam Filtering System for Multimedia Messaging Service, In: *International Conference on Artificial Intelligence Science and Applications (CAISA)*, vol. 1441, M. Abd Elaziz, M. Medhat Gaber, S. El-Sappagh, M. A. A. Al-qaness, and A. A. Ewees, Eds., in Advances in Intelligent Systems and Computing, 1441 121–131.( Springer Nature Switzerland, 2023). [https://doi.org/10.1007/978-3-031-28106-8\_9](https://doi.org/10.1007/978-3-031-28106-8_9)

[^29]: Qaddara, I., Alraba’nah, Y. & Hiari, M. O. Evaluation of SQL and NoSQL Databases on Parallel Processing. *Eng. Technol. Appl. Sci. Res.* **15** (4), 24298–24304 (2025).

[Article](https://doi.org/10.48084%2Fetasr.10620) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Evaluation%20of%20SQL%20and%20NoSQL%20Databases%20on%20Parallel%20Processing&journal=Eng.%20Technol.%20Appl.%20Sci.%20Res.&doi=10.48084%2Fetasr.10620&volume=15&issue=4&pages=24298-24304&publication_year=2025&author=Qaddara%2CI&author=Alraba%E2%80%99nah%2CY&author=Hiari%2CMO)

[^30]: Qaddara, I. & Applying machine learning techniques on cyber security datasets: detecting cyber attacks. *Harbin Gongye Daxue XuebaoJournal Harbin Inst. Technol.*, **54**, 7, 95–110, (2022).

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=&journal=Harbin%20Gongye%20Daxue%20XuebaoJournal%20Harbin%20Inst.%20Technol.&volume=54&issue=7&pages=95-110&publication_year=2022&author=Qaddara%2CI)

[^31]: Qaddara, I. *12th International Conference on Information* Technology *(ICIT)*, IEEE, 2025, pp. 571–576. Accessed: Dec. 29, 2025. \[Online\]. (2025). Available: [https://ieeexplore.ieee.org/abstract/document/11049137/](https://ieeexplore.ieee.org/abstract/document/11049137/)

[^32]: Hendrycks, D. et al. Measuring massive multitask language understanding. *arXiv* (2021). [https://doi.org/10.48550/arXiv.2009.03300](https://doi.org/10.48550/arXiv.2009.03300)

[Article](https://doi.org/10.48550%2FarXiv.2009.03300) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Measuring%20Massive%20Multitask%20Language%20Understanding&journal=arXiv&doi=10.48550%2FarXiv.2009.03300&publication_year=2021&author=Hendrycks%2CD.)

[^33]: Pal, A., Umapathi, L. K. & Sankarasubbu, M. MedMCQA: A Large-scale Multi-Subject Multi-Choice Dataset for Medical domain Question Answering, arXiv.org. Accessed: Dec. 18, 2025. \[Online\]. Available: [https://arxiv.org/abs/2203.14371v1](https://arxiv.org/abs/2203.14371v1)

[^34]: Guha, N. et al. LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models, arXiv.org. Accessed: Dec. 18, 2025. \[Online\]. Available: [https://arxiv.org/abs/2308.11462v1](https://arxiv.org/abs/2308.11462v1)

[^35]: Touvron, H. et al. LLaMA: Open and efficient foundation language models. arXiv. (2023). [https://doi.org/10.48550/arXiv.2302.13971](https://doi.org/10.48550/arXiv.2302.13971)

[Article](https://doi.org/10.48550%2FarXiv.2302.13971) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=LLaMA%3A%20Open%20and%20efficient%20foundation%20language%20models.&journal=arXiv&doi=10.48550%2FarXiv.2302.13971&publication_year=2023&author=Touvron%2CH.)

[^36]: \[2310. 06825\] Mistral 7B. Accessed: Dec. 18, 2025. \[Online\]. Available: [https://arxiv.org/abs/2310.06825](https://arxiv.org/abs/2310.06825)

[^37]: Yang, A. et al. Qwen3 Technical Report, arXiv.org. Accessed: Dec. 18, 2025. \[Online\]. Available: [https://arxiv.org/abs/2505.09388v1](https://arxiv.org/abs/2505.09388v1)

[^38]: Ilharco, G. et al. Jul. 28,., *OpenCLIP*. Zenodo. (2021). [https://doi.org/10.5281/ZENODO.5143773](https://doi.org/10.5281/ZENODO.5143773)

[^39]: Vaswani, A. et al. *Atten. Is All You Need arXiv* (2024). [https://doi.org/10.48550/arXiv.1706.03762](https://doi.org/10.48550/arXiv.1706.03762)

[Article](https://doi.org/10.48550%2FarXiv.1706.03762) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Atten.%20Is%20All%20You%20Need&journal=arXiv&doi=10.48550%2FarXiv.1706.03762&publication_year=2024&author=Vaswani%2CA.)

[^40]: OpenAI et al. GPT-4 technical report. *arXiv* (2024). [https://doi.org/10.48550/arXiv.2303.08774](https://doi.org/10.48550/arXiv.2303.08774)

[Article](https://doi.org/10.48550%2FarXiv.2303.08774) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=GPT-4%20Technical%20Report&journal=arXiv&doi=10.48550%2FarXiv.2303.08774&publication_year=2024&author=OpenAI%2C)

[^41]: Brown, T. B. et al. Language models are few-shot learners. *arXiv* (2020). [https://doi.org/10.48550/arXiv.2005.14165](https://doi.org/10.48550/arXiv.2005.14165)

[Article](https://doi.org/10.48550%2FarXiv.2005.14165) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Language%20models%20are%20few-shot%20learners&journal=arXiv&doi=10.48550%2FarXiv.2005.14165&publication_year=2020&author=Brown%2CT.%20B.)

[^42]: Abualhaj, M. M. et al. Enhanced network communication security through hybrid dragonfly-bat feature selection for intrusion detection. *J. Commun.* (2025). [https://doi.org/10.12720/jcm.20.5.607-618](https://doi.org/10.12720/jcm.20.5.607-618)

[Article](https://doi.org/10.12720%2Fjcm.20.5.607-618) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Enhanced%20Network%20Communication%20Security%20Through%20Hybrid%20Dragonfly-Bat%20Feature%20Selection%20for%20Intrusion%20Detection&journal=J.%20Commun.&doi=10.12720%2Fjcm.20.5.607-618&publication_year=2025&author=Abualhaj%2CM.%20M.)

[^43]: Goodfellow, I. J., Shlens, J. & Szegedy, C. Explaining and harnessing adversarial examples. *arXiv* (2015). [https://doi.org/10.48550/arXiv.1412.6572](https://doi.org/10.48550/arXiv.1412.6572)

[Article](https://doi.org/10.48550%2FarXiv.1412.6572) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Explaining%20and%20Harnessing%20Adversarial%20Examples&journal=arXiv&doi=10.48550%2FarXiv.1412.6572&publication_year=2015&author=Goodfellow%2CI.%20J.&author=Shlens%2CJ.&author=Szegedy%2CC.)

[^44]: Abualhaj, M. M., Al-Khatib, S., Al Shafi, N., Qaddara, I. & Hyassat, A. Utilizing gray wolf optimization algorithm in malware forensic investigation, *J. Comput. Cogn. Eng.*, Accessed: Dec. 29, 2025. \[Online\]. (2025). Available: [https://scholar.google.com/scholar?cluster=5089858435436670152&hl=en&oi=scholarr](https://scholar.google.com/scholar?cluster=5089858435436670152%26hl=en%26oi=scholarr)

[^45]: Qaddara, I. & Alraba’nah, Y. Enhancing requirements classification using machine learning techniques. *SN Comput. Sci.* **6** (6), 649. [https://doi.org/10.1007/s42979-025-04158-z](https://doi.org/10.1007/s42979-025-04158-z)

[Article](https://link.springer.com/doi/10.1007/s42979-025-04158-z) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Enhancing%20requirements%20classification%20using%20machine%20learning%20techniques&journal=SN%20Comput.%20Sci.&doi=10.1007%2Fs42979-025-04158-z&volume=6&issue=6&publication_year=2025&author=Qaddara%2CI.&author=Alraba%E2%80%99nah%2CY.)

[^46]: Qaddara, I. A., Kenana, A. J., Al-Tarawneh, K. M. & Sarhan, S. Evaluation of CPU Scheduling and Synchronization Algorithms in Distributed Systems. *Nanotechnol Percept*, 698–719, (2024).

[^47]: Kraidia, I. & Belhaouari, S. B. Towards Robust SEA Detection: Leveraging Model Diversity and Randomization Against Adversarial Attacks, In: *12th International Conference on Information* Technology *(ICIT)*, (IEEE, 2025). [https://ieeexplore.ieee.org/abstract/document/11049179/](https://ieeexplore.ieee.org/abstract/document/11049179/)

[^48]: Kraidia, I., Kassoul, K., Cheikhrouhou, N., Hassan, S. & Belhaouari, S. B. ExPSO-DL: An Exponential Particle Swarm Optimization Package for Deep Learning Model Optimization, *J. Open Res. Softw.*13, 1, 2025 Available: [https://openresearchsoftware.metajnl.com/articles/521](https://openresearchsoftware.metajnl.com/articles/521)