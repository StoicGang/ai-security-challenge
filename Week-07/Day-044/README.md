# Day 044 - NIST AI RMF - Map, Measure, Manage (Light)

**Week 7 - Scoped Task** | [Day 043](../Day-043/) | [Week 7](../README.md) | [Root](../../README.md) | [Day 045](../Day-045/)

## Today's Task
---
**Read** (15 min): NIST AI RMF Playbook - one-paragraph overviews of the other 3 functions only.

**Build** (30 min): Write ONE risk register row for your biggest Week 4 finding: likelihood, impact, mitigation (link to Week 6's fix), residual risk.

## Deliverable
---
This Learning Log with one complete, well-reasoned risk register row - depth on one entry, not a rushed full register.

**Note:** One row done properly is the bar this week. A full multi-row register is a later stretch goal.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
How do I turn a real security finding into a risk decision and apply Map, Measure, and Manage to it?

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
- Map establishes the system, its context, dependencies, stakeholders, and potential impacts. It asks, "What are we dealing with, and who or what could be affected?"
- Measure gathers evidence and evaluates relevant characteristics and risks identified from that context. It asks, "What evidence do we have about how the system actually behaves and how significant these risks are?"
- Manage uses the understanding from Map and the evidence from Measure to prioritize and respond to risks. It asks, "What should we do about this risk, and what residual risk are we willing to accept?"

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Read the NIST RMF overviews for Map, Measure, and Manage.
2. Analyzed the Week 4 indirect prompt-injection finding and compared it with the Week 6 logging fix.
3. Assessed likelihood, impact, mitigation, and residual risk and recorded them in one risk-register row.

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
A capability cannot be understood as a risk in isolation. Its risk depends on what the capability is, why it exists, what it touches, who depends on it, and who could be affected.

I initially considered the French translation behavior an unsuccessful prompt injection because the malicious instruction was not executed. I now understand that the retrieved instruction influencing the model was itself evidence of the vulnerability. The fact that Gemini's built-in behavior rejected the more harmful instruction does not mean the application had implemented a security control against prompt injection.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
when i realised that

```text
Map = context
Measure = evidence
Manage = decision
```

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
I would separate the observed attack behavior from the model's security response earlier, and I would constrain the impact assessment to capabilities actually present in the system instead of assuming hypothetical attack consequences.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How should likelihood be assessed when different stages of the same attack path have different probabilities, especially when one stage is demonstrated but another is currently constrained?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---
[NIST RMF map](https://airc.nist.gov/airmf-resources/playbook/map/)
[NIST RMF measure](https://airc.nist.gov/airmf-resources/playbook/measure/)
[NIST RMF manage](https://airc.nist.gov/airmf-resources/playbook/manage/)

[Day 043](../Day-043/) | [Week 7](../README.md) | [Root](../../README.md) | [Day 045](../Day-045/)
