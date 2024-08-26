#!/usr/bin/env python3
# Task: Write a unit test for the GithubOrgClient class in client.py

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Set up the mock return value
        mock_get_json.return_value = {"login": org_name}

        # Create an instance of GithubOrgClient with the org_name
        client = GithubOrgClient(org_name)

        # Call the .org method
        result = client.org

        # Assert get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
                )

        # Assert the result is what we expect
        self.assertEqual(result, {"login": org_name})


if __name__ == "__main__":
    unittest.main()
