from datetime import datetime
from config import file_path
from common.chunking import (
    read_document
)


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

def read_specific_file():
    """
    Read only the Day 009 article.
    Implements the principle of least privilege by exposing exactly one file.
    """

    document_path = file_path(
        week=2,
        day=9,
        filename="article.md"
    )

    return read_document(document_path)

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

read_specific_file_function = {
    "type": "function",
    "name": "read_specific_file",
    "description": (
        "Read the contents of the single approved file. "
        "This tool cannot read arbitrary files."
    ),
    "parameters": {
        "type": "object",
        "properties": {}
    }
}

ALL_TOOLS = [
    calculator_function,
    datetime_function,
    read_specific_file_function,
]
