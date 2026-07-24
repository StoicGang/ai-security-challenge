from google import genai
from common.tools import (
    calculator,
    get_datetime,
    read_specific_file,
    ALL_TOOLS,
)
import json
from config import(
    GEMINI_API_KEY,
    GENAI_MODEL_NAME,
)

client = genai.Client(api_key=GEMINI_API_KEY)
function_results = []

user_query=input("Ask a question: ")

interaction = client.interactions.create(
    model=GENAI_MODEL_NAME,
    input=user_query,
    tools=ALL_TOOLS,
)

for step in interaction.steps:
    print(step)
    if step.type == "function_call":

        if step.name == "calculator":
            result = calculator(step.arguments["expression"])

        elif step.name == "get_datetime":
            result = get_datetime(step.arguments["format_type"])

        elif step.name == "read_specific_file":
            result = read_specific_file()

        else:
            result = f"Unknown tool: {step.name}"

        function_results.append({
            "type": "function_result",
            "id": step.id,
            "name": step.name,
            "result": [
                {
                    "type": "text",
                    "text": json.dumps(result),
                }
            ],
        })

if function_results:
    final_interaction = client.interactions.create(
        model=GENAI_MODEL_NAME,
        previous_interaction_id=interaction.id, 
        input=function_results,
        tools=ALL_TOOLS,
    )
    print(final_interaction.output_text)

else:
    print(interaction.output_text)