#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and displays the
    value of the variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    reqst = requests.get(sys.argv[1])
    print(reqst.headers.get("X-Request-Id"))
