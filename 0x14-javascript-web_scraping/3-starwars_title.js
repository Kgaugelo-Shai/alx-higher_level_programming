#!/usr/bin/node

const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api/films/';
const episode = process.argv[2];

request(URL + episode, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
