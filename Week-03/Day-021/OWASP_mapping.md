| Asset / Component                | Possible Attacker Goal                         | Suspected OWASP Category (2023-24)                             | Existing Control                           |
| -------------------------------- | ---------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------ |
| LLM                              | Manipulate the model with crafted instructions | Prompt Injection                                               | Tool restrictions and least privilege      |
| `read_specific_file()` tool      | Read unauthorized files                        | Prompt Injection                                               | Hardcoded file path                        |
| Calculator tool                  | Invoke tool outside intended purpose           | Prompt Injection                                               | Single-purpose tool                        |
| Approved document (`article.md`) | Access or expose document contents             | Sensitive Information Disclosure *(if sensitive data existed)* | Reads only one approved file               |
| Gemini API Key                   | Steal API credentials                          | Sensitive Information Disclosure                               | Stored in `.env`, not exposed to the model |
