# Day 046 - System Card (Light)

**Week 7 - Scoped Task** | [Day 045](../Day-045/) | [Week 7](../README.md) | [Root](../../README.md) | [Day 047](../Day-047/)

## Today's Task
---
**Read** (10 min): Skim ONE published system card's section headers only, to see the format - don't read the whole thing.

**Build** (30 min): Draft a mini system card for your Week 2 RAG component - just 3 sections: intended use, known risks, responsible party.

## Deliverable
---
system-card.md with 3 sections filled, committed alongside this Learning Log.

**Note:** 3 sections is the bar this week - a full multi-section card is a later stretch goal.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
How do I document an AI system at the system level by defining its intended use, known risks, and accountability, rather than documenting only the underlying model or implementation?

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
A System Card is structured documentation of a complete AI system, including the model and the surrounding components, controls, users, operational context, risks, and governance.


### Major Components of System-Cards
- Intended Use: Defines what the system is designed to do, who the intended users are, and the boundaries of its use.
- System Architecture & Components: Describes the major components that make up the system and how they interact, such as the LLM, RAG, databases, tools, APIs, and orchestration.
- Guardrails & Safety Controls: Documents controls used to restrict unsafe behavior, protect data, and enforce system boundaries.
- Known Risks & Limitations: Documents known failure modes, security risks, misuse cases, and limitations discovered through testing or analysis.
- Evaluation & Red-Teaming: Records how the system was tested and what failures or weaknesses were observed.
- Human Oversight & Monitoring: Defines where humans are responsible for reviewing, controlling, or monitoring system behavior.
- Responsible Party: Identifies who is accountable for maintaining the system, its data, controls, and risks.
- Governance & Compliance: Records relevant policies, regulatory requirements, data sources, licensing, and other governance information

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Reviewed the structure of a published system card and identified the main sections used to document an AI system.
2. Defined the intended use, known risks, and responsible party for the Week 2 RAG component based on its actual architecture and behavior.
3. Created [system-card](../../Week-02/system-card.md) with the three required sections and documented the identified risks and responsibilities.

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
A System Card is not just documentation of the model. It documents the system around the model, including its intended users and behavior, components, risks, limitations, controls, human responsibility, and governance.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
Today's System Card was intentionally limited to three sections, so I did not document the system architecture and component relationships, which are major parts of a complete System Card. I would add the architecture, component interactions, and other full-card sections later when the scope expands during this week.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
What are the standard components of a complete System Card, and how do real AI companies structure them?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---
[What is System cards](https://document360.com/blog/system-cards-and-datasheets/)
[Gemini 3.5 Flash model card](https://deepmind.google/models/model-cards/gemini-3-5-flash)
[Claude opus 5 system card](https://www-cdn.anthropic.com/ceaf5c7ff2783855203fde8208ec311252dced5b/Claude%20Opus%205%20System%20Card.pdf)

[Day 045](../Day-045/) | [Week 7](../README.md) | [Root](../../README.md) | [Day 047](../Day-047/)
