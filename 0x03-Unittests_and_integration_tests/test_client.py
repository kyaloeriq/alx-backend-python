#!/usr/bin/env python3
# Task: Write a unit test for the GithubOrgClient._public_repos_url method
# in client.py using unittest and patch.

import unittest
from unittest.mock import patch
from client import GithubOrgClient


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

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    def test_public_repos_url(self, org_name, expected_url):
        """Test that _public_repos_url returns the correct URL based on the
        mocked org property.
        """
        # Patch GithubOrgClient.org to return a known payload
        with patch.object(GithubOrgClient, 'org', new_callable=property) as mock_org:
            mock_org.return_value = {"repos_url": expected_url}
            client = GithubOrgClient(org_name)
            # Call _public_repos_url method
            result = client._public_repos_url
            # Assert the result is the expected URL
            self.assertEqual(result, expected_url)


if __name__ == "__main__":
    unittest.main()

