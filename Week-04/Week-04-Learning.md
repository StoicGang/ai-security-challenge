# Week 4 Learning - AI Security Fundamentals


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

## Mental Models
---

| Concept                 | Mental Model                                                                                         |
| ----------------------- | ---------------------------------------------------------------------------------------------------- |
| Prompt Chaining         | Completing a project by following a checklist instead of trying to do everything at once.            |
| Structured Outputs      | Filling out a standardized form instead of writing a free-form letter.                               |
| Direct Prompt Injection | Someone convincing a receptionist to ignore company policy by giving persuasive verbal instructions. |


## Biggest Takeaway (Week 4 - In Progress)
---
