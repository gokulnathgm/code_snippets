const express = require('express');
var bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true })); 

app.get('/', function(req, res) {
  console.log('GET Request');
  res.sendFile(__dirname + '/index.html');
})

app.post('/login', function(req, res) {
  // console.log('POST Request');
  // const body = req._parsedUrl.query;  
  // console.log('Request body: \n\n' + body);
  // console.log(req._parsedUrl.query);
  console.log(req.body);
});

app.listen(7000);
console.log('app -> 7000');