"""
Demonstrates statistics.mean from the statistics module.
Purpose: Calculates the arithmetic mean (average) of numbers.
"""
import statistics

def calculate_average(data: list) -> float:
    """Returns the arithmetic mean of a list of numbers."""
    return statistics.mean(data)