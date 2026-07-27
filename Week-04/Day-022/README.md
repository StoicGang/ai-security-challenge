# Day 022 - OWASP LLM Top 10 - Categories 1 to 5

**Week 4 - Scoped Task** | [Week 4](../README.md) | [Root](../../README.md) | [Day 023](../Day-023/

## Today's Task
---

**Read** (15 min): OWASP Top 10 for LLM Applications - the one-line summary of categories 1-5 only, not the full page.

**Build** (20-30 min): For each of the 5 categories, write one sentence: does this apply to your Week 3 agent, and where?

## Deliverable
---

This Learning Log with a markdown table, 5 rows: category, applies Y/N, where in your architecture.

**Note:** The full OWASP text for all 10 categories is a Day 23-onward reference, not a Day 22 requirement.

## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Identify which of the first five OWASP LLM Top 10 security categories apply to my Week 3 agent by mapping each category to the relevant part of its architecture.

### OWASP LLM Top 10 Assessment

| Category | Applies (Y/N) | Where in my architecture |
|----------|:-------------:|--------------------------|
| **LLM01: Prompt Injection** | **Y** | User input reaches the LLM, which decides whether to invoke `read_specific_file()` or `calculator()`. Scoped tools and least-privilege controls limit the impact. |
| **LLM02: Sensitive Information Disclosure** | **Y** | The agent can access `article.md` through `read_specific_file()`. The Gemini API key is managed by the application and is not exposed to the LLM or any tool. |
| **LLM03: Supply Chain** | **Y** | The agent relies on third-party components such as the Gemini API, the `google-genai` SDK, and external Python libraries. Vulnerabilities in these dependencies could affect the application. |
| **LLM04: Data and Model Poisoning** | **N** | The agent uses a static local document and a hosted Gemini model. End users cannot modify the document, model, or tool definitions through the application. |
| **LLM05: Improper Output Handling** | **N** | The application executes only predefined, scoped Python functions and does not blindly trust or execute arbitrary LLM-generated output. |

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Identified the architectural components of my Week 3 agent, including the LLM, tools, approved document, and external dependencies.
2. Compared each of the first five OWASP LLM Top 10 categories against those components to determine whether the category could apply.
3. Mapped each applicable category to the relevant part of the architecture and considered how existing controls, such as scoped tools and least privilege, reduced the potential impact.


### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
It clicked when I realized that identifying an OWASP category is different from proving the application is vulnerable. A category can still apply because the attack is possible in theory, while design choices such as scoped tools and least privilege determine whether the attack can actually succeed.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
If I repeated this exercise, I would begin by mapping the architectural components of the agent before reviewing the OWASP categories. This would make it easier to evaluate each category systematically and distinguish between identifying a potential risk and assessing whether existing security controls mitigate it.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
Some OWASP LLM Top 10 categories appear closely related, such as Prompt Injection and Sensitive Information Disclosure. How do these categories interact during a real attack chain, and where should the boundary between them be drawn when analyzing an AI application?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all sections - this .md file IS the deliverable)
- [x] Committed to GitHub

---

[Week 4](../README.md) | [Root](../../README.md) | [Day 023](../Day-023/)
