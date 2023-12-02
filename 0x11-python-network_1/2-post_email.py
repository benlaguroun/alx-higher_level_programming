#!/usr/bin/python3

"""A script that:
- Accept a URL as input
- Initiate a POST request to the provided URL
- Take an email address as a parameter
- Present the body of the response received from the server
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
