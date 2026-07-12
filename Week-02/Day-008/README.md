# Day 008 - Self-Attention - The Core Idea

**Week 2 - Scoped Task** | [Week 2](../README.md) | [Root](../../README.md) | [Day 009](../Day-009/)

## Today's Task
---
**Read** (15 min): Jay Alammar - 'The Illustrated Transformer' - just the 'Self-Attention at a High Level' section, not the full article.

**Build** (30-40 min): By hand, on paper or in a markdown table: trace attention scores for a 3-word toy sentence. Make up simple 2D Q/K/V vectors, compute dot products, apply softmax, compute the weighted sum.

## Deliverable
---

This Learning Log with your traced calculation (the actual numbers at each step) included as a small table.

**Note:** No code required today - this is a by-hand exercise so the mechanism is visible before any library hides it.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Understand how self-attention determines the importance of words in a sentence and combines their information to create a context-aware representation of a word without code.


### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
Self-attention allows each word to look at the other words in a sentence, decide how important they are to its meaning, and combine their information to better understand the word in context.
 
$$
\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}
$$


### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Compared the query of one word with the keys of every word using dot products to calculate their attention scores.
2. Applied softmax to the scores to convert them into attention weights that show how much focus each word receives.
3. Multiplied each value vector by its attention weight and added the results to create a new context-aware representation of the word.

### Table 
consider vector represent of the query is $Q_{drinks}=[1,1]$

| Word      | Key (K)  | $$Q_{drinks} \cdot K$$ | Softmax weight | Value (V) | Weighted Value     |
| --------- | -------- | ------------------: | -------------: | --------- | ------------------ |
| cat       | `[1, 0]` |                   1 |           0.21 | `[1, 1]`  | `[0.21, 0.21]`     |
| drinks    | `[0, 1]` |                   1 |           0.21 | `[1, 0]`  | `[0.21, 0]`        |
| milk      | `[1, 1]` |                   2 |           0.58 | `[0, 1]`  | `[0, 0.58]`        |
| **Final** |          |                     |       **1.00** |           | **`[0.42, 0.79]`** |


### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
Attention weights only decide how much information to take from each word; the value vectors contain the actual information that is combined to create the final context-aware representation.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
It clicked when I thought of attention weights as volume knobs and value vectors as audio signals. A high volume means nothing if the signal contains no information.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
I would trace one word through query-key comparison, attention weights, and the weighted value sum before relying on a library implementation.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
Why is the query compared with the key to calculate attention scores instead of being compared directly with the value vector?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

# References
---
[Week 2](../README.md) | [Root](../../README.md) | [Day 009](../Day-009/)

[Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
[Youtube](https://www.youtube.com/watch?v=eMlx5fFNoYc)
