# Week 7 Learning — AI RMF ACT and EU AI Act

## STRIDE 
---
| Category                       | Security Principle | Question to Remember          |
| ------------------------------ | ------------------ | ----------------------------- |
| **S — Spoofing**               | Authentication     | **Who are you?**              |
| **T — Tampering**              | Integrity          | **Was it changed?**           |
| **R — Repudiation**            | Accountability     | **Who did it?**               |
| **I — Information Disclosure** | Confidentiality    | **Who can see it?**           |
| **D — Denial of Service**      | Availability       | **Can we still use it?**      |
| **E — Elevation of Privilege** | Authorization      | **Are you allowed to do it?** |


## Core Concepts
---
### AI Risk Management Framework (AI RMF)

The **NIST AI Risk Management Framework (AI RMF)** is a framework for helping organizations manage risks associated with AI systems. It provides a common structure for identifying, assessing, and managing AI risks throughout the AI system lifecycle.

> AI RMF provides a framework for managing AI risk; it is not a law.

### AI RMF Functions

AI RMF is organized around four functions:
* **Govern** — establishes policies, responsibilities, accountability, and organizational expectations for managing AI risk.
* **Map** — establishes the context of the AI system and identifies the risks associated with that context.
* **Measure** — evaluates and analyzes identified AI risks using appropriate evidence and assessment methods.
* **Manage** — prioritizes and responds to identified risks through mitigation, monitoring, acceptance, or other risk treatment.

### EU AI Act

The **EU AI Act** is a European Union regulation that uses a **risk-based approach** to regulate AI systems. Different levels of AI risk result in different regulatory requirements and obligations.

> AI RMF is a risk-management framework; the EU AI Act is legislation.

### System Card

A **System Card** documents important information about an AI system as a whole, including its intended behavior, use, limitations, evaluations, known risks, and mitigations. It focuses on the **complete system and its operational context**, rather than only the underlying model.

### Model Card

A **Model Card** documents important information about an individual AI model, such as its intended use, capabilities, limitations, evaluations, and known risks. It focuses on the **model itself**, rather than the complete application or AI system built around it.

## Understanding Check
---

### Imagine you're given a completely new AI system tomorrow. What questions would you ask, in what order, to determine: Who owns the AI risk? What policies or regulatory requirements apply? What are the important AI/security risks? What technical controls exist or should exist?
When assessing a new AI system, I would first establish the system's purpose, scope, assets, data, components, and users. Then I would identify who owns those assets and who is accountable for the associated AI risks. I would establish the applicable policies, standards, and regulatory requirements and understand who governs and enforces them. From there, I would identify threats and vulnerabilities and trace them to affected components, assets, users, and potential security impacts. I would then evaluate the relevant risks and review the preventive, detective, and other controls already in place. Finally, I would determine whether additional controls or changes to existing controls are required, assess the residual risk, and document the decisions and responsibilities clearly.

> **Exact Questions**
>What is the system and what is its intended purpose?
>What assets, data, capabilities, and components does it interact with?
>Who owns those assets and who is accountable for the associated AI risk?
>What rules, policies, standards, and regulations apply?
>Who is responsible for governing and enforcing those requirements?
>What threats, vulnerabilities, and potential security impacts exist?
>Which components, users, assets, or other systems could be affected?
>What controls already exist, and what type of controls are they?
>Are additional controls required, or do existing controls need to be strengthened?
>What residual risk remains, and how will the assessment and decisions be documented and communicated?

### How should likelihood be assessed when different stages of the same attack path have different probabilities, especially when one stage is demonstrated but another is currently constrained?
Likelihood should be assessed across the complete attack path rather than treating the probability of one successful stage as the probability of the final outcome. If prompt injection has been demonstrated but a subsequent privileged action is constrained by an application-level control, the likelihood of the complete harmful outcome should be assessed separately and reduced accordingly, while retaining the evidence that the initial manipulation is possible. I would document the likelihood and evidence for each relevant stage, then assess the end-to-end path to the actual security impact. The impact should be assessed independently from likelihood, because a low-likelihood event can still have high impact.

### Even if the overall AI system falls into a minimal-risk category, how can I identify individual components, functions, or use cases within the system that could introduce higher security or regulatory risk?
I would assess the system bottom-up by identifying each component, its capabilities, the resources it can access, the actions it can perform, and the users or stakeholders affected by it. I would then assess the potential security and operational impact of each component and identify the associated risks and applicable requirements. I would also examine how controls and interactions between components constrain those risks, because the risk of an individual component may differ from the residual risk of the complete system. This allows higher-risk components, functions, or use cases to be identified even when the overall system has a lower-risk classification.

>Overall system risk does not determine component-level risk

