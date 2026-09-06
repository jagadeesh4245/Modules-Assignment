"""
Demonstrates re.findall from the re module.
Purpose: Finds all non-overlapping occurrences of a pattern in a string.
"""
import re

def extract_digits(text: str) -> list:
    """Extracts and returns all digits found in a text string."""
    return re.findall(r'\d+', text)