# Day 021 - Week 3 to Week 4 Handoff

**Week 3 - Preview** | [Day 020](../Day-020/) | [Week 3](../README.md) | [Root](../../README.md) | [Week 04](../../Week-04/)

## Today's Task
---
**Read** (10 min): OWASP Top 10 for LLM Applications - the category names only, not the descriptions.

**Build** (10 min): Confirm all Week 3 learning logs exist. Write which category you already suspect applies to your Week 3 agent.

## Deliverable
---
Confirmation note plus one suspected OWASP category with a one-sentence reason.

**Note:** Light day on purpose - Week 4 is hands-on offense.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Today's challenge was to begin viewing my Week 3 AI agent from a security perspective by identifying which OWASP risk category might apply to it.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
The OWASP Top 10 for LLM Applications is a list of the ten most important categories of security risks that developers should think about when building applications that uses Large Language Models.

| **OWASP Top 10 for LLM Applications (2023–24)** | **OWASP Top 10 for LLM Applications (2025)** |                                      |
| ----------------------------------------------- | -------------------------------------------- | ------------------------------------ |
| LLM01: Prompt Injection                         | LLM01: Prompt Injection                      |                                      |
| LLM02: Insecure Output Handling                 | LLM02: Sensitive Information Disclosure      |                                      |
| LLM03: Training Data Poisoning                  | LLM03: Supply Chain                          |                                      |
| LLM04: Model Denial of Service                  | LLM04: Data and Model Poisoning              |                                      |
| LLM05: Supply Chain Vulnerabilities             | LLM05: Improper Output Handling              |                                      |
| LLM06: Sensitive Information Disclosure         | LLM06: Excessive Agency                      |                                      |
| LLM07: Insecure Plugin Design                   | LLM07: System Prompt Leakage                 |                                      |
| LLM08: Excessive Agency                         | LLM08: Vector and Embedding Weaknesses       |                                      |
| LLM09: Overreliance                             | LLM09: Misinformation                        |                                      |
| LLM10: Model Theft                              | LLM10: Unbounded Consumption                 | |


### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Think like an attacker.
2. Imagine the attacker's goal.
3. Follow the attack path.
4. Check which security controls stop it.
5. Map that reasoning to an OWASP category (prompt injection).

>*note*: look at the [OWASP Mapping](OWASP_mapping.md) file for the exact mapping

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
Security is not achieved by writing better prompts. It's achieved by designing better systems.
Security begins by understanding an attacker's objective, not by searching for vulnerabilities. By identifying what an attacker would try to achieve against my AI agent and then examining how my security controls respond, I could reason about the most relevant OWASP risk category instead of guessing based on category names.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
I realized that the same attacker-first mindset used in traditional application security can be applied to AI agents, even though the attack vectors are different.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
Instead of selecting an OWASP category based on its name, I would first create a simple threat model by identifying the system's assets, entry points, trust boundaries, attacker goals, and existing security controls. I would then map those observations to the most relevant OWASP category.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How do professional security engineers perform threat modeling for LLM agents before any vulnerabilities are discovered?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---
[OWASP top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
[OWASP top 10 2025](https://genai.owasp.org/llm-top-10/)

[Day 020](../Day-020/) | [Week 3](../README.md) | [Root](../../README.md) | [Week 04](../../Week-04/)
