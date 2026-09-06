"""
Demonstrates json.dumps from the json module.
Purpose: Converts a Python dictionary into a JSON-formatted string.
"""
import json

def convert_to_json_string(data: dict) -> str:
    """Serializes a Python dictionary into a JSON string."""
    return json.dumps(data)