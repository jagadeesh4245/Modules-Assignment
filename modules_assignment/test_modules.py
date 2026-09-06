"""
Unit tests for verifying each standard library wrapper function.
Run using: python -m unittest test_modules.py
"""
import unittest
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

class TestModuleWrappers(unittest.TestCase):

    def test_datetime(self):
        result = datetime_util.get_current_time_str()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_json(self):
        result = json_util.convert_to_json_string({"a": 1})
        self.assertEqual(result, '{"a": 1}')

    def test_random(self):
        original = [1, 2, 3, 4]
        result = random_util.shuffle_list_copy(original)
        self.assertEqual(sorted(result), sorted(original))

    def test_os(self):
        result = os_util.get_current_working_directory()
        self.assertIsInstance(result, str)

    def test_re(self):
        result = re_util.extract_digits("Item 42 and Item 99")
        self.assertEqual(result, ["42", "99"])

    def test_collections(self):
        result = collections_util.count_word_frequencies(["x", "x", "y"])
        self.assertEqual(result, {"x": 2, "y": 1})

    def test_itertools(self):
        result = itertools_util.get_unique_pairs([1, 2, 3])
        self.assertEqual(len(result), 3)

    def test_math(self):
        result = math_util.calculate_square_root(25)
        self.assertEqual(result, 5.0)

    def test_statistics(self):
        result = statistics_util.calculate_average([2, 4, 6])
        self.assertEqual(result, 4.0)

    def test_pathlib(self):
        result = pathlib_util.check_file_exists("main.py")
        self.assertIsInstance(result, bool)

if __name__ == "__main__":
    unittest.main()