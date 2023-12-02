#!/usr/bin/python3
"""A script that:
- Accept a URL as input
- Initiate a request to the provided URL
- Display the decoded body of the response in utf-8
"""
import urllib.request
import urllib.error
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Decode and print the body of the response
        print(response.read().decode('utf-8'))

except urllib.error.HTTPError as e:
    # Print the HTTP error code
    print("Error code:", e.code)
