var elasticsearch = require('elasticsearch');
var client = new elasticsearch.Client({
  host: 'localhost:9200',
  //log: 'trace'
});

client.ping({
  // ping usually has a 3000ms timeout
  requestTimeout: Infinity,

  // undocumented params are appended to the query string
  hello: "elasticsearch!"
}, function (error) {
  if (error) {
    console.trace('elasticsearch cluster is down!');
  } else {
    console.log('All is well');
  }
});

/*client.search({
  q: 'pants'
}).then(function (body) {
  var hits = body.hits.hits;
}, function (error) {
  console.trace(error.message);
});*/

client.search({
  index: 'blog',
  type: 'post',
  body: {
    query: {"match": {"_all": "search"}}
  }
}).then(function (resp) {
    var hits = resp.hits.hits;
    console.log(hits[0]['_source']['body'])
    console.log(len(hits));
}, function (err) {
    console.trace(err.message);
});