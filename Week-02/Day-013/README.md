# Day 013 - Week 2 Buffer and Review

**Week 2 - Buffer** | [Day 012](../Day-012/) | [Week 2](../README.md) | [Root](../../README.md) | [Day 014](../Day-014/)

## Today's Task
---
**Read** (20-30 min): Re-read Day 8-12 learning logs.

**Build** (remainder of ~1 hr): Finish any incomplete Day 8-12 learning log. Answer the weekly quiz cold.

## Deliverable
---
All 5 weekday Learning Logs completed and committed; quiz answers written in this note.

**Note:** Use this buffer - don't carry incomplete logs into Week 3.

## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Verify that I could explain every major Week 2 concept

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->

- **Self-Attention:** A language model understands a sentence by looking at how all the words relate to each other instead of reading every word in isolation. This helps it understand the actual meaning of the sentence.

- **Context Window:** A language model can only consider a limited amount of information at one time. This acts like its working memory while generating a response.

- **Chunking:** Large documents are divided into smaller, meaningful sections so the system can quickly find only the information related to a user's question instead of searching through the entire document.

- **Embeddings and Vector Database:** Each chunk is converted into numbers that capture its meaning and stored in a vector database. When a question is asked, the system searches for chunks with the most similar meaning instead of matching exact words.

- **Retrieval-Augmented Generation (RAG):** Before answering a question, the system first retrieves the most relevant information from the knowledge base and provides it to the language model. This helps the model generate answers based on evidence rather than relying only on what it remembers from training.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->

1. Understood how a language model uses self-attention to understand relationships between words and how the context window limits the amount of information it can process at once.
2. Divided large documents into smaller, meaningful chunks so individual topics could be represented and retrieved more effectively.
3. Converted each chunk into embeddings and stored them in a vector database, creating a searchable knowledge base based on semantic meaning.
4. Converted the user's question into an embedding using the same embedding model and performed a similarity search to retrieve the most relevant chunks.
5. Combined the retrieved context with the user's question and system instructions before sending it to the LLM, allowing it to generate a grounded answer based on the provided evidence.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
Before this week, I didn't even know that the complete workflow was called Retrieval-Augmented Generation (RAG). Looking back, I realized I had already built parts of the same pipeline in previous projects without understanding the underlying concepts or terminology. Week 2 connected those individual pieces into a complete system, helping me understand not just how to build it, but why each component exists and how they work together.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
Instead of focusing only on getting a working RAG pipeline, I would spend more time evaluating the retrieval stage. I would inspect the retrieved chunks, experiment with different chunk sizes, overlaps, and retrieval counts, and validate that the correct evidence reaches the LLM before trying to improve the model's response.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
- How should chunk size and overlap be selected for different types of documents to balance retrieval accuracy and context preservation?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above (at [quiz](quiz.md))
- [x] Learning Log fully written 
- [x] Committed to GitHub

## References
---

[Day 012](../Day-012/) | [Week 2](../README.md) | [Root](../../README.md) | [Day 014](../Day-014/)
