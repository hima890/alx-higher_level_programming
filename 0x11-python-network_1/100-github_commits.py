#!/usr/bin/python3
"""
A Python script that takes 2 arguments (repository name and owner name) and
uses the GitHub API to list 10 commits (from the most recent to oldest)
of the specified repository.
Print all commits by: <sha>: <author name> (one by line).
"""

if __name__ == "__main__":
    import requests
    import sys

    # Get the user info
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API URL to get commits of the repository
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    try:
        # Send the GET request to the GitHub API
        response = requests.get(url, params={'per_page': 10})

        # Raise an error for bad status codes
        response.raise_for_status()

        # Parse the JSON response
        commits = response.json()

        # Print the sha and author name for each commit
        for commit in commits:
            # Get the commit sha
            sha = commit.get('sha')
            # Get the author name from the commit
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")

    # handle exceptions
    except requests.exceptions.HTTPError as e:
        print(
                f"HTTP error occurred: {e.response.status_code}
                {e.response.reason}"
            )
    except requests.exceptions.RequestException as e:
        print(f"Request error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
