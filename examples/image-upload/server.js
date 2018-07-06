const express = require('express');
const fs = require('fs');
const bodyParser = require('body-parser');
const multer = require('multer');

const app = express();
app.use(bodyParser.urlencoded({ extended: true })); 

const upload = multer({
  dest: __dirname + '/uploads/',
});

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.post('/upload', upload.single('image'), function(req, res) {
  console.log(req.file + '\n\n');
  console.log(req.body);
  fs.rename(req.file.path, req.file.destination + '/' + req.file.originalname);
  res.end('uploaded');
});

app.listen(6060);
console.log('App -> 6060');