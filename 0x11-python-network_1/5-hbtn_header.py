#!/usr/bin/python3

""" Shows the value of the X-Request-Id header variable in the response from a specified URL """
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
