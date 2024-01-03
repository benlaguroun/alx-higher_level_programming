#!/usr/bin/node
const fs = require('fs');

// Write the content to the file

fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});

