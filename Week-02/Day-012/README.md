# Day 012 - Week 2 Challenge - RAG Q&A

**Week 2 - Scoped Task** | [Day 011](../Day-011/) | [Week 2](../README.md) | [Root](../../README.md) | [Day 013](../Day-013/)

## Today's Task
---
**Read** (-): None - integration day.

**Build** (45-60 min): Wire Day 11's retrieval to one LLM API call (Claude API or OpenAI API). Ask a real question about your TryHackMe notes. Retrieve the top chunk, pass it to the LLM, get a grounded answer.

## Deliverable
---

This Learning Log with one full Q&A pair documented: the question, the retrieved chunk, and the final grounded answer - proof the RAG chain works end to end.

**Note:** This is the Week 2 Challenge. A full production RAG pipeline with re-ranking is a later stretch goal.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Build an end-to-end Retrieval-Augmented Generation (RAG) pipeline by connecting semantic retrieval from a vector database with an LLM, so the model answers questions using my TryHackMe notes instead of relying on its own knowledge.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
A Retrieval-Augmented Generation (RAG) pipeline combines two separate systems. The retrieval system first searches a knowledge base and finds the most relevant information for a question. That retrieved information is then given to the Large Language Model as evidence. Instead of searching for information itself, the LLM's job is only to understand the provided context and generate a clear, natural-language answer from it.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->

1. Read my existing TryHackMe notes and split them into reusable text chunks.
2. Generated embeddings for each chunk and stored them in a ChromaDB collection.
3. Converted the user's question into an embedding and retrieved the most semantically relevant chunk.
4. Built a prompt containing the retrieved context, the user's question, and clear instructions for the LLM to answer only from the provided evidence.
5. Sent the prompt to the Gemini API and generated a grounded answer.
6. Printed the original question, retrieved context, and final answer to verify the complete RAG pipeline worked end to end.

```text
Documents
     │
     ▼
Chunking
     │
     ▼
Embeddings
     │
     ▼
Vector Database
     │
User Question
     │
     ▼
Query Embedding
     │
     ▼
Similarity Search
     │
Retrieved Chunks (Evidence)
     │
     ▼
Prompt
     │
Instructions + Evidence + Question
     │
     ▼
LLM
     │
Grounded Answer
```

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
context = "\n\n".join(retrieved_chunks)

response = client.models.generate_content(
    model=GENAI_MODEL_NAME,
    contents=f"""
    Context:
    {context}

    Question:
    {query}

    Answer using only the provided context.
    """,
)

print(response.text)
```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
The retriever and the LLM have different responsibilities. The retriever's job is to find the most relevant information, while the LLM's job is to understand that retrieved evidence and generate a clear answer. The LLM doesn't search for the information itself; it reasons over the context it is given.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
The pipeline finally clicked when I realized the LLM is like a knowledgeable teacher taking an open-book exam. The retriever hands it the correct page from the book, and the LLM's only job is to read, understand, and explain it instead of searching the entire library itself.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
I would test the LLM API with a minimal standalone script before integrating it into the RAG pipeline. That would have isolated the configuration issues much earlier.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How does a RAG system decide how many chunks to retrieve, and how does retrieving too many or too few chunks affect the quality of the final answer?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---

[Day 011](../Day-011/) | [Week 2](../README.md) | [Root](../../README.md) | [Day 013](../Day-013/)
