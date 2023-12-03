#!/usr/bin/python3

""" A Python script that:
- Accepts a URL as input
- Sends a request to the specified URL
- displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
