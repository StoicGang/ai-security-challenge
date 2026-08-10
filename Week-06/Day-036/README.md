# Day 036 - STRIDE for AI - Light Mapping

**Week 6 - Scoped Task** | [Week 6](../README.md) | [Root](../../README.md) | [Day 037](../Day-037/)

## Today's Task
---
**Read** (0-10 min): No new reading required if STRIDE is already familiar - otherwise a 10-minute refresher on the 6 categories.

**Build** (30 min): List your Week 3 agent's 3 main components (agent loop, tool registry, file-read tool). Assign at least one STRIDE threat category to each.

## Deliverable
---
This Learning Log with a markdown table, 3 rows: component, STRIDE category, one-sentence threat description.

**Note:** 3 components is the bar this week - a full 6-component table is a later stretch goal.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Today's task was to identify the main components of the Week 3 AI agent and map each component to a relevant STRIDE threat. The goal was to understand how an attacker could exploit each component and which security boundary or security property would be violated.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
We mapped each agent component to a STRIDE category by looking at what an attacker could manipulate or abuse and which security property or boundary would be violated.

| Component      | STRIDE Category        | Security Principle | Threat Description                                                                                                         |
| -------------- | ---------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Agent loop     | Tampering              | Integrity          | Attacker manipulates trusted instructions or control flow, causing the agent to execute an unintended action.              |
| Tool registry  | Elevation of Privilege | Authorization      | Attacker causes an unauthorized capability to become available to the agent through the tool registry.                     |
| File-read tool | Elevation of Privilege | Authorization      | Without the hardcoded filename restriction, an attacker could cause the tool to access files outside its authorized scope. |


### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Identified the three core components of the Week 3 agent: the agent loop, tool registry, and file-read tool.
2. Examined what each component could be manipulated to do and which security principle or boundary could be violated.
3. Mapped the violated security principle to the relevant STRIDE category and tested my understanding through attack scenarios.

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
A component can have multiple STRIDE categories depending on what the attacker is trying to achieve and which security property or boundary is being violated. A component does not have one permanently fixed STRIDE category; the attack path, violated security principle, and resulting security impact determine which category is most appropriate.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
When breaking an attack into different phases, I realized that different STRIDE categories can apply at different points in the attack path. The same scenario can involve unauthorized access as Elevation of Privilege and the subsequent exposure of sensitive data as Information Disclosure, so the category depends on what security property is being violated at that stage.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
I would continue using the same approach: first identify the components and their security boundaries, then determine what an attacker could achieve or manipulate, identify the violated security principle, and finally map it to the appropriate STRIDE category.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
When an attack violates multiple security properties across different stages of the same attack path, how should the primary STRIDE category be selected for a component?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---

[Week 6](../README.md) | [Root](../../README.md) | [Day 037](../Day-037/)
