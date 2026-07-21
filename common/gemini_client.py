from google import genai

from config import GEMINI_API_KEY, MODEL_NAME

client = genai.Client(api_key=GEMINI_API_KEY)


def create_interaction(user_prompt: str, tools: list):
    return client.interactions.create(
        model=MODEL_NAME,
        input=user_prompt,
        tools=tools,
    )


def continue_interaction(previous_interaction_id: str, function_results: list):
    return client.interactions.create(
        previous_interaction_id=previous_interaction_id,
        input=function_results,
    )


def get_function_calls(interaction):
    return [
        step
        for step in interaction.steps
        if step.type == "function_call"
    ]