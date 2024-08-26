#!/usr/bin/env python3
# Task: Write unit tests for the GithubOrgClient.public_repos method in client.py
# using unittest and patch.

import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class."""

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

    @parameterized.expand([
        ("google", "apache-2.0", ["repo1"]),
        ("abc", "mit", ["repoA"]),
    ])
    @patch('client.get_json')
    def test_public_repos_with_license(self, org_name, license, expected_repos, mock_get_json):
        """Test that GithubOrgClient.public_repos with a license argument returns the correct repos list."""
        # Set up the mock return value for get_json
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"spdx_id": "apache-2.0"}},
            {"name": "repo2", "license": {"spdx_id": "mit"}},
            {"name": "repo3", "license": {"spdx_id": "apache-2.0"}}
        ]
        
        # Patch _public_repos_url to return a specific URL
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=property) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/{}/repos".format(org_name)
            
            # Create an instance of GithubOrgClient
            client = GithubOrgClient(org_name)
            
            # Call the public_repos method with license argument
            result = client.public_repos(license=license)
            
            # Assert public_repos returns the expected repos list based on the license filter
            self.assertEqual(result, expected_repos)
            
            # Assert _public_repos_url was called once
            mock_public_repos_url.assert_called_once()
            
            # Assert get_json was called once with the mocked URL
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/{}/repos".format(org_name)
            )


if __name__ == "__main__":
    unittest.main()
