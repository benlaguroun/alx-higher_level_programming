#!/usr/bin/node
const fs = require('fs');
const request = require('request');

// Make a GET request to the provided URL
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
