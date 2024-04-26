#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL with
    the email as a parameter, and displays the body of the response
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":

    url = sys.argv[1]
    email = {}
    email["email"] = {sys.argv[2]}
    content = urllib.parse.urlencode(email).encode("ascii")

    web_reqst = urllib.request.Request(url, content)
    with urllib.request.urlopen(web_reqst) as response:
        print(response.read().decode("utf-8"))
