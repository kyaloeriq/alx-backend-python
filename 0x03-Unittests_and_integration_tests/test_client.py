#!/usr/bin/env python3
# Task: Write a unit test for the GithubOrgClient.public_repos method in client.py
# using unittest, patch, and a mock payload.

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
        ("google", ["repo1", "repo2"]),
        ("abc", ["repoA", "repoB"]),
    ])
    @patch('client.get_json')
    def test_public_repos(self, org_name, expected_repos, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the correct repos list."""
        # Set up the mock return value for get_json
        mock_get_json.return_value = expected_repos
        
        # Patch _public_repos_url to return a specific URL
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=property) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/{}/repos".format(org_name)
            
            # Create an instance of GithubOrgClient
            client = GithubOrgClient(org_name)
            
            # Call the public_repos method
            result = client.public_repos
            
            # Assert public_repos returns the expected repos list
            self.assertEqual(result, expected_repos)
            
            # Assert _public_repos_url was called once
            mock_public_repos_url.assert_called_once()
            
            # Assert get_json was called once with the mocked URL
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/{}/repos".format(org_name)
            )

if __name__ == "__main__":
    unittest.main()
