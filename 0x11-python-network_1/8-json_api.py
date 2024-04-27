#!/usr/bin/python3
""" Script in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        reqst = requests.post(url, data={'q': sys.argv[1]})
    else:
        reqst = requests.post(url, data={'q': ""})
    try:
        response = reqst.json()
        if response:
            print("[{}] {}".format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
