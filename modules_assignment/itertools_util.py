"""
Demonstrates itertools.combinations from the itertools module.
Purpose: Generates r-length subsequences of elements from the input iterable.
"""
from itertools import combinations

def get_unique_pairs(items: list) -> list:
    """Returns a list of all unique length-2 combinations of elements."""
    return list(combinations(items, 2))