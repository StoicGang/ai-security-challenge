```mermaid
flowchart TD
    U[User]

    subgraph Agent
        LLM[Gemini LLM]
        Loop[Agent Loop]
    end

    subgraph Tools
        Calc[Calculator Tool]
        Time[Date & Time Tool]
        File[Read Specific File Tool]
    end

    U --> LLM
    LLM --> Loop

    Loop --> Calc
    Loop --> Time
    Loop --> File

    Calc --> Loop
    Time --> Loop
    File --> Loop

    Loop --> LLM
    LLM --> U

    File -.Least Privilege.-> Approved[(article.md only)]
```