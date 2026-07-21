# Day 016 - The Agent Loop - Plan, Act, Observe

**Week 3 - Scoped Task** | [Day 015](../Day-015/) | [Week 3](../README.md) | [Root](../../README.md) | [Day 017](../Day-017/)

## Today's Task
---
**Read** (15 min): A short blog explainer of the ReAct pattern - one paragraph summary, not the full paper (save the paper for later if curious).

**Build** (30-40 min): Extend Day 15 so the tool's result is fed back to the model, which then gives a final natural-language answer - a 2-step loop, not a full framework.

## Deliverable
---

This Learning Log showing: user question, tool call, tool result, final answer, all logged.

**Note:** A 2-step loop is enough to prove the mechanism. Multi-step planning is a later stretch goal.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Extend the function-calling workflow so that, after the application executes the requested tool, its result is sent back to the LLM, allowing it to continue reasoning and generate a final natural-language response.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
The LLM never directly interacts with external tools. Instead, the application acts as the bridge: it executes the requested tools, returns their results to the LLM, and enables the LLM to continue its reasoning before producing the final response.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. The application sends the user's prompt along with the available tool definitions to the LLM.
2. If the LLM determines that external information or computation is required, it returns a structured function call instead of a final answer.
3. The application executes the requested tool, packages the result as a function_result, and sends it back to the same interaction.
4. The LLM continues its reasoning using the tool's output as evidence and generates the final natural-language response.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
final_interaction = client.interactions.create(
    model=GENAI_MODEL_NAME,
    previous_interaction_id=interaction.id,
    input=function_results,
    tools=[calculator_function, datetime_function],
)

print(final_interaction.output_text)
```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
Function calling is not a single request-response operation but an iterative reasoning loop. The LLM can only continue its reasoning after the application returns the tool's output, making the application an active participant rather than just a request forwarder.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
The application isn't just a messenger between the user and the LLM.
Tool gathers the evidence, LLM explains the evidence.
    LLM → Thinks
    Tool → Does
    LLM → Thinks again

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
I would love to put this into modular approach with different file for different service like reasoning and request-response workflow.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How does the reasoning loop support multiple sequential or parallel tool calls within a single interaction?

---

## Day Checklist
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---
[IBM react agent documentation](https://www.ibm.com/think/topics/react-agent)
[Agent patterns](https://agent-patterns.readthedocs.io/en/stable/patterns/react.html)
[gemini docs](https://ai.google.dev/gemini-api/docs/function-calling)

[Day 015](../Day-015/) | [Week 3](../README.md) | [Root](../../README.md) | [Day 017](../Day-017/)
