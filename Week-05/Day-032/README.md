# Day 032 - ML Supply Chain Basics

**Week 5 - Scoped Task** | [Day 031](../Day-031/) | [Week 5](../README.md) | [Root](../../README.md) | [Day 033](../Day-033/)

## Today's Task
---
**Read** (10-15 min): Hugging Face - model cards and provenance documentation, the intro paragraph only.

**Build** (30 min): List 5 supply-chain checklist items relevant to your own project (e.g. 'model source documented,' 'dependencies pinned') - draft from your own DevSecOps knowledge, informed by the reading.

## Deliverable
---
This Learning Log with a markdown checklist - 5 items, each with pass/fail against your own project.

**Note:** 5 items is the bar this week, not 8+. Depth on 5 beats a rushed list of 10.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
To learn how to evaluate the trustworthiness of the AI components used in my project by understanding model cards, provenance, and creating a practical ML supply-chain security [checklist](checklist.md).

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
An AI model is part of the software supply chain, just like a library or dependency. Before using a model, we should know where it came from, who published it, which version we are using, and whether it is suitable for our use case.
A model card is documentation that describes a model, including details such as its purpose, publisher, supported tasks, limitations, license, and other important metadata. It helps developers make informed decisions before adopting a model.
Provenance is the ability to trace a model back to its original source and verify its origin and history. It helps establish trust by showing that the model being used is the intended one and has not been unexpectedly replaced or modified.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Read the introductory Hugging Face documentation on model cards and provenance to understand how AI models should be documented and traced to their source.
2. Identified the AI supply-chain components used in my AI Security Challenge project, such as models, APIs, and dependencies.
3. Created a five-item ML supply-chain security checklist and evaluated my project against each item using a pass/fail assessment.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
# No code was required for today's challenge.
```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
Before today, I thought choosing an AI model was mainly about its performance. Now I understand that a model is also part of the ML supply chain. Model cards provide the documentation needed to understand a model's purpose, limitations, and metadata, while provenance helps verify where the model came from and whether it can be trusted.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
I realized that AI models should be treated just like software dependencies. I wouldn't blindly trust or update a library without knowing its source and version

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
1. I would spend more time reading the model card itself instead of only understanding the concepts, so I can evaluate AI models using their actual documentation rather than assumptions.
2. If I were starting this project again, I would establish ML supply-chain practices from the beginning instead of adding them later. I would maintain a dedicated MODEL.md file for all external AI models, pin dependency versions for reproducible builds, document AI providers and model versions, and define a review process before updating models or major dependencies.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How can I verify the integrity and authenticity of an AI model beyond trusting the hosting platform?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---
[Hugging face Templates](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md)
[Model cards hugging face docs](https://huggingface.co/docs/hub/model-cards)

[Day 031](../Day-031/) | [Week 5](../README.md) | [Root](../../README.md) | [Day 033](../Day-033/)
