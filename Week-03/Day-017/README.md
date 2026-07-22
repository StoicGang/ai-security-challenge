# Day 017 - MCP Awareness

**Week 3 - Scoped Task** | [Day 016](../Day-016/) | [Week 3](../README.md) | [Root](../../README.md) | [Day 018](../Day-018/)

## Today's Task
---

**Read** (10-15 min): MCP documentation (modelcontextprotocol.io) - the 'What is MCP' intro paragraph only.

**Build** (20-30 min): Look at ONE MCP server you already have access to. List 3 tools it exposes, in your own words.

## Deliverable
---
This Learning Log with a markdown table: tool name, what it does, what it can access - 3 rows.

**Note:** No server-building required. This is an observation exercise, not a build exercise.

## Learning Log
---
### The Challenge
<!-- What problem were you actually trying to solve today, in one sentence? -->
Understand the purpose of the Model Context Protocol (MCP) 

### Key Concept
<!-- The idea in plain English — no jargon, as if explaining to a junior. -->
The Model Context Protocol (MCP) is an open standard that defines a common way for AI applications to communicate with external tools and data sources through MCP servers.

Think of MCP as a universal connector between an AI and external systems like GitHub, databases, or documentation. Instead of every AI application building a different integration for each service, the AI can use the same protocol to discover available tools and use them in a consistent way. This makes integrations more reusable, easier to maintain, and more secure to manage.

### How I Approached It
<!-- Numbered steps, briefly. This is the only "steps" section — everything else below should be about the mechanism, not the process. -->
1. An AI client connects to an MCP server.
2. The MCP server advertises the tools it makes available.
3. The AI discovers those tools and understands what each one can do.
4. When the user asks for something, the AI decides whether a tool is needed.
5. If needed, the AI invokes the appropriate MCP tool with the required arguments.
6. The MCP server executes the request against the external service (such as GitHub or a documentation server) using the configured credentials.
7. The external service returns the result to the MCP server.
8. The MCP server sends the result back to the AI, which uses it to generate the final response for the user.

### Code Snippet (if relevant)
<!-- 5-10 lines max, only if it illustrates the concept. Not the whole file. -->
```python

```

### Key Learning
<!-- The one thing you understand now that you didn't before today. -->
MCP is the standard interface between ai clients and external services. It keeps tool implementation separate from the AI. 

### Ah-ha Moment
<!-- The specific instant it clicked, and what made it click. -->
Related the access contols priciples and MCP

### What I'd Do Differently
<!-- If you redid today, what would you change? -->
When evaluating an MCP server in the future, I would first classify everytool by its permission level(read, write, delete, execute) before looking at its functionalities.

### Residual Questions
<!-- What still doesn't make sense? Carry this into tomorrow or the Day 6 buffer. -->
How are authentication and authorization handled between an MCP server and external services like GitHub?

### Deepwiki
| Tool Name             | What it does                                                                           | What it can access                                                                                             |
| --------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `read_wiki_structure` | Returns the documentation structure or table of contents.                              | Read access to the repository's documentation/DeepWiki knowledge to discover its structure.                    |
| `read_wiki_contents`  | Returns the actual text of the requested documentation sections.                       | Read access to the repository's documentation.                                                                 |
| `ask_question`        | Answers natural-language questions by retrieving and reasoning over the documentation. | Read access to the repository's documentation. It does **not** require additional write or delete permissions. |


### Github
| Tool                  | What it does                                                                                           | What it can access                                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `get_file_contents`   | Retrieves the contents of a specific file or lists the contents of a directory in a GitHub repository. | Files and directories in repositories that the provided GitHub credentials are authorized to access.                                     |
| `issue_write`         | Creates new GitHub issues or updates existing ones.                                                    | Issues and issue metadata (such as title, description, labels, assignees, etc.) in repositories the credentials are permitted to modify. |
| `create_pull_request` | Creates a pull request to propose changes from one branch to another.                                  | Pull request functionality and repository branches in repositories where the credentials have permission to create pull requests.        |


## Day Checklist
---
- [ ] Reading done (within time box - don't let one resource eat the whole day)
- [ ] Build complete
- [ ] Deliverable exists exactly as specified above
- [ ] Learning Log fully written (all 8 sections - this .md file IS the deliverable)
- [ ] Committed to GitHub

## References
---
[Model context protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
[Deepwiki](https://deepwiki.com/)
[Github MCP server](https://github.com/github/github-mcp-server/blob/main/README.md#tools)


[Day 016](../Day-016/) | [Week 3](../README.md) | [Root](../../README.md) | [Day 018](../Day-018/)
