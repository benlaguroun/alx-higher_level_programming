#!/usr/bin/python3

""" A Python script designed to:
- Accept a URL as input
- Send a request to the specified URL
- Display the value of the X-Request-Id variable found in the response header.
"""
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

response = requests.post(url, data={'email': email})
print("Your email is:", response.text)
