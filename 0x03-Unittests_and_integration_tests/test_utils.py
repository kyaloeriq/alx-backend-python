#!/usr/bin/env python3
# Task: Write a unit test for the utils.get_json function using unittest and patch.

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json

class TestGetJson(unittest.TestCase):
    """Test case for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected result with a patched requests.get."""
        # Create a Mock object with the .json method returning the test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call get_json with the test_url
        result = get_json(test_url)

        # Assert that requests.get was called once with the test_url
        mock_get.assert_called_once_with(test_url)

        # Assert that the result is equal to the test_payload
        self.assertEqual(result, test_payload)

if __name__ == "__main__":
    unittest.main()
