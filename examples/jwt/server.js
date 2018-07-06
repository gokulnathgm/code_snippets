const express = require('express');
const app = express();
const jwt = require('jsonwebtoken');

user = {
  username: 'goks',
  password: 'admin'
};

var token = jwt.sign(user, 'ok_jarvis');
console.log(token);

app.get('/', function(req, res) {
  const decoded = jwt.verify(token, 'ok_jarvis', function(err, decoded) {
    console.log(typeof decoded);
  });
});

app.listen('3595');
