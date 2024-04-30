#!/usr/bin/node
const { readFile, writeFile } = require('fs');
const { argv } = require('process');

const contents = (file) => {
  return readFile(file, 'utf8');
};

const concatStr = contents(argv[2]) + '' + contents(argv[3]);

writeFile(argv[4], concatStr, 'utf8', err => {
  if (err) throw err;
});
