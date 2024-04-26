#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays the
    body of the response
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(web_reqst) as response:
            content = response.read()

        print(content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
