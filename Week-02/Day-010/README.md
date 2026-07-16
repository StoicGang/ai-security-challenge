# Day 010 - RAG Concept and Chunking

**Week 2 - Scoped Task** | [Day 009](../Day-009/) | [Week 2](../README.md) | [Root](../../README.md) | [Day 011](../Day-011/)

## Today's Task
---
**Read** (15-20 min): Pinecone or LangChain's 'chunking strategies' doc - one section only on fixed-size chunking with overlap.

**Build** (30 min): Split ONE of your TryHackMe writeups into chunks using a simple Python loop (fixed-size, with overlap) - no chunking library required.

## Deliverable
---
This Learning Log with the list of chunks and their character counts logged.

**Note:** Plain Python string slicing is enough. A dedicated chunking library is a later stretch goal.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Breaking a large document into smaller retrievable units so the relevant section can later be found and passed to the model.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
1. A chunk is a smaller unit of the original document that can later be processed or retrieved independently.
2. Chunk overlap means next chunk start before the previous chunk completely ends.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Read the article.md file and stored its content as a Python string.
2. Defined a fixed chunk size of 1,000 characters with a 200-character overlap and calculated the step size.
3. Used Python string slicing to create the chunks, store them in a list, and print each chunk with its character count.

### Code Snippet 
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
for i in range (0, Document_size, step_size):
    chunk = document[i:i + chunk_size]
    chunks.append(chunk)

for i in chunks:
    print("Chunk: ", i)
    print("Character Count:", len(i))
```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
- Even if the entire document fits inside the context window, chunking can still improve retrieval by providing only the relevant information. This leaves context space for instructions, conversation history, and other retrieved information while reducing unrelated content that may distract the model.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
I understood that the 200-character overlap intentionally duplicates text so that an explanation split at a fixed-size boundary can still retain its surrounding context in the next chunk.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
If I repeated this task, I would compare fixed-size character chunking with a method that respects sentence or paragraph boundaries. The current approach can split words and explanations at arbitrary positions, even though overlap helps preserve some of the lost context.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How do we choose the right chunk size and overlap for different types of documents, and what trade-offs occur when the overlap is too small or too large?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

References 
---
[Pinecone chunking Strategies](https://www.pinecone.io/learn/chunking-strategies/)
[Lost in the Middle](https://arxiv.org/pdf/2307.03172)

[Day 009](../Day-009/) | [Week 2](../README.md) | [Root](../../README.md) | [Day 011](../Day-011/)
