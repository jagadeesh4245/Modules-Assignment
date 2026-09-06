"""
Demonstrates pathlib.Path.exists from the pathlib module.
Purpose: Checks whether a given path or file exists.
"""
from pathlib import Path

def check_file_exists(file_path: str) -> bool:
    """Returns True if the specified path exists, False otherwise."""
    return Path(file_path).exists()