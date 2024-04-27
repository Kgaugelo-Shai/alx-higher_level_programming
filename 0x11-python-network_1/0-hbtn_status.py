#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request


if __name__ == "__main__":
    web_reqst = urllib.request.Request("http://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(web_reqst) as response:
        cont = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(cont)))
    print("\t- content: {}".format(cont))
    print("\t- utf8 content: {}".format(cont.decode("utf8")))
