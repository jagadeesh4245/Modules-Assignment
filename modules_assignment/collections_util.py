"""
Demonstrates collections.Counter from the collections module.
Purpose: Counts occurrences of elements in an iterable.
"""
from collections import Counter

def count_word_frequencies(words: list) -> dict:
    """Returns a dictionary containing frequencies of elements in a list."""
    return dict(Counter(words))