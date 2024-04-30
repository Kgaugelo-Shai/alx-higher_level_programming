#!/usr/bin/node
const fs = require('fs');
const f1 = process.argv[2];
const f2 = process.argv[3];
const f3 = process.argv[4];

function readfiles (file) {
  return fs.readFileSync(file);
}

function writefiles (file, content) {
  fs.writeFile(file, content, (err) => {
    if (err) {
      return console.error(err);
    }
  });
}
let newFile = '';
newFile = readfiles(f1);
dnewFile += readfiles(f2);
writefiles(f3, newFile);
