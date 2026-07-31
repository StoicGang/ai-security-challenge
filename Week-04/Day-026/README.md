# Day 026 - Week 4 Challenge - Red-Team Notes

**Week 4 - Scoped Task** | [Day 025](../Day-025/) | [Week 4](../README.md) | [Root](../../README.md) | [Day 027](../Day-027/)

## Today's Task
---
**Read** (-): None - integration day.

**Build** (30-40 min): Write a short 1-page summary combining Day 24 and Day 25 findings: what happened, your own severity judgment (High/Medium/Low), and one root-cause sentence for each.

## Deliverable
---
red-team-notes.md - this Learning Log doubles as that file, or references it directly. This is the Week 4 Challenge.

**Note:** A formal multi-section red team report with full OWASP tagging is a later stretch goal - this week the bar is 2 real findings, clearly explained.

## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Combine the findings from the direct and indirect prompt injection experiments into a concise red-team summary that explains what happened, evaluates the severity of each finding, and identifies the underlying root cause.


### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
Direct and indirect prompt injection target different stages of an AI application's workflow. Direct prompt injection attacks user input, while indirect prompt injection attacks external content retrieved by the agent. Even when tools are properly scoped, retrieved content can still influence the model, making secure context handling just as important as tool security.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
I would expand the experiments by testing more realistic prompt injection techniques, varying the wording, document structure, and instruction complexity to better understand the model's robustness and identify the conditions under which the attacks become more effective.
Along with this will try to find the models from hugging face to test against.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
what techniques provide the strongest protection against increasingly sophisticated prompt injection attacks?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub

## References
---

[Day 025](../Day-025/) | [Week 4](../README.md) | [Root](../../README.md) | [Day 027](../Day-027/)
