# Day 018 - Tool Scoping and Least Privilege

**Week 3 - Scoped Task** | [Day 017](../Day-017/) | [Week 3](../README.md) | [Root](../../README.md) | [Day 019](../Day-019/)

---

## Today's Task

**Read** (0-10 min): No new reading required if least-privilege is already familiar from your cybersecurity background - otherwise a 10-minute refresher on the principle.

**Build** (30-40 min): Add a second tool to Day 16's loop - a 'read this specific file' tool - restricted to one hardcoded filename, not a whole directory.

## Deliverable
---

This Learning Log with a test showing the model attempting to use the tool outside its scope, and the result (blocked, or documented as 'would be blocked because...').

**Note:** One hardcoded file is enough to prove the scoping mechanism works.

---

## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Restrict an AI file-reading tool to a single approved file and demonstrate that it cannot access anything outside its intended scope.

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
Least privilege means giving a tool only the minimum permissions it needs to perform its job. Instead of allowing an AI to read any file, the tool is limited to one hardcoded file. Even if the model receives a malicious prompt or prompt injection, it cannot access files the tool was never designed to read. By enforcing the restriction inside the tool, the potential impact of an attack is limited because the attacker cannot make the tool perform actions beyond its scope.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. Exposed a dedicated file-reading tool instead of giving the agent general file system access.
2. Hardcoded the tool to read only the approved Week-02/Day-009/article.md file.
3. Removed the filename parameter so the model cannot request arbitrary files through the tool.
4. Enforced the restriction inside the tool itself, making the implementation the security boundary rather than relying on prompt instructions.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python
def read_specific_file(): 
    document_path = file_path( week=2, day=9, filename="article.md" ) 
    return read_document(document_path)
```

### Test Results

| Test Case | Prompt | Expected Result | Actual Result | Status |
|-----------|--------|-----------------|---------------|:------:|
| Valid request | Read the approved document and summarize it. | Tool reads the hardcoded `article.md` file. | Successfully read the approved file and generated a summary. | worked |
| Out-of-scope request | Read the `.env` file. | Access should be denied because the tool is scoped to one hardcoded file. | The model refused the request and could only access the approved file because the tool exposes no filename parameter. | worked |

> **Detailed execution logs:** See [TEST_RESULTS.md](./TEST_RESULTS.md) for the complete terminal output, runtime error, root cause analysis, and the corrected implementation.

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
Least privilege is not about trusting the model to behave correctly. It is about designing tools with only the capabilities they actually need, so even malicious prompts cannot make them perform unauthorized actions.

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
The idea clicked when I realized that the security boundary is the tool itself, not the system prompt.

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
From now on, I would design every tool by first identifying its minimum required permissions and exposing only those capabilities instead of building a general-purpose tool and restricting it later.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How can the principle of least privilege be applied when a tool legitimately needs access to multiple files or directories without becoming overly permissive?

## Day Checklist
---
- [x] Reading done (within time box - don't let one resource eat the whole day)
- [x] Build complete
- [x] Deliverable exists exactly as specified above
- [x] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [x] Committed to GitHub


References
---

[Day 017](../Day-017/) | [Week 3](../README.md) | [Root](../../README.md) | [Day 019](../Day-019/)
