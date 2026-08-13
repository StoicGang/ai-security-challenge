# Day 039 - Basic Structured Logging

**Week 6 - Scoped Task** | [Day 038](../Day-038/) | [Week 6](../README.md) | [Root](../../README.md) | [Day 040](../Day-040/)

## Today's Task
---
**Read** (-): None - applied day.

**Build** (30 min): Add a simple print-based or file-based log that records every tool call your agent makes: tool name plus input.

## Deliverable
---
sample_log.md (or .json) with 3-5 example log lines from a real test run, committed alongside this Learning Log.

**Note:** A full structured logging pipeline with timestamps and session IDs is a later stretch goal - tool name plus input is the bar this week.

## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Observe every tool call made by the agent by printing the tool name and its input during execution.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
A tool call can be observed at the point where the agent produces the tool name and its input. Printing these values makes the agent's tool usage visible during execution.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Printed the tool name and input whenever the agent produced a tool call.
2. Ran the agent with queries that triggered multiple tools.
3. Verified that the tool calls appeared before the final agent answer.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
print(
    f"[TOOL CALL] "
    f"name={step.name} "
    f"input={step.arguments}"
)
```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
Tool calls are observable before the tool executes because the model provides the tool name and input as part of the function call. Printing these values makes the agent's actions visible without changing the tool execution itself.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
The agent can make several tool calls before producing its final answer. The tool calls are backend execution steps, while the final response is the actual agent answer, so they should be displayed separately.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
The agent can make several tool calls before producing its final answer. The tool calls are backend execution steps, while the final response is the actual agent answer, so they should be displayed separately.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How should tool-call logging handle arguments when a tool input may contain sensitive data or executable content?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---

[Day 038](../Day-038/) | [Week 6](../README.md) | [Root](../../README.md) | [Day 040](../Day-040/)
