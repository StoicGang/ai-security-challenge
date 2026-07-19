# Week 2 Learning — Retrieval-Augmented Generation (RAG)

## Pipeline

---

```text
User Question
      ↓
Chunk Query
      ↓
Embedding Model
      ↓
Vector Database
      ↓
Nearest Neighbor Search
      ↓
Retrieved Context
      ↓
LLM
      ↓
Grounded Answer
```

## Core Concepts

---

### Self-Attention

Self-attention allows every token in a sequence to determine which other tokens are most relevant when building its representation. Instead of treating every earlier token equally, the model learns to focus more on information that contributes to understanding the current token.

### Context Window

The context window is the maximum number of tokens an LLM can process in a single request. Any information outside this window is invisible to the model during generation.

> **Remember:** The context window limits what the model can see, not what it has learned during training.

### Retrieval-Augmented Generation (RAG)

RAG improves an LLM by retrieving relevant external information before generating a response. Rather than relying only on its internal knowledge, the model answers using the retrieved context.

### Chunking

Chunking divides large documents into smaller overlapping pieces so they can fit within an embedding model and be retrieved efficiently. Overlap helps preserve context that spans chunk boundaries.

> **Remember:** Good chunking preserves meaning while remaining small enough for accurate retrieval.

### Vector Database

A vector database stores embeddings and efficiently retrieves the vectors that are most similar to a query embedding using nearest-neighbor search.

### Grounded Generation

Grounded generation means the LLM generates its response using the retrieved context instead of relying solely on memorized knowledge. This helps reduce hallucinations and produces answers supported by evidence.

### Function Calling (Introduction)

Function Calling allows an LLM to recognize when another tool is better suited for a task and request that tool instead of attempting to perform the action itself. The application remains responsible for executing the requested function.

> **Remember:** The model decides **what** tool to use; the application decides **whether** to execute it.

## Understanding Check

---

### 1. Why is the query compared with the key instead of the value when calculating attention scores?

The query is compared with the key because their purpose is to measure how relevant one token is to another. The key represents what information a token can offer, while the query represents what the current token is looking for. Once attention scores identify the most relevant tokens, those scores are applied to the value vectors, which contain the information to be combined. Separating matching (Query-Key) from information transfer (Value) allows the model to learn specialized representations for each task and compute attention efficiently.

### 2. What happens when the total input exceeds an LLM's context window?

An LLM can only process tokens that fit within its context window. Any tokens beyond this limit are invisible to the model and therefore cannot influence its response. If important instructions or information fall outside the context window, the model may produce incomplete or incorrect answers. RAG addresses this limitation by retrieving only the most relevant document chunks and supplying them as context, allowing the model to focus on the information needed for the current query without processing the entire document.

### 3. Why do we split documents into chunks instead of embedding an entire document as one vector?

Documents are split into chunks because a single embedding represents the overall meaning of the entire document. If a document contains many different topics, its embedding becomes too broad, making it harder to retrieve the specific information needed for a query. By embedding smaller, focused chunks, each vector captures a more precise semantic meaning, allowing the retriever to identify and return only the most relevant sections. This improves retrieval accuracy and provides the LLM with concise, relevant context instead of an entire document.

### 4. How does chunk size affect both answer quality and retrieval security?
Chunk size directly affects both retrieval quality and security. Smaller chunks are more focused, improving retrieval precision and reducing the chance of irrelevant or malicious content being included, but they may omit important surrounding information. Larger chunks preserve more context and can improve answer completeness, but they increase the risk of retrieving unnecessary or adversarial content, consume more of the context window, and reduce retrieval precision. Choosing an appropriate chunk size is therefore a trade-off between accuracy, completeness, efficiency, and security.

### 5. Why does RAG retrieve relevant context before asking the LLM to generate an answer?

RAG retrieves relevant context before generation so that the LLM bases its response on external information rather than relying only on its internal knowledge. Without retrieval, the model may answer from memory, produce outdated information, or generate unsupported details. By supplying the most relevant document chunks as context, RAG grounds the model's response in evidence, making the answer more accurate, relevant, and less likely to hallucinate.

### 6. What is the conceptual difference between a RAG pipeline and an AI agent?

A RAG pipeline follows a fixed sequence: retrieve relevant information and provide it to the LLM to generate a grounded response. It cannot decide to perform different actions based on the user's goal. An AI agent, however, can reason about the task, choose appropriate tools, perform multiple actions when necessary, and use the results of those actions before generating a final response. In short, RAG answers questions using retrieved knowledge, while an agent decides how to accomplish a goal.

## Mental Models

| Concept          | Mental Model                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------ |
| Self-Attention   | A reader highlighting the most important words in a paragraph before answering a question.             |
| Context Window   | A desk that can hold only a limited number of pages at one time.                                       |
| Chunking         | Splitting a large book into organized chapters while keeping a few overlapping pages between chapters. |
| RAG              | A student opening a textbook before answering an exam question instead of relying only on memory.      |
| Vector Database  | A library catalog that quickly finds the most similar books instead of checking every shelf.           |
| Function Calling | Asking a specialist to perform a task instead of trying to do every job yourself.                      |

## Biggest Takeaway

Week 2 taught me that building reliable AI systems is not just about prompting an LLM. Retrieval, chunking, vector databases, and grounded generation work together to provide accurate context before the model responds. I also learned that LLMs should reason about when to use external tools rather than attempting every task themselves, providing the conceptual bridge from RAG systems to AI agents in Week 3.
