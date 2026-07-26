# Week 03 - AI Agents and Tool Calling

**Theme:** Function Calling - The Agent Loop - MCP Awareness - Tool Scoping - Least Privilege

---

## Objective
Understand what makes an agent different from a single LLM call - the ability to take actions via tools - and why that expanded capability is the core of agentic AI risk. Use existing SDK features, not a custom framework.

## This Week's Challenge
By Day 19: a single working agent that decides between two tools based on the user's request, with every tool call logged.

---

## Week Checklist
- [x] Day 1-5 Deliverables all exist exactly as specified in each day's README
- [x] Day 1-5 Learning Logs all fully written (each day's README.md - not code files - is the actual deliverable)
- [x] This Week's Challenge demonstrably met
- [x] Week-03-Learning.md filled in (aggregate reflection)
- [x] Weekly quiz answered cold
- [x] Interview questions practiced out loud
- [x] Day 6 buffer used if anything ran long

---

## Day Breakdown

| Status | Day | Topic | Read Time |
|--------|-----|-------|-----------|
| DONE | [Day 015](Day-015/) | Function and Tool Calling Basics | 15-20 min |
| DONE | [Day 016](Day-016/) | The Agent Loop - Plan, Act, Observe | 15 min |
| DONE | [Day 017](Day-017/) | MCP Awareness | 10-15 min |
| DONE | [Day 018](Day-018/) | Tool Scoping and Least Privilege | 0-10 min |
| DONE | [Day 019](Day-019/) | Week 3 Challenge - Two-Tool Agent | n/a |
| DONE | [Day 020](Day-020/) | Week 3 Buffer and Review | 20-30 min |
| DONE | [Day 021](Day-021/) | Week 3 to Week 4 Handoff | 10 min |

---

## Weekly Quiz

- [x] Draw the agent loop from memory - what are the 3 phases and what happens at each?
```Mermaid
flowchart LR
    A[User Request] --> B[Plan]
    B -->|Decide whether a tool is needed| C[Act]
    C -->|Invoke Calculator / Date-Time / File Tool| D[Observe]
    D -->|Receive tool output| B
    B -->|Enough information?| E[Final Response]
```

- [x] Name two ways an agent's tool access could be abused that have nothing to do with jailbreaking the model.
1. An agent is given a file-reading tool that can access an entire directory instead of a single approved file.
2. An agent is connected to a tool that can send emails, delete files, or execute shell commands without proper authorization checks.

## Interview Questions
- What is the practical difference between a tool call and a function call?
- Why is an over-scoped tool a security issue even if the model usually behaves correctly?
- What problem does MCP solve that ad-hoc tool integration does not?

---

## A Note on Scope
Every day this week is scoped to ~1 hour total - one specific named resource with a real time estimate, and a build task using existing/industry-standard libraries first. From-scratch reimplementation of any concept is a stretch goal for later, not this week's bar. This mirrors the correction made after Week 1, Day 2, when "read a chapter" and "build from scratch" proved unachievable in the available time.

---

[Week-03-Learning.md](Week-03-Learning.md) | [Week 02](../Week-02/) | [Root](../README.md) | [Week 04](../Week-04/)
