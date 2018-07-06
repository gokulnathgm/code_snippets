
var express = require('express');
var app = express();
app.set("views", __dirname + "/views");
app.set("view engine", "jade");
 
var elasticsearch = require('elasticsearch');
var client = new elasticsearch.Client(); 
 
app.get('/:search_query', function(request, response) {
  client.search({
    index: 'blog',
    body: {
      query: {
        match: {
          body: request.param('search_query')
        }
      }
    },
    fields: ['user', 'postDate', 'body', 'title']
  }, function (error, search_response) {
    if (error) {
      // handle error
      return;
    }
    response.render('search_results', {
      results: search_response.hits.hits
    });
  });
});
 
var port = 9200;
app.listen(port, function() {
  console.log("Listening on " + port);
});