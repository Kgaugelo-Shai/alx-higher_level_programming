#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let sqr = '';
      for (let j = 0; j < this.width; j++) {
        sqr += c;
      }
      console.log(sqr);
    }
  }
}

module.exports = Square;
