# Day 037 - Mapping Week 4 Findings to Threats

**Week 6 - Scoped Task** | [Day 036](../Day-036/) | [Week 6](../README.md) | [Root](../../README.md) | [Day 038](../Day-038/)

## Today's Task
---
**Read** (-): None - applied day.

**Build** (20-30 min): Cross-reference your Week 4 findings against the Day 36 table - which finding maps to which STRIDE threat?

## Deliverable
---
This Learning Log with the Day 36 table updated to include a 'Related Finding' column.

## Learning Log
---

### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Cross-reference the Week 4 experiment findings with the Day 36 STRIDE threat model to determine which findings relate to each identified threat and what the results actually demonstrate.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
An attack technique should not be directly mapped to a STRIDE threat. The mapping should be based on the security impact of the attack and the security principle it violates.

### Mappings

### Threat Mapping

| Week 4 Finding               | Attack / Scenario                                                                         | Observed Result                                                                     | Security Impact if Successful                                                                      | Security Principle | STRIDE Mapping         | Reason for Mapping                                                                                                                       | Applicability to Project                                                                  |
| ---------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------ | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Prompt Injection - Attempt 1 | Embedded instruction attempted to override the legitimate translation instruction         | **Blocked**. The model treated the injected instruction as text to translate        | Attacker could manipulate trusted instructions or control flow and cause unintended model behavior | Integrity          | Tampering              | Successful prompt injection in this scenario would manipulate the intended instruction flow, making Tampering the relevant STRIDE threat | Threat is applicable as a scenario, but successful exploitation was not demonstrated      |
| Prompt Injection - Attempt 2 | Structured prompt attempted to make an embedded instruction override the translation task | **Blocked**. The model preserved the intended task and translated the injected text | Attacker could manipulate trusted instructions or control flow                                     | Integrity          | Tampering              | The structured format changes the injection technique, but the potential security impact remains manipulation of trusted instructions    | Threat is applicable as a scenario, but successful exploitation was not demonstrated      |
| Longer Interaction Signature | Injection attempts produced longer interaction signatures than normal prompts             | **Observed but unexplained**                                                        | No confirmed security impact from the available evidence                                           | Not established    | **No mapping**         | The experiment does not establish what the signature represents or whether it corresponds to a security violation                        | Not enough evidence for a STRIDE classification                                           |
| File-Read Tool Scope         | Attempt to access a file outside the tool's hardcoded authorized filename                 | **Blocked by application-level restriction**                                        | Attacker could access resources outside the tool's authorized scope                                | Authorization      | Elevation of Privilege | Bypassing the file restriction would allow the attacker to obtain a capability or resource that was not authorized for the tool          | Threat is applicable, but the implemented defense-in-depth control prevented exploitation |
| Tool Registry                | No Week 4 experiment directly demonstrated manipulation of the tool registry              | **Not directly tested**                                                             | Attacker could potentially make an unauthorized capability available to the agent                  | Authorization      | Elevation of Privilege | The Day 36 threat remains conceptually relevant, but no Week 4 finding provides direct evidence for this specific threat                 | No direct Week 4 finding mapped to this component                                         |


### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
A single attack technique such as prompt injection can map to different threats depending on what it actually compromises, while an observed behavior without a confirmed security impact should not be forced into a STRIDE category.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
I would build a reusable agentic system that maps an attack scenario to the appropriate STRIDE category based on the attack description and its security impact. The system could use RAG to provide relevant threat-modeling context and security principles from the knowledge base we developed earlier, while requiring the agent to justify the mapping instead of blindly assigning a category.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
If the prompt injection attack had been successful, how would the STRIDE reasoning change, and what differentiating factor would determine the appropriate threat category based on the resulting security impact?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written 
- [x] Committed to GitHub

## References
---

[Day 036](../Day-036/) | [Week 6](../README.md) | [Root](../../README.md) | [Day 038](../Day-038/)
