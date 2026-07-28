# Day 023 - OWASP LLM Top 10 - Categories 6 to 10

**Week 4 - Scoped Task** | [Day 022](../Day-022/) | [Week 4](../README.md) | [Root](../../README.md) | [Day 024](../Day-024/)

## Today's Task
---
**Read** (15 min): OWASP Top 10 for LLM Applications - the one-line summary of categories 6-10 only.

**Build** (20-30 min): Same mapping exercise for the remaining 5 categories. Flag the single riskiest category for your app in 1 sentence.

## Deliverable
---
This Learning Log with the mapping table completed (10 rows total) and the riskiest-category flag written.

**Note:** -

## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Extend the OWASP LLM Top 10 mapping by evaluating categories 6-10 against my application and identify the single highest-priority security risk.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->

| Category                                    | Meaning                                                         |
| ------------------------------------------- | --------------------------------------------------------------- |
| **LLM01: Prompt Injection**                 | Manipulating model behavior through malicious prompts.          |
| **LLM02: Sensitive Information Disclosure** | Exposing confidential or private information.                   |
| **LLM03: Supply Chain**                     | Risks introduced by third-party models, tools, or dependencies. |
| **LLM04: Data and Model Poisoning**         | Corrupting training data, models, or retrieval data.            |
| **LLM05: Improper Output Handling**         | Treating untrusted model output as trusted input.               |
| **LLM06: Excessive Agency**                 | Granting the model more authority than necessary.               |
| **LLM07: System Prompt Leakage**            | Revealing hidden prompts or internal instructions.              |
| **LLM08: Vector and Embedding Weaknesses**  | Attacks targeting RAG, embeddings, or vector databases.         |
| **LLM09: Misinformation**                   | Generating inaccurate or fabricated information.                |
| **LLM10: Unbounded Consumption**            | Excessive use of compute, tokens, APIs, or other resources.     |



### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. I rated Excessive Agency (LLM06) as Low Risk because, even if an attacker successfully manipulates the model's reasoning, the model only has read-only capabilities and cannot perform state-changing operations on external systems or application resources.
2. I would rate Category 7 as Low Risk because, even if an attacker learns the system prompt or tool descriptions, the exposed information does not grant additional capabilities, and the tool implementation enforces fixed, read-only behavior.
3. Category 8 is Not Applicable because this application does not contain a vector database, embedding model, or retrieval pipeline. Since no vector or embedding subsystem exists, there is no attack surface for vector or embedding manipulation.
4. Category 9 is rated Low Risk because the LLM performs a narrow summarization task on a single, developer-controlled article. Although the model may still generate inaccurate or fabricated information, the response is grounded in trusted input, making hallucinations less likely and limiting their potential impact compared with applications that answer arbitrary user questions or operate in high-stakes domains.
5. I rated category 10 as Low Risk because, even if an attacker successfully manipulates the model's reasoning, the model only has read-only capabilities and cannot perform state-changing operations on external systems or application resources.

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->


### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->


### What I'd Do Differently
<!-- If you redid today, what would you change? -->
If I were extending this project, I would intentionally introduce more complex components, such as a retrieval pipeline, external APIs, and additional tools, and then implement appropriate security controls. This would allow me to explore higher-risk OWASP categories and understand how mitigations change as the application's capabilities expand.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How should organizations reassess OWASP risk ratings as an AI application evolves over time?

## Day Checklist
----
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References 
---

[Day 022](../Day-022/) | [Week 4](../README.md) | [Root](../../README.md) | [Day 024](../Day-024/)
