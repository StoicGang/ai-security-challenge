# Day 045 - EU AI Act Awareness (Light)

**Week 7 - Scoped Task** | [Day 044](../Day-044/) | [Week 7](../README.md) | [Root](../../README.md) | [Day 046](../Day-046/)

## Today's Task
---
**Read** (10 min): EU AI Act summary (European Commission digital strategy site) - one paragraph on risk tiers only.

**Build** (15-20 min): Classify your own app into a risk tier. Write a 2-sentence justification.

## Deliverable
---
This Learning Log with the tier classification and 2-sentence justification.

**Note:** Conceptual literacy only - this is not a legal deep-dive.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Given the project built in Week 3, what category under the EU AI Act can we put our project in, and why?

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
The EU AI Act uses a risk-based approach, where an AI system's risk depends largely on what it is intended to do and the potential impact of that use, rather than simply whether the system uses AI.

| Risk category         |   meaning                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------- |
| **Unacceptable risk** | AI uses that are prohibited because they create unacceptable risks.                                   |
| **High risk**         | AI used in specific sensitive or consequential areas where stronger requirements apply.               |
| **Limited risk**      | AI with specific transparency obligations, such as informing users when they are interacting with AI. |
| **Minimal/no risk**   | Most ordinary AI uses with relatively low risk and few or no additional obligations.                  |


### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Read the EU AI Act risk-tier summary.
2. Identified the intended use and potential impact of the Week 3 RAG system.
3. Classified the system and justified the selected risk tier.

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
I would put the system in the minimal-risk category under the EU AI Act because its intended use is personal experimentation, knowledge retrieval, and learning. The output primarily affects my own understanding rather than being used to make consequential decisions about other people.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
The same RAG system could have a different EU AI Act risk classification if its purpose changed, even if the underlying model and implementation stayed the same.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
I would first identify the system's intended use, identify the users affected by its output, and create simple user stories to understand the possible impact before assigning a risk category.
`System → intended use → users → possible impact → risk classification`

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
Even if the overall AI system falls into a minimal-risk category, how can I identify individual components, functions, or use cases within the system that could introduce higher security or regulatory risk?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written 
- [x] Committed to GitHub

##  Refrences
---
[EU AI act risk categories](https://governancedocs.com/eu-ai-act-risk-categories/)

[Day 044](../Day-044/) | [Week 7](../README.md) | [Root](../../README.md) | [Day 046](../Day-046/)
