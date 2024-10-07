#!/usr/bin/python3
"""Unittests for max_integer([..]) function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests"""

    def test_ordered_list(self):
        """Test ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test list beginning max value."""
        max_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_beginning), 4)

    def test_empty_list(self):
        """Test empty list."""
        empt = []
        self.assertEqual(max_integer(empt), None)

    def test_one_element_list(self):
        """Test list with a single element."""
        one_e = [7]
        self.assertEqual(max_integer(one_e), 7)

    def test_floats(self):
        """Test list of floats."""
        floatz = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floatz), 15.2)

    def test_ints_and_floats(self):
        """Test list of ints & floats."""
        intz_and_floatz = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(intz_and_floatz), 15.5)

    def test_string(self):
        """Test string."""
        strng = "Brennan"
        self.assertEqual(max_integer(strng), 'r')

    def test_list_of_strings(self):
        """Test list of strings."""
        stringz = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(stringz), "name")

    def test_empty_string(self):
        """Test empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
