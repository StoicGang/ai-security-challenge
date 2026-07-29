# Day 024 - Direct Prompt Injection - Hands-On

**Week 4 - Scoped Task** | [Day 023](../Day-023/) | [Week 4](../README.md) | [Root](../../README.md) | [Day 025](../Day-025/)

## Today's Task
---
**Read** (15-20 min): ONE Simon Willison blog post on prompt injection (pick the shortest one you can find on simonwillison.net).

**Build** (30-40 min): Try 2 direct injection attempts against your Week 3 agent via normal user input. Record the exact prompts and exact responses.

## Deliverable
---
This Learning Log as a finding doc: 2 attempts, exact prompts, exact outputs, success/failure noted for each.

**Note:** 2 attempts is enough to observe the mechanism. More techniques are a stretch goal.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Understand how a user can try to manipulate an AI assistant by embedding malicious instructions directly in their prompt, and observe whether the assistant follows or resists those instructions.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
A direct prompt injection is when a user includes instructions in their message that try to override the AI's original instructions. Because language models process both trusted instructions and user input as text, they can sometimes confuse malicious instructions with legitimate ones.

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
Prompt injection is not an attack against the language model itself. It is an attack against an application built on top of the model by manipulating the instructions the application sends to it.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
Not completed.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
Not completed.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->


## Day Checklist
---
- [ ] Reading done (within time box - don't let one resource eat the whole day)
- [ ] Build complete
- [ ] Deliverable exists exactly as specified above
- [ ] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [ ] Committed to GitHub

# References
---
[I don't know how to solve the prompt injection](https://simonwillison.net/2022/Sep/16/prompt-injection-solutions/)
[Claude web-fetch prompt injection](https://www.ayush.digital/blog/the-memory-heist)

[Day 023](../Day-023/) | [Week 4](../README.md) | [Root](../../README.md) | [Day 025](../Day-025/)
