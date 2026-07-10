# Week 1 Learning — AI Foundations

## Pipeline
---
```text
ser Text -> Tokenizer -> Token IDs -> Embedding Model -> Embeddings -> Cosine Similarity -> Most Relevant Document
```

## Core Concepts
---
### Loss Function

A loss function measures how far a model's predictions are from the correct answers. During training, the model tries to minimize this value so that its predictions become more accurate.

### Gradient Descent

Gradient descent is an optimization algorithm that updates a model's parameters in the direction that reduces the loss. It repeatedly follows the slope of the loss function until the model reaches a better solution.

### Tokenization

Tokenization converts human-readable text into tokens from a predefined vocabulary and maps them to numerical token IDs. These IDs are the numerical representation that language models process.

> **Remember:** A token is not necessarily a word. It can represent a whole word, part of a word, punctuation, or even part of an emoji.

### Embeddings

An embedding is a learned numerical vector that represents the semantic meaning of text. Instead of comparing exact words, embeddings allow a model to compare meanings mathematically using measures such as cosine similarity.

> **Remember:** Token IDs identify a token. Embeddings represent its meaning.

## Understanding Check
---
### 1. What is the difference between a token and a word?

A word is a human language concept. A token is an element from the tokenizer's vocabulary. A token may represent a complete word, part of a word, punctuation, or even part of an emoji. Language models process tokens, not words.

### 2. Why can't we compute cosine similarity on token IDs?

Token IDs are arbitrary numerical identifiers assigned by the tokenizer. They contain no semantic information. Cosine similarity is meaningful only on embeddings because embeddings are learned vectors whose geometry reflects semantic relationships.

### 3. Why must the same embedding model be used for both documents and queries?

Different embedding models learn different semantic spaces. Even if two models produce vectors of the same dimension, their vector spaces are incompatible. Similarity comparisons are only meaningful when both documents and queries are embedded using the same model.

### 4. Why is semantic search better than keyword search?

Keyword search compares exact words and may miss relevant documents that use different wording. Semantic search compares the meaning of documents and queries through embeddings, allowing it to retrieve relevant information even when the vocabulary differs.

### 5. How does the semantic retrieval pipeline work?

The user's text is tokenized into token IDs. These token IDs are converted into embeddings by an embedding model. The query embedding is then compared with the stored document embeddings using cosine similarity, and the document with the highest similarity score is retrieved.

## Mental Models

| Concept          | Mental Model                                                                          |
| ---------------- | ------------------------------------------------------------------------------------- |
| Gradient Descent | Walking downhill until reaching the lowest point.                                     |
| Tokenization     | Looking up words using a predefined dictionary (token vocabulary).                    |
| Embeddings       | GPS coordinates representing meaning instead of location.                             |
| Semantic Search  | A librarian recommending books based on meaning rather than exact title words.        |
| Attention        | A reader deciding which earlier words matter most for understanding the current word. |

## Biggest Takeaway

Week 1 taught me that modern AI systems are a pipeline rather than only a collection of an algorithms. Text is tokenized, converted into embeddings, and compared semantically to retrieve relevant information. Understanding this pipeline is far more valuable than memorizing library APIs because every later topic builds upon these foundational ideas.