# Week 3 Learning — AI Agents and Tool Calling

## STRIDE 
---
| Category                       | Security Principle | Question to Remember          |
| ------------------------------ | ------------------ | ----------------------------- |
| **S — Spoofing**               | Authentication     | **Who are you?**              |
| **T — Tampering**              | Integrity          | **Was it changed?**           |
| **R — Repudiation**            | Accountability     | **Who did it?**               |
| **I — Information Disclosure** | Confidentiality    | **Who can see it?**           |
| **D — Denial of Service**      | Availability       | **Can we still use it?**      |
| **E — Elevation of Privilege** | Authorization      | **Are you allowed to do it?** |


## Core Concepts
---

### STRIDE
STRIDE is a threat-modeling framework used to categorize security threats into six categories: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege.

>STRIDE maps threats to the security property being violated.

### Attack Path
An attack path describes how an attacker moves through different components or stages to achieve an objective. Different stages of the same attack can create different security impacts.

>One attack path can contain multiple threats.

### Prompt Injection
Prompt injection is an attack where malicious instructions attempt to manipulate an AI system into behaving differently from its intended instructions.

>Prompt injection describes the attack technique. The resulting security impact determines what threat category may apply.

### Trust Boundary
A trust boundary separates trusted information or components from untrusted ones. Crossing that boundary without appropriate validation can allow untrusted input to influence trusted behavior.

>External input is untrusted until the application establishes otherwise.

### Tool-Call Logging
Tool-call logging records actions performed by an AI agent, such as the selected tool, arguments, execution result, and relevant context.

>Logging should provide useful evidence without unnecessarily exposing sensitive information.

### Security Audit
A security audit uses recorded events as evidence for investigating and evaluating security-related activity.

>A log records what happened; an audit uses trustworthy records to establish what happened.

## Understanding Check
---

### When an attack violates multiple security properties across different stages of the same attack path, how should the primary STRIDE category be selected for a component?
When an attack violates multiple security properties across different stages of an attack path, each relevant component or stage should be classified according to the security property it actually violates, rather than the original attack technique.
A single attack path can therefore have multiple STRIDE categories. For example, prompt injection may manipulate an agent into accessing a resource beyond its authorization, representing Elevation of Privilege. If the agent then exposes the contents of that resource to an unauthorized party, the resulting impact is Information Disclosure.
The primary category for a specific component should be the category that best represents the component's direct security impact. Other categories can be recorded for subsequent impacts in the same attack path.

>Attack technique → affected component → security impact → STRIDE category

### If the prompt injection attack had been successful, how would the STRIDE reasoning change, and what differentiating factor would determine the appropriate threat category based on the resulting security impact?
If a prompt injection attack succeeds, the STRIDE classification should not automatically be Tampering or any other single category. Prompt injection describes the attack technique, while the appropriate STRIDE category depends on the security impact produced by the resulting behavior.
For example:
- Unauthorized modification of data or system state → Tampering
- Unauthorized access to capabilities or resources → Elevation of Privilege
- Exposure of protected information → Information Disclosure
- Disruption of service → Denial of Service
The differentiating factor is therefore the security property violated by the successful outcome of the attack, not the fact that prompt injection was used.

>Prompt injection tells us how the attacker influenced the system; the resulting security impact tells us which STRIDE category applies.

### How much can prompt-level trust separation be relied upon before a stronger application-level control is required?
Prompt-level trust separation can be used as a defense layer, but it should not be treated as a strong security boundary by itself. LLMs are probabilistic and may interpret attacker-controlled input in unintended ways, even when system instructions clearly distinguish trusted instructions from untrusted content.
Once an action becomes security-critical, stronger application-level controls should enforce the boundary. These can include authorization checks, least privilege, tool scoping, validation, and human approval for high-risk actions.
The principle is:
**Prompt-level controls guide model behavior; application-level controls enforce security.**

>Therefore, the question is not "How strong is my prompt?" but "What happens if the model ignores it?"

### How should tool-call logging handle arguments when a tool input may contain sensitive data or executable content?
Tool-call logging should capture enough information to reconstruct the security-relevant event without unnecessarily storing sensitive or executable arguments. The application can log the caller or agent, tool name, timestamp, execution status, and relevant result metadata. If arguments are required for investigation, sensitive fields should be selectively redacted, masked, or otherwise protected rather than blindly recording the complete raw input.

