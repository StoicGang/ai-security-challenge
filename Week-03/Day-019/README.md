# Day 019 - Week 3 Challenge - Two-Tool Agent

**Week 3 - Scoped Task** | [Day 018](../Day-018/) | [Week 3](../README.md) | [Root](../../README.md) | [Day 020](../Day-020/)

## Today's Task

**Read** (-): None - integration day.

**Build** (45-60 min): Combine both tools (calculator plus scoped file-read) into one small agent that decides which tool to use based on the question. Test with 2 different questions.

## Deliverable
---

This Learning Log with both test runs logged - proof the agent correctly routes between tools based on intent.

**Note:** This is the Week 3 Challenge. Multi-agent orchestration is a later stretch goal.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Combine the previously built calculator and scoped file-reading tools into a single agent and verify that it chooses the correct tool based on the user's question.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
An AI agent can have access to multiple tools, but it should choose only the one that matches the user's intent. The application executes the selected tool, while the model decides which tool to use.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
user_query = input("Ask a question: ") 
interaction = client.interactions.create( 
    model=GENAI_MODEL_NAME, 
    input=user_query, 
    tools=ALL_TOOLS, 
)
```
>Note: check [test-results](test_results.md) for detailed results

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
The language model determines which tool to call based on the user's intent, while the application is responsible for executing the requested tool and returning its result.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
I would improve the test logging so that each tool invocation and its result are recorded more clearly, making it easier to verify the agent's routing behavior.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
What happens if two tools have very similar descriptions?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---

[Day 018](../Day-018/) | [Week 3](../README.md) | [Root](../../README.md) | [Day 020](../Day-020/)
