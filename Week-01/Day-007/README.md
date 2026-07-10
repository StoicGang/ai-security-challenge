# Day 007 - Week 1 to Week 2 Handoff

**Week 1 - Preview** | [Day 006](../Day-006/) | [Week 1](../README.md) | [Root](../../README.md) | [Week 02](../../Week-02/)

## Today's Task
---
**Read** (10 min max): One paragraph on what 'attention' is - not an article, a single paragraph from any intro source you find.

**Build** (-): Confirm all 5 weekday learning logs exist. No new build today.

## Deliverable
---
Confirmation note that all Week 1 Learning Logs exist; one open question carried into Week 2, written below.

**Note:** Light day on purpose - Week 2 starts fresh on Day 8.

## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Understanding of the attention mechanism, and identify one question to carry into Week 2.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
Attention allows the model to dynamically determine which parts of the input are most relevant when interpreting the current token. The important parts are not fixed, they depend on what the model is processing at that moment.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Read the sentence from left to right.
2. When reaching a new word, ask: "Which earlier words help me understand this word?"
3. Give more focus to the relevant words and less focus to unrelated or filler words.
4. Repeat this process for every word in the sentence, allowing the important context to change dynamically.


### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
Unlike a fixed summary of the sentence, the important context changes depending on what the model is processing at that moment.


### What I'd Do Differently
<!-- If you redid today, what would you change? -->
Before writing any code for the attention mechanism, I would first walk through a simple sentence on paper and manually identify which words should pay attention to each other. Once I can explain why certain words are more relevant than others, I would map that intuition to the implementation instead of treating the code as a collection of mathematical operations.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How does a Transformer mathematically determine which words should receive more attention?

### References
1. [GFG](https://www.geeksforgeeks.org/artificial-intelligence/ml-attention-mechanism/)
2. [Transformer guide](https://krugis.github.io/transformer-guide/)

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---

[Day 006](../Day-006/) | [Week 1](../README.md) | [Root](../../README.md) | [Week 02](../../Week-02/)
