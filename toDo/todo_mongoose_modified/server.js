var express = require('express');
var app = express();
var mongoose = require('mongoose');
var bodyParser = require('body-parser');
var Todo = require('./models/todo');

mongoose.connect('mongodb://localhost/todo');

app.use(express.static(__dirname + "/public"));
app.use(bodyParser.json());

app.get('/todo', function(req, res) {
	console.log("Received GET request");

	Todo.find({}, function(err, todos) {
	if (err) throw err;

	console.log(todos);
	res.json(todos);
	});
});

app.post('/todo', function(req, res) {
	console.log(req.body);
	var newTodo = Todo({
		action: req.body.action,
		time: req.body.time
	});
	newTodo.save(function(err, doc) {
		if (err) throw err;

		res.json(doc);
	});
});


app.delete('/todo/:id', function(req, res) {
	var id = req.params.id;
	console.log(id);

	Todo.findOneAndRemove({_id: id}, function(err, doc) {
		if (err) throw err;

		res.json(doc);
	});
});

app.get('/todo/:id', function(req, res) {
	var id = req.params.id;
	console.log(id);

	Todo.find({_id: id}, function(err, todos) {
	if (err) throw err;

	console.log(todos);
	res.json(todos);
	});
});

app.put('/todo/:id', function(req, res) {
	var id = req.params.id;
	console.log(req.body.action);
	var action = req.body.action;

	Todo.findOneAndUpdate({_id: id}, {action: action}, function(err, docs) {
		if (err) throw err;

		console.log(docs);
		res.json(docs);
	});
});

app.post('/todo/done/:id', function(req, res) {
	console.log(req.params.id);
	var id = req.params.id;
	Todo.findOneAndUpdate({_id: id}, {done: true}, function(err, docs) {
		if (err) throw err;

		console.log(docs);
		res.json(docs);
	});
});

app.post('/todo/close/:id', function(req, res) {
	console.log('.......................................................');
	var id = req.params.id;
	Todo.remove({_id: id}, function(err, docs) {
		if (err) throw err;
		res.json(docs);
	});
});

app.listen(5000);
console.log('App is listening on 5000');