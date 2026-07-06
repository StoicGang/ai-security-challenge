# Day 004 - Embeddings - What a Vector Actually Captures

**Week 1 - Corrected Scope** | [Day 003](../Day-003/) | [Week 1](../README.md) | [Root](../../README.md) | [Day 005](../Day-005/)

---

## Today's Task

**Read** (15 min): Jay Alammar - 'The Illustrated Word2Vec' - first 3 diagrams/sections only, not the full article.

**Build** (30-40 min): Install sentence-transformers (pip install sentence-transformers). Embed 5 sentences you write yourself (2 similar in meaning, 3 unrelated). Compute cosine similarity between pairs using sklearn.metrics.pairwise.cosine_similarity.

## Deliverable
> This is the specific, measurable output that must exist before the day is done.

This Learning Log with the cosine similarity scores for at least 2 sentence pairs (1 similar, 1 unrelated) recorded and compared.

**Note:** No NumPy-from-scratch embedding math this week. Use the library, observe what similarity scores look like for similar vs. unrelated sentences.

---

## Learning Log
> Fill in after completing the day. This markdown file — not a code file — is the actual deliverable. A code snippet can illustrate a point, but the writing is what proves understanding.

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
To understand how sentence embeddings convert text into numerical vectors that capture semantic meaning, and how cosine similarity can be used to compare the meanings of different sentences. 

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
1. A sentence embedding is a numerical representation of a sentence that captures its overall meaning rather than the exact words used. Sentences with similar meanings are placed closer together in a high-dimensional space, allowing us to compare meaning using cosine similarity instead of comparing words one by one.
2. Skip-Gram and Negative Sampling are training techniques used in Word2Vec to learn word embeddings. They provide historical context but are not the primary concept of today's exercise.


### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1.
2.
3.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
embeddings = model.encode(sentences) similar = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0] unrelated = cosine_similarity([embeddings[0]], [embeddings[4]])[0][0] print(similar) print(unrelated)
```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
Embeddings do not store words or predict the next word. They represent the overall meaning of a sentence as a numerical vector. Cosine similarity allows us to measure how similar two meanings are, even when the wording is different.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
The concept clicked when I realized that embeddings are not probabilities or next-word predictions. They act more like coordinates in a semantic space, where sentences expressing similar ideas are located closer together even if they use different vocabulary.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
Before computing cosine similarity, I would first predict which sentence pairs should be the most similar.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
1. How are sentence embedding models trained?
2. Why don't individual dimensions of an embedding have a clear human-readable meaning?
3. How are embeddings stored and searched efficiently in vector databases?

---

## Day Checklist
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

---

[Day 003](../Day-003/) | [Week 1](../README.md) | [Root](../../README.md) | [Day 005](../Day-005/)
