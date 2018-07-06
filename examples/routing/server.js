const express = require('express');
const bodyParser = require('body-parser');

const app = express();

//app.use(express.static(__dirname));
app.use(bodyParser.urlencoded({ extended: true })); 

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html');
});

app.post('/submit', function(req, res) {
  console.log(req.body);
  if (req.body.name === 'Gokul') {
    res.sendFile(__dirname + '/home.html');
  }
});

app.listen(5500);