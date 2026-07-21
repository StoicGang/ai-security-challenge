from datetime import datetime


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

ALL_TOOLS = [
    calculator_function,
    datetime_function,
]