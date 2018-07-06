
var express = require('express');
var fs = require('fs');
var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var app = express();

// img path
var imgPath = __dirname + '/friends.jpg';

// connect to mongo
mongoose.connect('mongodb://localhost/mongo-image');

// example schema
var schema = new Schema({
  img: { data: Buffer, contentType: String }
});

// our model
var A = mongoose.model('image', schema);

    // store an img in binary in mongo

A.img.data = fs.readFileSync(imgPath);
A.img.contentType = 'image/jpg';
A.save(function (err, a) {
  if (err) throw err;
  console.log(a);
  console.error('saved img to mongo');
}); 

app.listen('8080');
console.log('listening -> 8080');

