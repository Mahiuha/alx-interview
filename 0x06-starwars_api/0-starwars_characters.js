#!/usr/bin/node
// Print all characters of a star wars movie

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');

request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
  }
  response = JSON.parse(body);
  for (const character of response.characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
