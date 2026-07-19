# Week 02 - Transformers, Attention and RAG Basics

**Theme:** Self-Attention - Context Windows - Chunking - Vector Databases - Retrieval-Augmented Generation

## Objective
---
Understand - at a conceptual, explainable level - how attention lets a model weigh relevant tokens, what a context window actually limits, and how retrieval augments generation. Use existing tools to see each piece work; do not reimplement a transformer.

## This Week's Challenge
---
By Day 12: a working small RAG query - retrieve the right chunk from your own notes and get a grounded answer from an LLM API call, using ChromaDB plus an API call.

## Week Checklist
---
- [x] Day 1-5 Deliverables all exist exactly as specified in each day's README
- [x] Day 1-5 Learning Logs all fully written (each day's README.md - not code files - is the actual deliverable)
- [x] This Week's Challenge demonstrably met
- [x] Week-02-Learning.md filled in (aggregate reflection)
- [x] Weekly quiz answered cold
- [x] Interview questions practiced out loud
- [x] Day 6 buffer used if anything ran long

---

## Day Breakdown

| Status | Day | Topic | Read Time |
|--------|-----|-------|-----------|
| DONE | [Day 008](Day-008/) | Self-Attention - The Core Idea | 15 min |
| DONE | [Day 009](Day-009/) | Context Windows and Positional Encoding | 15 min |
| DONE | [Day 010](Day-010/) | RAG Concept and Chunking | 15-20 min |
| DONE | [Day 011](Day-011/) | Vector Databases - Storing and Retrieving & Creating Micro usable code | 15 min |
| DONE | [Day 012](Day-012/) | Week 2 Challenge - RAG Q&A | n/a |
| DONE | [Day 013](Day-013/) | Week 2 Buffer and Review | 20-30 min |
| DONE | [Day 014](Day-014/) | Week 2 to Week 3 Handoff | 10 min max |

## Weekly Quiz
---
- [x] Explain attention in 3 sentences without using the word 'context'.
> Attention allows each token to determine which other tokens are most relevant while building its representation. It assigns higher importance to tokens that contribute more to understanding the current token. This is like a selective approach where model captures the relationships and generate more accurate representation.
- [x] Why does a vector DB return approximate, not exact, nearest neighbours?
>Vector databases return approximate rather than exact. Nearest neighbors because comparing a query against every embedding becomes computationally heavy when database grows. Instead they use indexing algorithm to search only relevant regions in the vector space.

## Interview Questions
---
[Learning Log](./Week-02-Learning.md)

## A Note on Scope
---
Every day this week is scoped to ~1 hour total - one specific named resource with a real time estimate, and a build task using existing/industry-standard libraries first. From-scratch reimplementation of any concept is a stretch goal for later, not this week's bar. This mirrors the correction made after Week 1, Day 2, when "read a chapter" and "build from scratch" proved unachievable in the available time.

## References
---
[Week-02-Learning.md](Week-02-Learning.md) | [Week 01](../Week-01/) | [Root](../README.md) | [Week 03](../Week-03/)
