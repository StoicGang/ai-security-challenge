# Day 047 - Week 7 Challenge - AI Audit Summary

**Week 7 - Scoped Task** | [Day 046](../Day-046/) | [Week 7](../README.md) | [Root](../../README.md) | [Day 048](../Day-048/)

## Today's Task
---
**Read** (-): None - integration day.

**Build** (30-40 min): Combine Day 44's risk register row plus Day 46's system card plus a one-line reference to NIST AI RMF into a single one-page summary.

## Deliverable
---
ai-audit-summary.md - this is the Week 7 Challenge.

**Note:** -

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
The challenge was to understand the different purposes of the system card and risk register, then combine their relevant information into a single audit summary that connects system context, identified risk, risk assessment, and governance context.

### Key Concept
A system card describes the system, its intended behavior, and known risks, while a risk register assesses a specific risk in the context of the current deployment. Combining them into an audit summary connects what the system is with how a particular risk is currently assessed and managed.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Reviewed the Day 44 risk register and identified the relevant retrieved-content instruction-injection risk and its current assessment.
2. Reviewed the Day 46 system card to connect the risk with the RAG system's intended use, architecture, and operating context.
3. Combined the relevant information into a one-page audit summary and added NIST AI RMF as an external risk-management framework reference.

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
The key learning was that the existence of a risk and its assessed risk level are different things. A system can have a known security risk while its current likelihood and impact remain low because of the specific deployment, attack surface, and available controls.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
The ah-ha moment was realizing that retrieved content does not need to perform a dangerous action to demonstrate the underlying security issue.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
I would avoid treating an experimental environment as the primary reason for a low risk rating and instead document the concrete attack paths, system capabilities, and controls that support the assessment.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How should the likelihood and impact of retrieved-content instruction injection be reassessed when the retrieval corpus becomes externally supplied, user-controlled, or dynamically updated?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---

[Day 046](../Day-046/) | [Week 7](../README.md) | [Root](../../README.md) | [Day 048](../Day-048/)
