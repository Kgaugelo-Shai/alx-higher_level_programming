#!/usr/bin/node
if (process.argv.length > 3) {
  const listInt = process.argv.slice(2).map(Number);
  const copyList = listInt.sort(function (a, b) { return b - a; })[1];
  console.log(copyList);
} else {
  console.log('0');
}
