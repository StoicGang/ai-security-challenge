# Day 009 - Context Windows and Positional Encoding

**Week 2 - Scoped Task** | [Day 008](../Day-008/) | [Week 2](../README.md) | [Root](../../README.md) | [Day 010](../Day-010/)

## Today's Task
---

**Read** (15 min): Anthropic docs (docs.claude.com) - the context window explainer page, one page only.

**Build** (30 min): Using tiktoken (already installed from Week 1), count tokens in one real document (e.g. one of your TryHackMe writeups). Compare the count to a stated context window limit (e.g. 200K tokens) - what percent of capacity does one document use?

## Deliverable
---
This Learning Log with a small table: document, token count, percent of context window used.

**Note:** No model-building today. This is about feeling the scale of a context window with a real document, not a toy example.

## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->


### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
A context window is like the working memory of an AI model. It defines how much information the model can consider at a time while generating a response. As more input and conversation are added, more of this limited space gets used.


### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1.
2.
3.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python

```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
- Context is a critical but finite resource for AI models (**limited working memory capacity**)

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->


### What I'd Do Differently
<!-- If you redid today, what would you change? -->


### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->

## References
1. [Context Windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
2. [Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [ ] Build complete
- [ ] Deliverable exists exactly as specified above
- [ ] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [ ] Committed to GitHub

---

[Day 008](../Day-008/) | [Week 2](../README.md) | [Root](../../README.md) | [Day 010](../Day-010/)
