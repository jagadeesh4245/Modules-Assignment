"""
Demonstrates datetime.datetime.now from the datetime module.
Purpose: Retrieves the current local date and time.
"""
from datetime import datetime

def get_current_time_str() -> str:
    """Returns the current date and time formatted as a string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")