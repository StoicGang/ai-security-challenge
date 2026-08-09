# Day 035 - Week 5 to Week 6 Handoff

**Week 5 - Preview** | [Day 034](../Day-034/) | [Week 5](../README.md) | [Root](../../README.md) | [Week 06](../../Week-06/)

## Today's Task
---
**Read** (0-10 min): No new reading required if STRIDE is already familiar from your cybersecurity background - otherwise a 10-minute refresher on the 6 STRIDE categories.

**Build** (10 min): Confirm all Week 5 learning logs exist. Write your hypothesis: how would you use your Week 4 findings as input to a threat model?

## Deliverable
Confirmation note plus your hypothesis written out.

**Note:** Light day on purpose.


## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Identify the relevant STRIDE categories and map the attacker’s path through the application, using the security findings from the Day 024 OWASP LLM Top 10 assessment as inputs.

### Key Concept

STRIDE is a threat-modeling framework used to classify threats based on the security property they can affect. For Day 035, the STRIDE categories are used together with the findings from the **[Day 024 OWASP LLM Top 10 security assessment](./../../Week-04/Day-024/findings.md)** to identify how an existing vulnerability could translate into a concrete threat against the application's architecture.

### Hypothesis

The security findings documented in the **[Day 024 OWASP LLM Top 10 assessment](./../../Week-04/Day-024/findings.md)** can be used as inputs to a threat model by mapping each relevant finding onto the application's architecture and identifying the corresponding attacker path, affected component, potential impact, and STRIDE category. For example, the Day 024 **LLM01 Prompt Injection** finding can be mapped from attacker-controlled user input through the application and LLM to potential unintended tool invocation, while the existing least-privilege controls determine how far that attack can actually affect the system. This approach should allow the OWASP vulnerability mapping and STRIDE threat model to complement each other, with the former identifying the AI-specific vulnerability and the latter describing the resulting security threat and affected security property.


### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
- Threat modeling must consider both the attacker's potential path and the security controls already implemented, rather than assuming that successful manipulation of the LLM automatically means full system compromise.
- The actual impact of a vuln depends heavily on the capabilities exposed to the model. The Day 024 least-privilege design limits the impact because the available tools cannot modify files, access arbitrary files, or perform external state-changing actions.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
The main realization was that prompt injection and system compromise are not the same thing. Even if an attacker successfully influences the LLM's behavior, the actual impact is constrained by the capabilities exposed through the application's tools.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
After completing an OWASP LLM Top 10 assessment, I would immediately map each relevant finding to the application's architecture, attacker entry point, attack path, affected asset, potential impact, and applicable STRIDE category.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How should multiple STRIDE categories be prioritized when a single AI security finding can lead to different impacts depending on the attack path?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---
[Devesecops article](https://www.practical-devsecops.com/what-is-stride-threat-model/)
[Trent AI article](https://trent.ai/blog/stride-threat-model/)

[Day 034](../Day-034/) | [Week 5](../README.md) | [Root](../../README.md) | [Week 06](../../Week-06/)
