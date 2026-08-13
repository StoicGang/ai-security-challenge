from config import lab_artifact_path

from common.prompts import RAG_PROMPT
from common.gemini_client import (
    generate_content,
    create_interaction,
    get_function_calls,
    continue_interaction,
)
from common.tools import (
    ALL_TOOLS,
    execute_tool,
)


DOCUMENT_PATH = lab_artifact_path(
    "day038_indirect_injection_02.md"
)


def build_prompt(
    query: str,
    context: str,
    prompt_template=RAG_PROMPT,
) -> str:
    return prompt_template.format(
        context=context,
        query=query,
    )


def run_rag():
    from common.rag_integration import retrieve_context

    query = input("Question: ").strip()

    result = retrieve_context(
        document_path=DOCUMENT_PATH,
        query=query,
    )

    context = result["context"]

    print("\n=== Retrieved Context ===")
    print(context)

    prompt = build_prompt(
        query=query,
        context=context,
    )

    print("\n=== Agent Answer ===")

    try:
        response = generate_content(prompt)
        print(response.text)
    except Exception as error:
        print(f"Gemini request failed: {error}")


def run_agent():
    user_prompt = input("Agent request: ").strip()

    interaction = create_interaction(
        user_prompt=user_prompt,
        tools=ALL_TOOLS,
    )

    while True:
        function_calls = get_function_calls(interaction)

        if not function_calls:
            print("\n=== Agent Answer ===")
            print(interaction.output_text)
            break

        function_results = []

        for step in function_calls:

            print(
                f"[TOOL CALL] "
                f"name={step.name} "
                f"input={step.arguments}"
            )

            result = execute_tool(
                tool_name=step.name,
                arguments=step.arguments,
            )

            function_results.append(
                {
                    "type": "function_result",
                    "name": step.name,
                    "call_id": step.id,
                    "result": [
                        {
                            "type": "text",
                            "text": str(result),
                        }
                    ],
                }
            )

        interaction = continue_interaction(
            previous_interaction_id=interaction.id,
            function_results=function_results,
            tools=ALL_TOOLS,
        )


def main():
    print("Select mode:")
    print("1. RAG")
    print("2. Agent")

    mode = input("Choice: ").strip()

    if mode == "1":
        run_rag()

    elif mode == "2":
        run_agent()

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()