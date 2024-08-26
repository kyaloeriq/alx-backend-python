#!/usr/bin/env python3
# Task: Write unit tests for utils functions using unittest and parameterized.
# Includes tests for access_nested_map, get_json, and memoize decorator.

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with different inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for missing keys."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))

class TestGetJson(unittest.TestCase):
    """Test case for get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns the expected result."""
        # Configure the mock to return a response with a .json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call get_json with the test URL
        result = get_json(test_url)

        # Assert that the mock's get method was called exactly once with the test_url
        mock_get.assert_called_once_with(test_url)

        # Assert that the result is equal to the test_payload
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator."""

    def test_memoize(self):
        """Test memoize caches results correctly."""

        class TestClass:
            """Class with a method to be memoized."""

            def a_method(self):
                """Simple method that returns a value."""
                return 42

            @memoize
            def a_property(self):
                """Method decorated with memoize."""
                return self.a_method()

        # Create an instance of TestClass
        obj = TestClass()

        # Replace a_method with a Mock to track calls
        with unittest.mock.patch.object(obj, 'a_method', wraps=obj.a_method) as mock_method:
            # First call to a_property, should call a_method
            result_first_call = obj.a_property()
            mock_method.assert_called_once()  # a_method should have been called once
            self.assertEqual(result_first_call, 42)

            # Second call to a_property, should return cached result
            result_second_call = obj.a_property()
            mock_method.assert_called_once()  # a_method should not be called again
            self.assertEqual(result_second_call, 42)

if __name__ == "__main__":
    unittest.main()
