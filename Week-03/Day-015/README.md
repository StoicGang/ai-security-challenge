# Day 015 - Function and Tool Calling Basics

**Week 3 - Scoped Task** | [Week 3](../README.md) | [Root](../../README.md) | [Day 016](../Day-016/)

## Today's Task
---
**Read** (15-20 min): Anthropic docs (docs.claude.com) - 'Tool use' quickstart, the first example only.

**Build** (30 min): Using the Anthropic SDK, define ONE tool (a calculator function). Get the model to call it for a maths question.

## Deliverable
---
This Learning Log with the terminal output (copy-pasted) showing the tool call and its result.

**Note:** One tool, one question. No agent loop yet - that's Day 16.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
To understand how can an LLM delegate a specific task to an external tool instead of trying to solve everything itself, and then use the tool's result to answer the user?

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
An LLM using a tool is like a waiter in a restaurant. The waiter takes the customer's order, asks the chef (the external tool) to prepare it, and then delivers the finished dish back to the customer. The waiter coordinates the process but doesn't prepare the dish itself.
```text
Customer → User
Waiter → LLM
Chef/Kitchen → Python tool (calculator)
Dish → Tool result (e.g., 8.75)
```

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Implemented a local calculator function that could perform arithmetic operations independently of the LLM.
2. Defined the calculator's tool schema by describing its purpose, expected arguments, and parameter types so the LLM could understand when and how to use it.
3. Sent the user's question and the registered tool definition to Gemini, allowing the model to decide whether to call the calculator before returning a response.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
interaction = client.interactions.create(
    model=GENAI_MODEL_NAME,
    input="What is (56 * 5)/32?",
    tools=[calculator_function],  # Tool schema defined above
)
```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
An LLM doesn't have to perform every task itself. It can recognize when a specialized tool is better suited for a task, delegate the work, and use the tool's result to respond to the user.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
The concept clicked when I saw Gemini produce a function_call instead of the answer. That made me realize the model wasn't executing my Python code itself. It was requesting my application to run the calculator and return the result, just like a waiter asks the kitchen to prepare a dish before serving it.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
I would define multiple tools and use more complex queries so I could observe how the model decides which tool to call and when it relies on a tool instead of its own capabilities.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How does the model decide which function to call when multiple tools are available? If several tools have overlapping capabilities, what influences its selection, and how are priorities determined?

---

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---
[Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#how-computer-use-works)
[How tool use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)
[Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)

[Week 3](../README.md) | [Root](../../README.md) | [Day 016](../Day-016/)
