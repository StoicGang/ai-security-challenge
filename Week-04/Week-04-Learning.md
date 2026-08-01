# Week 4 Learning - AI Security Fundamentals

## OWASP Top 10 for LLM Applications 

| Sr. No | Category | Remember It As |
|---|----------|----------------|
| LLM01 | Prompt Injection | Malicious instructions manipulate the model. |
| LLM02 | Sensitive Information Disclosure | AI exposes secrets or confidential data. |
| LLM03 | Supply Chain | Compromised models, datasets, or dependencies. |
| LLM04 | Data and Model Poisoning | Training or retrieval data is intentionally corrupted. |
| LLM05 | Improper Output Handling | Application trusts unsafe model output. |
| LLM06 | Excessive Agency | AI has more permissions than it should. |
| LLM07 | System Prompt Leakage | Hidden instructions become exposed. |
| LLM08 | Vector and Embedding Weaknesses | Weak retrieval or vector database security. |
| LLM09 | Misinformation | AI generates false or misleading information. |
| LLM10 | Unbounded Consumption | AI consumes excessive resources or cost. |

> **Memory Rule**
>
> **Input → Data → Output → Permissions → Infrastructure**
>
> - **Input:** LLM01 (Prompt Injection)
> - **Data:** LLM02, LLM03, LLM04
> - **Output:** LLM05, LLM07, LLM09
> - **Permissions:** LLM06
> - **Infrastructure:** LLM08, LLM10

## Core Concepts
---

### Prompt Chaining
Prompt chaining breaks a complex task into multiple smaller prompts, where the output of one prompt becomes the input to the next. This makes AI workflows more modular, easier to debug, and more reliable than relying on a single large prompt.

>**Remember**: Divide complex reasoning into manageable steps.

### Structured Outputs

Structured outputs require an AI model to return responses in a predefined format, such as JSON or a schema, instead of unrestricted natural language. This improves reliability by making the output easier for applications to validate and process automatically.

>**Remember**: Constrain the output, not just the prompt.

### Direct Prompt Injection

Direct prompt injection is an attack where a user includes malicious instructions directly in their input, attempting to override the application's intended behavior or the model's original instructions. Since both trusted instructions and user input are processed as natural language, the model may treat attacker-controlled text as legitimate instructions.

>**Remember**: User input is untrusted data, even when it looks like instructions.

### Indirect Prompt Injection

Indirect prompt injection is an attack where malicious instructions are hidden inside external content, such as documents, emails, or web pages, that an AI agent later retrieves. Instead of sending the instructions directly to the model, the attacker places them in the retrieved data, hoping the model will treat those instructions as part of its context and follow them.

> **Remember**: Retrieved data is untrusted, even when it comes from an approved tool.


### Trust Boundaries

A trust boundary separates trusted information, such as system prompts or application logic, from untrusted information like user input or retrieved documents. Crossing this boundary without validation can allow attackers to influence an AI application's behavior.

> **Remember:** Treat every external input as untrusted until proven otherwise.


## Understanding check

### Some OWASP Top 10 for LLM Applications categories appear closely related, such as Prompt Injection and Sensitive Information Disclosure.
Prompt Injection and Sensitive Information Disclosure are closely related but describe different parts of an attack chain.
Prompt Injection is the **attack vector**. It occurs when an attacker manipulates the model through malicious instructions, causing it to behave in an unintended way.
Sensitive Information Disclosure is the **impact**. It occurs when the manipulated model exposes confidential information such as API keys, system prompts, private documents, or user data.
For example, an attacker may first use a prompt injection attack to convince an AI assistant to ignore its original instructions. If the model then reveals an API key stored in its context, the Prompt Injection enabled the attack, while Sensitive Information Disclosure describes the resulting security breach. 
The boundary should therefore be drawn between **how the attacker gained influence** (Prompt Injection) and **what security consequence followed** (Sensitive Information Disclosure). During incident analysis, both categories may apply to the same attack chain because one vulnerability can directly lead to another.
> **Remember**: Prompt Injection is the cause; Sensitive Information Disclosure is one possible effect.

### How should organizations reassess OWASP risk ratings as an AI application evolves over time?
The original OWASP risk assessment should not be considered permanently valid because an AI application's attack surface changes as new capabilities are introduced.
Features such as long-term memory, retrieval-augmented generation (RAG), tool calling, external APIs, file access, or database integrations create new trust boundaries and new opportunities for attackers. A chatbot that only generates text has a much smaller risk profile than an AI agent that can retrieve documents, execute tools, or interact with external systems.
Organizations should reassess their OWASP risk ratings whenever significant architectural changes are introduced, including:
- Adding new tools or external integrations.
- Enabling long-term memory.
- Introducing RAG or document retrieval.
- Expanding the permissions available to the agent.
- Processing new categories of sensitive data.
Risk assessment should be treated as a continuous activity throughout the application's lifecycle rather than a one-time exercise performed during initial deployment. As the application's capabilities evolve, its security controls and OWASP risk ratings should evolve as well.

>**Remember**: New capabilities create new attack surfaces, and new attack surfaces require a new risk assessment.

### What techniques provide the strongest protection against increasingly sophisticated prompt injection attacks?
We can use following important defensive techniques:
- Treating all user input and retrieved content as untrusted.
- Applying the principle of least privilege so tools have only the minimum permissions required.
- Enforcing strict access controls for sensitive resources.
- Using structured outputs and input validation where appropriate.
- Implementing human approval for high-risk actions.
- Monitoring and logging AI interactions to detect suspicious behavior.
- Applying defense-in-depth so that if one control fails, other security mechanisms continue protecting the system.

Rather than relying on the model to always reject malicious prompts, organizations should design the application assuming prompt injection attempts will occur and limit the damage through layered security controls.

>**Remember**: Prompt injection is mitigated, not eliminated. Security comes from layers of defenses, not from trusting the model to always make the correct decision.

### Why are system prompts alone insufficient to defend an AI application against prompt injection attacks?
System prompts alone are not sufficient to defend against prompt injection attacks because LLMs are probabilistic systems and cannot be relied upon to consistently ignore malicious instructions. An attacker may still influence the model's behavior through carefully crafted inputs. Security should therefore be enforced by the application rather than relying entirely on the model. Effective defenses include least privilege for tools, tool scoping, strict access controls, input and output validation, structured outputs, monitoring, and human approval for high-risk actions. A system prompt should be treated as one layer of defense, not the only layer. Secure AI applications assume that prompt injection attempts will occur and limit their impact through application-level security controls.

>**Remember**: System prompts guide behavior; application security enforces it.

## Mental Models
---

| Concept                   | Mental Model                                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Prompt Chaining           | Completing a project by following a checklist, where each completed step provides the input for the next one.                            |
| Structured Outputs        | Filling out a standardized form instead of writing a free-form letter, making the information easier to process consistently.             |
| Direct Prompt Injection   | Someone convincing a receptionist to ignore company policy through persuasive verbal instructions.                                        |
| Indirect Prompt Injection | A spy hides instructions inside an official-looking document, hoping the reader follows the hidden note instead of their original task.   |
| Trust Boundaries          | A security checkpoint that verifies every visitor before allowing them into a restricted area.                                            |

## Biggest Takeaway
---

Week 4 shifted my perspective from building AI applications to securing them. I learned that even well-designed agents can be influenced by malicious instructions if untrusted input is treated as trusted context. Reliable AI systems require more than capable language models, they need structured outputs, carefully designed prompt flows, and security controls that assume all external input, whether from users or retrieved content, may be adversarial. Security should be enforced by the application, not delegated entirely to the model.
