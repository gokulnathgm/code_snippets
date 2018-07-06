var express = require('express');
var app = express();
var mongojs = require('mongojs');
var bodyParser = require('body-parser');
var db = mongojs('todo', ['todo']);

app.use(express.static(__dirname + "/public"));
app.use(bodyParser.json());

app.get('/todo', function(req, res) {
	console.log("Received GET request");

	db.todo.find(function (err,docs) {
		console.log(docs);
		res.json(docs);
	});
});

app.post('/todo', function(req, res) {
	console.log(req.body);
	db.todo.insert(req.body, function(err, doc) {
		res.json(doc);
	})
});


app.delete('/todo/:id', function(req, res) {
	var id = req.params.id;
	console.log(id);
	db.todo.remove({_id: mongojs.ObjectId(id)}, function(err, doc) {
		res.json(doc);
	});
});

app.get('/todo/:id', function(req, res) {
	var id = req.params.id;
	console.log(id);
	db.todo.findOne({_id: mongojs.ObjectId(id)}, function(err, doc) {
		res.json(doc);
	});
});

app.put('/todo/:id', function(req, res) {
	var id = req.params.id;
	console.log(req.body.action);
	db.todo.findAndModify({
		query: {_id: mongojs.ObjectId(id)},
		update: {$set: {action: req.body.action}}, new: true}, function(err, doc) {
			res.json(doc);
		}
	);
});

app.listen(4000);
console.log('App is listening on 3000');