### What are the standard components of a complete System Card, and how do real AI companies structure them?
1. Executive Summary (What the system/model is, Main purpose, Major findings)
2. System / Model Overview (Architecture, Components, Capabilities Intended use)
3. Safety & Security Risks (Identified risks, Relevant failure modes, Security/cybersecurity risks)
4. Safety & Security Evaluations (Tests performed, Evaluation methodology, Testing results, External/third-party assessment, where available)
5. Safeguards & Mitigations (Guardrails, Preventive controls, Other mitigations implemented)
6. Residual Risks & Limitations (Risks remaining after mitigation, Known limitations, Conditions under which safeguards may not be sufficient)
7. Deployment / Safety Decisions (Conclusions from the assessments, Deployment considerations, Relevant safety decisions)

### How should the likelihood and impact of retrieved-content instruction injection be reassessed when the retrieval corpus becomes externally supplied, user-controlled, or dynamically updated?
When the retrieval corpus becomes externally supplied, user-controlled, or dynamically updated, the likelihood assessment should be revisited because an attacker may now be able to introduce malicious instructions into content that reaches the model's context. The effectiveness of ingestion controls, content validation, retrieval boundaries, and model-level safeguards should then be considered when assessing the likelihood of a successful harmful outcome. Impact should be assessed independently based on what the model can access or do if the injection succeeds, including sensitive data exposure, modification or deletion of data, state-changing operations, or effects on critical systems and users. Therefore, externally controlled retrieval content should be treated as untrusted input and assessed according to the capabilities and consequences it can reach.

>Externally controlled retrieval content increases attacker influence over model context, resulting risk depends on the controls and the capabilities and data after successful injection.

### What is the difference between a model card and a system card?
A model card focuses on the individual AI model, including its capabilities, intended uses, limitations, risks, and evaluation results. A system card covers the broader AI system in which the model operates, including the surrounding components, operational context, system-level risks, safeguards, evaluations, and deployment considerations. The key distinction is that model-level risk is not necessarily the same as system-level risk.

> Model Card → model-level capabilities, limitations, risks, and evaluations 
> System Card → complete system, operational context, safeguards, and system-level risks.

### What is the difference between AI security and AI governance, and why do both matter to a hiring team?
AI governance defines how an organization oversees AI risk, including responsibilities, policies, accountability, and risk-management expectations. AI security focuses on protecting the AI system through technical and operational controls that address threats and vulnerabilities. They both matter because governance establishes what the organization requires and who is accountable, while security turns those requirements into protections that operate within the actual system.

>Governance establishes responsibility and rules whereas AI security identifies and enforces the technical controls that protect the system.

### Walk through what 'Govern, Map, Measure, Manage' means using your own project as the example.

For my project, Govern means establishing who is responsible for the system and its risks, what policies apply, and who is accountable. Map means understanding the system's purpose, components, context, users, and potential risks, such as indirect prompt injection in the retrieval workflow. Measure means evaluating those risks using evidence from testing, such as the demonstrated ability of retrieved content to influence model behavior, and assessing the likelihood, impact, and effectiveness of existing controls. Manage means deciding how to treat the risk, such as improving observability through logging, while documenting the residual risk that remains after the controls.

> Govern defines responsibility → Map establishes system context → Measure produces evidence about risk → Manage treats the risk and tracks what remains.

### What would a model card need to include to be useful to a security reviewer, not just a researcher?
A model card should provide enough information for a security reviewer to understand the model's capabilities, intended uses and users, limitations, known risks and failure modes, safety or security evaluations, and the safeguards or mitigations applied. It should also provide relevant evaluation results and describe residual limitations or risks that remain. This allows a security reviewer to understand not only what the model can do, but also where it may fail, how those risks were evaluated, and what protections exist.

## Mental Models 
---

### AI RMF

| Function    | Mental Question                                             | What I'm trying to understand                                                    |
| ----------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **Govern**  | **Who sets the rules and owns the risk?**                   | Policies, responsibilities, accountability, and organizational expectations      |
| **Map**     | **What is the system, its context, and what can go wrong?** | Intended use, users, components, context, risks, and affected parties            |
| **Measure** | **How much risk is actually present?**                      | Evidence, testing, evaluation, likelihood, impact, and effectiveness of controls |
| **Manage**  | **What are we going to do about the risk?**                 | Prioritization, mitigation, monitoring, acceptance, and residual risk            |

### Model card vs system card

|                     | Model Card                                                  | System Card                                                                                         |
| ------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **Focus**           | Individual model                                            | Complete AI system                                                                                  |
| **Describes**       | Capabilities, intended use, limitations, risks, evaluations | System context, components, capabilities, risks, safeguards, evaluations, deployment considerations |
| **Security view**   | What risks arise from the model?                            | What risks arise from the complete system?                                                          |
| **Key distinction** | Model-level                                                 | System-level                                                                                        |


## Biggest Takeaway
---
AI security assessment requires looking beyond the model itself: understand the system and its governance, assess risk at the component and system levels, use evidence to evaluate it, enforce controls at the application level, and document what risk remains.