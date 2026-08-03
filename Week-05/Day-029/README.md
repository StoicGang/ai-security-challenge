# Day 029 - Model Extraction - Concept Only

**Week 5 - Scoped Task** | [Week 5](../README.md) | [Root](../../README.md) | [Day 030](../Day-030/)

## Today's Task
---
**Read** (10 min): Carlini et al., 'Extracting Training Data from Large Language Models' - the abstract only.

**Build** (20-30 min): Write a 3-5 sentence plain-language explanation of what the attack does, in your own words, as if explaining to a non-technical friend.

## Deliverable
---
This Learning Log with the plain-language paragraph - no copied phrasing, your own words only.

**Note:** No hands-on extraction attempt this week - conceptual understanding is the bar.

## Learning Log

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
The challenge was to understand how a training data extraction attack can cause a model to reveal memorized parts of its training data, making it a security and privacy risk.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
Imagine someone has read millions of documents belonging to a company, including employee records and internal policies. Normally, when people ask questions, they should answer using what they learned instead of repeating the documents word for word. The problem begins when they start revealing exact details, such as confidential employee information or internal company data. An attacker can intentionally ask carefully chosen questions to make those hidden details come out, even though they were never meant to be shared.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Identified what information an attacker is trying to recover from an AI system.
2. Compared an AI that answers from learned patterns with one that repeats specific information it has seen before.
3. Connected that behavior to the resulting privacy and security risks.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python

```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
I learned that a training data extraction attack is not about stealing or copying the AI model. Its goal is to recover specific pieces of information that the model memorized during training, which can create serious privacy and security risks.
A model becomes a security and privacy risk when it reproduces specific pieces of its training data instead of only generating responses based on learned patterns.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
The idea clicked when I realized the attacker isn't trying to obtain the AI itself. They're trying to make it repeat specific information it retained from its training data.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
After reading the abstract, I would first explain the concept in my own words before thinking about the security impact.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
I understand what the attack achieves, but I still don't know what capabilities the attacker has or what interaction method is used to recover the memorized information.

---

## Day Checklist
- [ ] Reading done (within time box - don't let one resource eat the whole day)
- [ ] Build complete
- [ ] Deliverable exists exactly as specified above
- [ ] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [ ] Committed to GitHub

---

[Week 5](../README.md) | [Root](../../README.md) | [Day 030](../Day-030/)
