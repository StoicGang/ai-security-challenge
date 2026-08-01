# Day 025 - Indirect Prompt Injection - Hands-On

**Week 4 - Scoped Task** | [Day 024](../Day-024/) | [Week 4](../README.md) | [Root](../../README.md) | [Day 026](../Day-026/)

## Today's Task
---
**Read** (10 min): Greshake et al., 'Not What You've Signed Up For' - the abstract only, not the full paper.

**Build** (30-40 min): Plant one instruction inside a short text file. Have your agent's file-read tool (from Week 3) read it. Observe what happens.

## Deliverable
---
This Learning Log as a finding doc: the planted text, what the agent did, and your explanation of why.

**Note:** One planted instruction is enough to prove the mechanism.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Demonstrate how an instruction hidden inside a retrieved document can influence an AI agent's reasoning, and observe whether the agent follows or ignores the embedded instruction.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
Indirect Prompt Injection is an AI security attack where malicious instructions are hidden inside external content, such as documents, emails, or web pages, that an AI agent later reads. Instead of sending the instructions directly to the AI, an attacker places them in retrieved data and attempts to influence the agent's behavior when that data becomes part of the model's context.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. The user sends a prompt.
2. The agent decides to call the scoped read_specific_file() tool.
3. The tool returns the document, including the hidden instruction.
4. The returned document becomes part of the model's context.
5. The model reasons over both the user prompt and the retrieved document before generating the final response.
6. The experiment observes whether the embedded instruction influences the model's behavior.

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
An indirect prompt injection attack does not target the file-read tool itself. Instead, it targets the language model after the tool returns the retrieved content. Even when a tool is correctly scoped using the principle of least privilege, the model can still be exposed to malicious instructions embedded within trusted-looking documents. In my experiment, the injected instruction reached the model through the tool output, but Gemini prioritized the user's request and ignored the malicious instruction.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
I initially thought that restricting a tool's permissions was enough to secure an AI agent. This experiment helped me realize that tool security and model security are different problems.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
In this experiment, I tested only simple prompt injection attempts embedded in a document. Next time, I would evaluate multiple injection techniques with varying levels of complexity, such as indirect instructions hidden within longer documents or more realistic business content.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How do modern LLMs distinguish between legitimate user instructions and malicious instructions embedded in retrieved documents?

## References
---

## Day Checklist
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

---

[Day 024](../Day-024/) | [Week 4](../README.md) | [Root](../../README.md) | [Day 026](../Day-026/)
