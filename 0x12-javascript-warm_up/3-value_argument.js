#!/usr/bin/node

const [,, ...args] = process.argv;

if (args.length === 0) {
  console.log('No argument');
} else {
  const firstArgument = args[0];
  console.log(firstArgument);
}
