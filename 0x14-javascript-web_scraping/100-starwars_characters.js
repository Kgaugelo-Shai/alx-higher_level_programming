#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const urlLink = 'https://swapi-api.hbtn.io/api/films/';
request.get(urlLink + movieId, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const content = JSON.parse(body);
  const data = content.characters;
  for (const i of data) {
    request.get(i, function (error, response, body1) {
      if (error) {
        console.log(error);
      }
      const newData = JSON.parse(body1);
      console.log(newData.name);
    });
  }
});
