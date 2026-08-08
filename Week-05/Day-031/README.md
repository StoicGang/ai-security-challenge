# Day 031 - Poisoning Impact - Hands-On

**Week 5 - Scoped Task** | [Day 030](../Day-030/) | [Week 5](../README.md) | [Root](../../README.md) | [Day 032](../Day-032/)

## Today's Task
---
**Read** (-): None - build day.

**Build** (30-40 min): Ask your Week 2 RAG app ONE question that touches the planted fact - before and after adding it to the corpus. Compare the two answers.

## Deliverable

This Learning Log with a table: question, answer before, answer after, what changed and why.

**Note:** One question is enough to observe the effect clearly.

## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
The goal was to observe how poisoning a RAG corpus changes the generated answer by asking the same question before and after introducing a poisoned document into the knowledge base, while keeping the retrieval pipeline and model unchanged.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
A RAG system does not learn from the documents it retrieves at runtime. Instead, it searches the indexed corpus for relevant information and provides the retrieved content to the LLM as context. If the retrieved content is poisoned, the model may generate a different answer because it trusts the provided context, even though the model's own parameters have not changed. This makes data poisoning in RAG a retrieval-layer attack rather than a model poisoning attack.


### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Refactored the Week 2 RAG pipeline into a reusable function that accepts a document path and a user query.
2. Created two corpus states using a clean document and a poisoned document containing a planted fact.
3. Ran the same query against both corpus states using the same RAG pipeline.
4. Compared the retrieved context and generated answers to observe how the poisoned corpus influenced the response.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
clean_result = run_rag(
    document_path=clean_document,
    query=query,
)

poisoned_result = run_rag(
    document_path=poisoned_document,
    query=query,
)
```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
A RAG system can produce misleading answers without changing the model itself. Simply retrieving poisoned context was enough to influence the generated response. The experiment also showed that the final answer may contain a mix of correct and incorrect information because the retrieved context itself contained both.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
The important realization was that the LLM did not invent the false information. It simply trusted the retrieved context. Once the poisoned chunk became part of the retrieval results, the generated answer reflected that misinformation while still preserving some surrounding correct facts.
> **Note**: The complete experiment output, including the retrieved context and generated answers before and after poisoning, is documented in [experiment](experiment.md).

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
If I repeated this exercise, I would first verify that the complete RAG pipeline, API access, and external dependencies were working before designing the experiment around them.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How much poisoning is actually required to influence retrieval and the final answer?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---

[Day 030](../Day-030/) | [Week 5](../README.md) | [Root](../../README.md) | [Day 032](../Day-032/)
