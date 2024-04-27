#!/usr/bin/python3
"""  list 10 commits (from the most recent to oldest) of the repository “rails”
     by the user “rails. You must use the GitHub API, here is the documentation
     https://developer.github.com/v3/repos/commits/
     Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}'.format(sys.argv[1], sys.argv[2])

    reqst = request.get(url)
    commit_js = reqst.json()
    for c in range(10):
        print("{}: {}".format(
            commit_js[c].get("sha"),
            commit_js[c].get("commit").get("author").get("name")))
