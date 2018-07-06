const https = require('https');
const fs = require('fs');
const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static('public'))

var secureServer = https.createServer({
  key: fs.readFileSync('./server.key'),
  cert: fs.readFileSync('./server.crt'),
  ca: fs.readFileSync('./ca.crt'),
  requestCert: true,
  rejectUnauthorized: false
}, app).listen('4040', function() {
  console.log("Secure Express server listening on port 4040");
});

app.post('/login', function(req, res) {
  console.log(req.body);
  res.end('Thanks!');
});
