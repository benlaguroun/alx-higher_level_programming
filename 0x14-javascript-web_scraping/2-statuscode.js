#!/usr/bin/node
const request = require('request');

// Make a GET request and display the status code
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});

