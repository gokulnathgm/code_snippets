const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/mastelio');

const User = require('./model');

const user = User({
  name: 'test',
  email: 'testing'
});

user.save(function(err, response) {
  if (err) {
    throw err;
  }
  else {
    console.log(response);
  }
});

// User.find({name: 'test'}, function(err, response) {
//   if (err) {
//     throw err;
//   }
//   console.log(response);
// });