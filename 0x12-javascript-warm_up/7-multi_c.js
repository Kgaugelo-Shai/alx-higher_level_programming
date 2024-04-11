#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(process.argv[2]);
  let count = 0;
  while (count < x) {
    console.log('C is fun');
    count++;
  }
}
