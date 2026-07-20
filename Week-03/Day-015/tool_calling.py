from google import genai 

from config import (
    GEMINI_API_KEY,
    GENAI_MODEL_NAME,
)


client = genai.Client(api_key=GEMINI_API_KEY)

def calculator(expression: str):
    return eval(expression)

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

interaction = client.interactions.create(
    model=GENAI_MODEL_NAME,
    input="What is (56 * 5)/32?",
    tools=[calculator_function],
)

for step in interaction.steps:
    if step.type == "function_call":
        result = calculator(step.arguments["expression"])
        print(f"Tool Result: {result}")