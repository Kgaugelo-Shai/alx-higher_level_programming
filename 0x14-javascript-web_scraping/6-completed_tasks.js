#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error == null) {
    const res = {};
    const js = JSON.parse(body);
    for (let i = 0; i < js.length; i++) {
      if (js[i].completed === true) {
        if (res[js[i].userId] === undefined) {
          res[js[i].userId] = 0;
        }
        res[js[i].userId]++;
      }
    }
    console.log(res);
  }
});
