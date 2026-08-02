# Day 028 - Week 4 to Week 5 Handoff

**Week 4 - Preview** | [Day 027](../Day-027/) | [Week 4](../README.md) | [Root](../../README.md) | [Week 05](../../Week-05/)

---

## Today's Task

**Read** (5-10 min): One sentence definition of 'data poisoning' - from any source, not a paper.

**Build** (10 min): Confirm all Week 4 learning logs exist. Write your current hypothesis: what's the difference between a runtime attack (Week 4) and a training-time attack (Week 5)?

## Deliverable
---
Confirmation note plus your hypothesis written out.

**Note:** Light day on purpose.

---

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Understand the difference between runtime attacks and training-time attacks while preparing to transition from Week 4 to Week 5, and verify that all Week 4 learning logs were complete.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
Data poisoning is a training-time attack where an attacker manipulates the training data so the model learns incorrect or malicious behavior before it is deployed.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Read a one-sentence definition of data poisoning.
2. Reviewed and confirmed the Week 4 learning logs.
3. Compared runtime attacks with training-time attacks and wrote my hypothesis.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python

```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
Training-time attacks target the model's learning process by manipulating the training data or training pipeline, causing the model to learn incorrect behavior. 
Runtime attacks target an already deployed model by manipulating its inputs or surrounding components to influence its behavior without changing the trained model.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
The difference between runtime and training-time attacks isn't only when they happen, but also what they target.

### Current Hypothesis

My current hypothesis is that runtime attacks occur after a model has been deployed, where an attacker manipulates inputs, prompts, or surrounding application components to influence the model's behavior without changing the trained model. In contrast, training-time attacks target the training data or training process before deployment, causing the model to learn incorrect or malicious behavior. The fundamental difference is both when the attack occurs in the AI lifecycle and what the attacker is trying to influence.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->

Apart from data poisoning, what other types of training-time attacks exist, and how do they affect a model during training?

## Day Checklist
---
- [ ] Reading done (within time box - don't let one resource eat the whole day)
- [ ] Build complete
- [ ] Deliverable exists exactly as specified above
- [ ] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [ ] Committed to GitHub

## References
---
[IBM data poisoning](https://www.ibm.com/think/topics/data-poisoning)
[Ai Security](https://aisecurityandsafety.org/en/guides/data-poisoning/)

[Day 027](../Day-027/) | [Week 4](../README.md) | [Root](../../README.md) | [Week 05](../../Week-05/)
