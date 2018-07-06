const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.urlencoded({ extended: true })); 

app.get('/home', function(req, res) {

  const number = 143;
  const fullUrl = req.protocol + '://' + req.get('host') + req.originalUrl;
  const newUrl = fullUrl + '/verify?' + number;

  const smtpTransport = nodemailer.createTransport('SMTP', {
    service: 'Gmail',
    auth: {
      user: 'employee.handler@gmail.com',
      pass: 'adminemployeespace'
    }
  });

  const mailOptions = {
    to: 'gokulnath@qburst.com',
    subject: 'Signup confirmation',
    text: 'Pls confirm this mail',
    html:  '<b><a href=' + newUrl + '>Click here to Verify</a></b>'
  }

  smtpTransport.sendMail(mailOptions, function(error, response) {
    if (error) {
      throw error
    }
    else {
      console.log('Message sent!');
    }
  })
  res.send('Home');
});

app.get('/home/verify', function(req, res) {
  console.log('Verifying.........');
  console.log(req._parsedUrl.query);
  res.sendFile(__dirname + '/reset.html');
});

app.post('/password', function(req, res) {
  console.log('Password........');
  console.log(req);
});

app.listen(6006);
console.log('App is listening on port 6006');