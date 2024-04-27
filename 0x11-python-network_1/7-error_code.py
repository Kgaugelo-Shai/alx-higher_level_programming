#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays the
    body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    reqst = requests.get(sys.argv[1])
    if int(reqst.status_code) < 400:
        print(reqst.text)
    else:
        print("Error code: {}".format(reqst.status_code))
