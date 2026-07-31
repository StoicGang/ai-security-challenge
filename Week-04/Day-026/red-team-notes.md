# Day 026 - Week 4 Challenge - Red-Team Notes

## Week 4 Challenge Summary

### Finding 1 - Direct Prompt Injection (Day 24)

#### What Happened

I attempted two direct prompt injection attacks by sending malicious instructions through normal user input to my Week 3 AI agent. The goal was to determine whether the model would ignore its original behavior and follow attacker-controlled instructions. The model treated the injected prompts as user input and evaluated them against its existing instruction hierarchy. The observed responses showed that the model resisted the direct injection attempts rather than blindly following the malicious instructions.

#### Severity: Medium

#### Reasoning: 
Direct prompt injection targets the primary communication channel between the user and the model. If successful, it could manipulate the agent's behavior or bypass intended safeguards. In my experiment the attacks were unsuccessful, reducing the immediate impact, but the attack vector remains realistic and common for AI applications.

#### Root Cause: 
The language model must interpret both trusted instructions and user-supplied text, creating opportunities for malicious prompts to compete with legitimate instructions.

### Finding 2 - Indirect Prompt Injection (Day 25)

#### What Happened

I placed a malicious instruction inside a text document and used the agent's scoped read_specific_file() tool to retrieve it. The tool successfully returned the document, causing the hidden instruction to become part of the model's context. Gemini analyzed both the user's request and the retrieved document but ultimately ignored the malicious instruction and followed the user's intended request.

#### Severity: Low

#### Reasoning: 
Although the attack path existed and the malicious content reached the model, the model successfully resisted the embedded instruction. Under the tested conditions, the practical security impact was limited because no unintended behavior occurred.

#### Root Cause: 
External content retrieved by AI tools becomes part of the model's context, requiring the model to distinguish between legitimate data and malicious embedded instructions.