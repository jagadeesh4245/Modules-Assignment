"""
Demonstrates random.shuffle from the random module.
Purpose: Shuffles a copy of a list without modifying the original.
"""
import random

def shuffle_list_copy(items: list) -> list:
    """Shuffles a copy of the provided list and returns the shuffled copy."""
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled
