from google import genai 
from datetime import datetime
import json
from config import (
    GEMINI_API_KEY,
    GENAI_MODEL_NAME,
)

# Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)
function_results = []

#Tools
def calculator(expression: str):
    return eval(expression)

def get_datetime(format_type: str = "datetime"):
    now = datetime.now()

    if format_type == "date":
        return now.strftime("%Y-%m-%d")

    elif format_type == "time":
        return now.strftime("%H:%M:%S")

    return now.strftime("%Y-%m-%d %H:%M:%S")

# Tool schemas 
calculator_function = {
    "type": "function",
    "name": "calculator",
    "description": "Perform arithmetic operations",
    "parameters": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "valuate a mathematical expression such as '12*63' or '(10+5)/3'."
            }
        },
        "required": ["expression"],
    },
}

datetime_function = {
    "type": "function",
    "name": "get_datetime",
    "description": "Returns the current system date, time, or both.",
    "parameters": {
        "type": "object",
        "properties": {
            "format_type": {
                "type": "string",
                "description": "Specify whether to return date, time, or datetime.",
                "enum": ["date", "time", "datetime"]
            }
        },
        "required": ["format_type"]
    }
}

interaction = client.interactions.create(
    model=GENAI_MODEL_NAME,
    input="Before answering, tell me the current date and time. Then calculate ((250 + 75) * 8) / 13.",
    tools=[calculator_function, datetime_function],
)

for step in interaction.steps:
    print(step)
    if step.type == "function_call":

        if step.name == "calculator":
            result = calculator(step.arguments["expression"])

        elif step.name == "get_datetime":
            result = get_datetime(step.arguments["format_type"])

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

final_interaction = client.interactions.create(
    model=GENAI_MODEL_NAME,
    previous_interaction_id=interaction.id, 
    input=function_results,
    tools=[calculator_function, datetime_function],
)

print(final_interaction.output_text)