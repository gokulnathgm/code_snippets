const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const userSchema = new Schema({
  name: String,
  email: String
});

const User = mongoose.model('userdata', userSchema);

module.exports = User;