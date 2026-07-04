# Day 003 — Tokenization — What a Token Actually Is

**Week 1** · 🔧 Corrected Scope · [← Day 002](../Day-002/) · [🏠 Week 1](../README.md) · [📁 Root](../../README.md) · [Day 004 →](../Day-004/)

---

## Today's Task

**Read** (15–20 min): Hugging Face — 'Byte-Pair Encoding tokenization' conceptual page. **This one page only** — not the API reference.

**Build** (30–40 min): Install `tiktoken` (`pip install tiktoken`). Tokenize 3 sentences you write yourself. Print the tokens and their IDs. Count: does a 10-word sentence produce more or fewer than 10 tokens? Why?

**Note:** No custom tokenizer this week. Use the library, observe the behavior, understand the concept. Building BPE from scratch is a stretch goal for later, once the concept is solid.

---

## Learning Log
> Fill in after completing the day. This markdown file — not a code file — is the actual deliverable. A code snippet can illustrate a point, but the writing is what proves understanding.


### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Understand what a token actually is and determine whether tokens are the same as words.


### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
1. Training tokenizer is just like writing a dictionary of words. Whereas using a tokenizer is something like using dictionary to find out specific word from that.
2. A token is a unit from the tokenizer's vocabulary used to represent text. A token may be a whole word, part of a word, punctuation, or even part of an emoji. Each token is mapped to an integer ID before being sent to the model.
3. The tokenizer may treat punctuation as separate tokens because they are reusable across many different words and sentences.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Read about Byte Pair Encoding (BPE) and realized I was missing the motivation behind tokenization.
2. Used the tiktoken library to tokenize multiple custom sentences.
3. Compared words, token IDs, and token counts to observe tokenizer behavior.
4. Experimented with punctuation and emojis to understand how they are represented.

### Code Snippet (if relevant)
<!-- 5–10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
encoded = encoding.encode(sentence)
print(encoded)
print(len(encoded))
```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
GPT cannot operate directly on human-readable text because neural networks perform computations on numerical representations. The tokenizer converts text into a sequence of token IDs while preserving the original text, allowing the model to process it mathematically.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
Seeing that an emoji produced multiple token IDs and that punctuation was tokenized separately made me realize that tokenization is based on the tokenizer's vocabulary, not on human notions of words.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
Reading about the algorithm without understanding the underlying problem made the concepts much harder to follow.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
1. How does BPE decide the final vocabulary size?
2. How are token IDs converted into embeddings?

---

## Day Checklist
- [x] Reading done (within time box — don't let one resource eat the whole day)
- [x] Build complete
- [x] Learning Log fully written (all 8 sections — this .md file IS the deliverable)
- [x] Committed to GitHub

---

[← Day 002](../Day-002/) · [🏠 Week 1](../README.md) · [📁 Root](../../README.md) · [Day 004 →](../Day-004/)