>Log the event needed for accountability, not every piece of data involved in the event.

### How should runtime tool-call logging evolve into a proper security audit mechanism?
Runtime tool-call logging can evolve into a proper security audit mechanism by making security-relevant events structured, attributable, consistent, and protected.
Each event should capture information such as the actor or agent, timestamp, action/tool, relevant resource, authorization context, and outcome. The logging system should also protect audit records from unauthorized modification or deletion and enforce appropriate access and retention policies.
This allows the logs to support not only debugging and monitoring, but also incident investigation, accountability, and detection of unauthorized activity.

>Logging records events; security auditing makes those records trustworthy and useful as evidence.

### Walk through the AI threat model for one component: STRIDE category, mitigation, residual risk.
I would threat-model the file-read tool as an Elevation of Privilege risk because an over-scoped tool could allow the agent to access files beyond the intended authorization. The mitigation is to enforce least privilege through a specific file or path allowlist and keep the tool read-only when write access isn't required. The residual risk is that even an approved file may contain sensitive or malicious content, so restricting filesystem access does not eliminate risks from the content itself or from how that content is subsequently processed.
- **Component**: File-read tool
- **Threat**: Unauthorized access to filesystem resources
- **STRIDE**: Elevation of Privilege
- **Mitigation**: Restrict the tool to explicitly approved files/paths
- **Residual risk**: Approved resources can still contain sensitive or malicious content, and downstream processing of that content may create additional security risks.

### Why is logging the prompt and the tool call, not just the final output, necessary for AI system monitoring?
Logging the prompt and tool calls, rather than only the final output, is necessary because an AI agent can perform multiple actions before producing its final response. The final output alone does not show which instructions influenced the agent, which tools were selected, what actions were performed, or whether those actions were authorized.
Logging the interaction and tool-call sequence allows defenders to detect unexpected behavior, investigate failures, identify prompt-injection effects, and reconstruct an attack path.

>The final output tells us what the agent said; the prompt and tool calls help establish why it said it and what it actually did.

### How do you scope an agent's tool permissions practically, not just in theory?
Practically, I would scope an agent's permissions by exposing only the tools and capabilities required for its task, while enforcing the actual permissions at the application level. Tools should have clearly defined scopes, such as read-only access to specific resources rather than unrestricted filesystem or API access. RAG can be used to retrieve or select relevant tools dynamically, but it should not be treated as the authorization mechanism because retrieval can be incorrect. The application should independently validate whether the requested tool and operation are authorized before execution.

> RAG can decide what is relevant; application-level authorization decides what is allowed.

## Mental Models
---

| STRIDE Category            | AI-Security Example                                                                                                   | What the Threat Looks Like                                                                                                                            |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Spoofing**               | An attacker impersonates an authorized user of an AI agent.                                                           | The system accepts the attacker's identity as if they were a legitimate user, allowing them to interact with the agent under someone else's identity. |
| **Tampering**              | An attacker modifies retrieved documents or agent context before the model uses them.                                 | The agent processes altered information and may produce decisions or actions based on data that was changed without authorization.                    |
| **Repudiation**            | A user denies making a sensitive tool call, but the system has no reliable record connecting the action to that user. | The system cannot reliably establish who performed a security-relevant action, making investigation and accountability difficult.                     |
| **Information Disclosure** | An AI agent exposes a private document, system prompt, API key, or other confidential information.                    | Information that should remain restricted becomes accessible to an unauthorized person or component.                                                  |
| **Denial of Service**      | An attacker causes an agent to repeatedly perform expensive operations or consume excessive resources.                | The system becomes unavailable, degraded, or excessively expensive for legitimate users.                                                              |
| **Elevation of Privilege** | An agent uses a privileged tool or accesses a resource beyond the permissions granted to the user.                    | A user or agent obtains capabilities or access that it was not authorized to have.                                                                    |


## Biggest Takeaway
---
Week 6 taught me to look beyond the attack technique and reason about the security impact on each component. A single attack path can produce multiple STRIDE categories, so the correct category depends on the security property actually violated. I also learned that model behavior cannot be treated as a security boundary: least privilege, tool scoping, authorization, and other controls must be enforced at the application level. Finally, logging should capture the agent's actions, not just its final response, so those events can evolve into trustworthy security evidence for monitoring and investigation.

> Understand the attack path, identify the security impact, enforce the boundary in the application, and preserve evidence of what happened.