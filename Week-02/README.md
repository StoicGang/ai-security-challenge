# Week 02 - Transformers, Attention and RAG Basics

**Theme:** Self-Attention - Context Windows - Chunking - Vector Databases - Retrieval-Augmented Generation

---

## Objective
Understand - at a conceptual, explainable level - how attention lets a model weigh relevant tokens, what a context window actually limits, and how retrieval augments generation. Use existing tools to see each piece work; do not reimplement a transformer.

## This Week's Challenge
By Day 12: a working small RAG query - retrieve the right chunk from your own notes and get a grounded answer from an LLM API call, using ChromaDB plus an API call.

---

## Week Checklist
- [ ] Day 1-5 Deliverables all exist exactly as specified in each day's README
- [ ] Day 1-5 Learning Logs all fully written (each day's README.md - not code files - is the actual deliverable)
- [ ] This Week's Challenge demonstrably met
- [ ] Week-02-Learning.md filled in (aggregate reflection)
- [ ] Weekly quiz answered cold
- [ ] Interview questions practiced out loud
- [ ] Day 6 buffer used if anything ran long

---

## Day Breakdown

| Status | Day | Topic | Read Time |
|--------|-----|-------|-----------|
| TODO | [Day 008](Day-008/) | Self-Attention - The Core Idea | 15 min |
| TODO | [Day 009](Day-009/) | Context Windows and Positional Encoding | 15 min |
| TODO | [Day 010](Day-010/) | RAG Concept and Chunking | 15-20 min |
| TODO | [Day 011](Day-011/) | Vector Databases - Storing and Retrieving | 15 min |
| TODO | [Day 012](Day-012/) | Week 2 Challenge - RAG Q&A | n/a |
| TODO | [Day 013](Day-013/) | Week 2 Buffer and Review | 20-30 min |
| TODO | [Day 014](Day-014/) | Week 2 to Week 3 Handoff | 10 min max |

---

## Weekly Quiz
- [ ] Explain attention in 3 sentences without using the word 'context'.
- [ ] Why does a vector DB return approximate, not exact, nearest neighbours?

## Interview Questions
- What is the difference between fine-tuning and RAG, and when would you choose one over the other for a security-sensitive application?
- How does chunk size affect both answer quality and retrieval security?
- What happens to context once it exceeds the context window?

---

## A Note on Scope
Every day this week is scoped to ~1 hour total - one specific named resource with a real time estimate, and a build task using existing/industry-standard libraries first. From-scratch reimplementation of any concept is a stretch goal for later, not this week's bar. This mirrors the correction made after Week 1, Day 2, when "read a chapter" and "build from scratch" proved unachievable in the available time.

---

[Week-02-Learning.md](Week-02-Learning.md) | [Week 01](../Week-01/) | [Root](../README.md) | [Week 03](../Week-03/)
