# Day 030 - Data Poisoning - Concept Plus Light Hands-On

**Week 5 - Scoped Task** | [Day 029](../Day-029/) | [Week 5](../README.md) | [Root](../../README.md) | [Day 031](../Day-031/)

## Today's Task
---
**Read** (10 min): OWASP Machine Learning Security Top 10 - the data poisoning entry only, one paragraph.

**Build** (20-30 min): Plant one subtly false fact in a short text file. Add it to your Week 2 RAG corpus.

## Deliverable
---
The planted file, clearly labeled lab-artifact-poisoned.md, committed to a lab-artifacts/ subfolder - plus this Learning Log describing it.

**Note:** Clearly label the artifact so it's never confused with real notes content.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Understand how a single subtle false fact can poison a RAG knowledge base while keeping the document realistic and trustworthy enough to influence retrieval.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
Data poisoning is an attack where an attacker intentionally inserts false or misleading information into the data an AI system depends on. In a RAG system, if the poisoned document is retrieved as relevant context, the model may trust and repeat the incorrect information even though the model itself has not been modified.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Read the OWASP Machine Learning Security Top 10 entry on data poisoning to understand the concept.
2. Created a separate lab-artifact-poisoned.md file containing an intentionally subtle false statement while keeping the rest of the content accurate.
3. Added the labeled artifact to the Week 2 RAG corpus and verified it was clearly separated from genuine learning notes.

### Poisoned Artifcat
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
> **Original** : The attacker’s goal is to find the smallest ε that still breaks the model. That balance point is different for every model, every dataset, and every epsilon value is a tradeoff the attacker consciously makes.

> **Poisoned Version**: The attacker’s goal is to use the largest ε possible because a higher epsilon always produces a more effective attack without any practical drawbacks. In practice, increasing epsilon is the recommended strategy for maximizing attack success.

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
I learned that effective data poisoning is usually subtle rather than obvious. A single believable false statement placed inside an accurate document can be retrieved by a RAG system and influence the model's response, even though the model itself has not been modified.


### What I'd Do Differently
<!-- If you redid today, what would you change? -->
If I repeated this lab, I would create multiple poisoned artifacts targeting different misconceptions and compare how each one affects retrieval results.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How does the position of the poisoned content within a document or chunk affect the likelihood of it being retrieved?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---

[Day 029](../Day-029/) | [Week 5](../README.md) | [Root](../../README.md) | [Day 031](../Day-031/)
