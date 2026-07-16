# Day 011 - Vector Databases - Storing and Retrieving

**Week 2 - Scoped Task** | [Day 010](../Day-010/) | [Week 2](../README.md) | [Root](../../README.md) | [Day 012](../Day-012/)

## Today's Task
---
**Read** (15 min): ChromaDB official 'Getting Started' quickstart - just the first code example, not the whole quickstart.

**Build** (30-40 min): Install chromadb. Store Day 10's chunks as embeddings (reuse sentence-transformers from Week 1). Run ONE test query. Print the top-2 results with similarity scores.

## Deliverable
---

This Learning Log with the query used and its top-2 results (with scores) recorded.

**Note:** One query is enough to prove retrieval works. More test queries can wait for Day 12.

## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Store document embeddings in a vector database and retrieve the most relevant chunks for a natural language query instead of comparing every embedding manually.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
1. Vector database: A database designed to store embeddings and retrieve vectors that are close to a query vector. a vector database does not necessarily store vectors "in semantic order."
Analogy: instead of searching a library by exact book title, ask for books closest in topic.
2. Collection: The collection groups the chunk records that ChromaDB searches during retrieval. 
Analogy: one labelled drawer in a filing cabinet.
3. Document, embedding, and ID relationship: The chunk is the actual text, the embedding is its numerical semantic representation, and the ID uniquely identifies the stored item.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Read the document and split it into fixed-size chunks.
2. Generate one embedding for each chunk using the same embedding model.
3. Assign a unique ID to every chunk so each document, embedding, and ID form a single record.
4. Store the chunk records inside a ChromaDB collection.
5. Convert the user's query into an embedding using the same embedding model.
6. Search the collection for the two nearest embeddings and return their associated document chunks with similarity scores.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
results = query_collection(
    collection=collection,
    query_embedding=query_embedding,
    n_results=2
)

documents = results["documents"][0]
distances = results["distances"][0]
```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
1. I now understand that semantic understanding and retrieval are two separate responsibilities. The embedding model determines which pieces of text are semantically close by generating their vector representations, while the vector database efficiently stores those vectors and retrieves the nearest ones within the selected collection.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
- The idea clicked when I realized that ChromaDB never understands the document's meaning. It simply retrieves the nearest vectors, while the embedding model is entirely responsible for placing semantically related chunks close together in vector space. 
- The second realization was that the chunking, embedding, and vector database logic had become reusable building blocks, leading me to organize them into a shared [common](../../common/) directory for future RAG implementations.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
I would design reusable components as soon as I notice the same logic appearing across multiple days. Instead of keeping chunking, embedding generation, and vector database operations inside a single script, I would organize them into shared modules earlier. This keeps each day's implementation focused on the new concept while making the codebase easier to extend.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How do different vector databases (such as ChromaDB, FAISS, Pinecone, and Qdrant) differ in the way they store, index, and retrieve embeddings?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---
[Cromadb core](https://cookbook.chromadb.dev/core/)
[Getting started with cromadb](https://docs.trychroma.com/docs/overview/getting-started?utm_source=chatgpt.com)

[Day 010](../Day-010/) | [Week 2](../README.md) | [Root](../../README.md) | [Day 012](../Day-012/)
