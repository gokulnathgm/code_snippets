const path = require('path');
const mime = require('mime');
const express = require('express');
const fs = require('fs');

const app = express();

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.get('/download-text', function(req, res) {

  const file = __dirname + '/test-download';

  const filename = path.basename(file);
  const mimetype = mime.lookup(file);

  res.setHeader('Content-disposition', 'attachment; filename=' + filename);
  res.setHeader('Content-type', mimetype);

  const filestream = fs.createReadStream(file);
  filestream.pipe(res);
});

app.get('/download-pic', function(req, res) {

  const file = __dirname + '/friends.jpg';

  const filename = path.basename(file);
  const mimetype = mime.lookup(file);

  res.setHeader('Content-disposition', 'attachment; filename=' + filename);
  res.setHeader('Content-type', mimetype);

  const filestream = fs.createReadStream(file);
  filestream.pipe(res);
});

app.listen(5005);
console.log('App is listening on port 5005');