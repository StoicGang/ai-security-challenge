# Week 3 Learning — AI Agents and Tool Calling

## Agent Loop
---

```text
User Request
      ↓
LLM (Reasoning)
      ↓
Plan
      ↓
Need a Tool?
   ↙        ↘
 No          Yes
 ↓            ↓
Respond    Select Tool
              ↓
        Execute Tool
              ↓
        Observe Result
              ↓
      More Actions Needed?
         ↙            ↘
       Yes             No
        ↓               ↓
      Plan        Final Response
```
## Core Concepts
---

### AI Agent
An AI agent extends an LLM by allowing it to interact with external tools to accomplish tasks. Instead of producing a response in a single generation, an agent can reason, perform actions, observe results, and continue working until it reaches an objective.

### Function Calling
Function calling enables an LLM to request the execution of predefined functions when they are better suited than natural language generation alone. The application validates and executes the requested function before returning the result to the model.

Remember: The model requests a function; the application executes it.

### Agent Loop (Plan → Act → Observe)

The agent loop is an iterative reasoning process where the model plans its next action, performs the selected tool call, observes the returned result, and repeats the process until enough information is available to answer the user.

>**Remember**: Agents think between actions instead of producing one immediate answer.

### Tool Calling
Tool calling allows an AI agent to extend its capabilities by interacting with external systems such as calculators, APIs, databases, or file readers instead of relying solely on the model's internal knowledge.

### Model Context Protocol (MCP)
Model Context Protocol (MCP) is an open standard that allows AI models to communicate with external tools and data sources through a consistent interface. It separates tool implementations from the model, making integrations reusable across different AI applications.

### Least Privilege
Least privilege is the security principle of granting every tool only the minimum permissions required to perform its intended task.

>**Remember**: Restrict capabilities, not just model behavior.

### Tool Scoping
Tool scoping limits what a tool can access or perform. Rather than exposing an entire filesystem or API, tools should expose only the specific resources required by the application.

### Prompt Injection
Prompt injection is an attack where malicious instructions attempt to manipulate the model into performing unintended actions or ignoring its original instructions.

>**Remember**: Secure tools should remain safe even if the model is manipulated.

## Understanding Check
---
### What is the practical difference between a tool call and a function call?
A function call is the model's request to execute a predefined function implemented by the application. The application validates the request, executes the function, and returns the result to the model. A tool call, on the other hand, represents a higher-level capability that the model can use, such as searching a database, reading a file, or calling an API. Internally, a tool is often implemented using one or more functions. In practice, the model selects a tool based on its description, while the application executes the underlying function(s) that implement that capability.

>A function is an implementation; a tool is a capability exposed to the model.

### Why is an over-scoped tool a security issue even if the model usually behaves correctly?
An over-scoped tool violates the principle of least privilege by exposing more capabilities than the task requires. Even if the model usually behaves correctly, LLMs are probabilistic systems and can occasionally make incorrect decisions or receive misleading inputs. If a tool has excessive permissions, a single unintended tool invocation could access or modify resources beyond its intended scope. Restricting tools to the minimum required permissions reduces the impact of both accidental errors and malicious attempts to misuse the agent.

>The security risk comes from what the tool can do, not from how often the model behaves correctly.

### What problem does MCP solve that ad-hoc tool integration does not?
MCP solves the lack of a standardized interface between AI applications and external tools. Without MCP, every application must build custom integrations for each service, resulting in duplicated effort and incompatible implementations. MCP defines a common protocol that allows AI clients to discover, authenticate with, and interact with external tools in a consistent way. This makes tool integrations reusable, portable, and easier to maintain across different AI applications and model providers.

>Without MCP, every integration is custom; with MCP, tools expose one standard interface that any compatible AI client can use.

### What happens if two tools have very similar descriptions?
If two tools have very similar descriptions or overlapping capabilities, the model may have difficulty determining which one is the best match for the user's request. Since the model selects tools based on their names, descriptions, and parameter schemas, ambiguous or redundant tool definitions can lead to inconsistent or unintended tool selection. To improve reliability, each tool should have a clear, distinct purpose with descriptive names and documentation that minimizes overlap.

>Clear tool descriptions reduce ambiguity and help the model choose the intended tool consistently.

### How can the principle of least privilege be applied when a tool legitimately needs access to multiple files or directories without becoming overly permissive?
When a tool legitimately requires access to multiple files or directories, least privilege should be applied by granting access only to the specific locations required for its task rather than broad filesystem permissions. An explicit allowlist of approved directories should be maintained, and every requested path should be validated against it before access is granted. In addition, the tool should be limited to the minimum operations it needs, such as read-only access if writing is unnecessary. This approach provides the required functionality without exposing unrelated resources.

>Least privilege is achieved by granting only the specific resources and operations a tool requires, not by granting broad access and trying to block dangerous cases later.

### How are authentication and authorization handled between an MCP server and external services like GitHub?
Authentication between an MCP server and external services such as GitHub is typically handled using OAuth. The user authenticates with the external service, which issues an access token to the MCP server. When the MCP server makes API requests, it presents this token to prove its identity. Authorization is then enforced by the external service based on the token's granted scopes or permissions, ensuring the MCP server can perform only the actions the user has explicitly authorized.

>Authentication verifies identity, while authorization determines what actions that authenticated identity is allowed to perform.

### How does the reasoning loop support multiple sequential or parallel tool calls within a single interaction?
The reasoning loop supports multiple sequential tool calls by feeding the result of each tool execution back into the model. After observing the returned output, the model re-evaluates the task and decides whether additional tools are needed or whether it has enough information to generate the final response. Some agent frameworks also support parallel tool calls when independent tasks can be executed simultaneously, allowing multiple tool results to be combined before the model continues its reasoning. This iterative Plan → Act → Observe cycle enables agents to solve complex tasks that require more than a single action.

> Each tool result becomes new context for the next reasoning step.

### How does the model decide which function to call when multiple tools are available? If several tools have overlapping capabilities, what influences its selection, and how are priorities determined?
When multiple tools are available, the model compares the user's request with each tool's schema, including its name, description, and parameter definitions. It selects the tool whose documented capability best matches the requested task. If several tools have overlapping descriptions or similar functionality, the choice becomes more ambiguous and may be inconsistent. Therefore, applications should design tools with clear, distinct responsibilities and descriptive schemas to guide reliable tool selection.

>The model chooses the tool whose schema best matches the user's intent.

## Mental Models
---

| Concept          | Mental Model                                                                                             |
| ---------------- | -------------------------------------------------------------------------------------------------------- |
| AI Agent         | A project manager who delegates work to specialists instead of doing everything alone.                   |
| Function Calling | Asking an electrician to fix wiring instead of attempting it yourself.                                   |
| Agent Loop       | Solve → Check → Adjust → Repeat until finished.                                                          |
| Tool Calling     | A worker selecting the correct tool from a toolbox for each task.                                        |
| MCP              | A universal power socket allowing different devices to use the same interface.                           |
| Least Privilege  | Giving a hotel guest access only to their own room, not every room in the building.                      |
| Tool Scoping     | A vending machine that dispenses only the selected item instead of opening the entire storage cabinet.   |
| Prompt Injection | Someone attempting to trick a receptionist into breaking company policy through persuasive instructions. |

## Biggest Takeaway
---
Week 3 taught me that AI agents are fundamentally different from standalone LLMs because they can take actions through external tools. That additional capability also introduces new security responsibilities. Secure agent design depends on restricting tool permissions, enforcing least privilege, and implementing security controls within the application rather than trusting the model to behave correctly.