#!/usr/bin/python3

"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')
with urllib.request.urlopen(url, data=data) as response:
    print(response.read().decode('utf-8'))
