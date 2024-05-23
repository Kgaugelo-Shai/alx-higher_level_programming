#!/usr/bin/node
const request = require('request');

const link = process.argv[2];
request.get(link).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
