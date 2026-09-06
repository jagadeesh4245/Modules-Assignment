"""
Main driver script to execute and showcase all 10 module implementations.
"""
import datetime_util
import json_util
import random_util
import os_util
import re_util
import collections_util
import itertools_util
import math_util
import statistics_util
import pathlib_util

def run_all():
    print("1. datetime:", datetime_util.get_current_time_str())
    print("2. json:", json_util.convert_to_json_string({"name": "Alice", "role": "Developer"}))
    print("3. random:", random_util.shuffle_list_copy([1, 2, 3, 4, 5]))
    print("4. os:", os_util.get_current_working_directory())
    print("5. re:", re_util.extract_digits("Order #1234 on 2026-09-06"))
    print("6. collections:", collections_util.count_word_frequencies(["apple", "banana", "apple"]))
    print("7. itertools:", itertools_util.get_unique_pairs(['A', 'B', 'C']))
    print("8. math:", math_util.calculate_square_root(16))
    print("9. statistics:", statistics_util.calculate_average([10, 20, 30, 40]))
    print("10. pathlib:", pathlib_util.check_file_exists("main.py"))

if __name__ == "__main__":
    run_all()