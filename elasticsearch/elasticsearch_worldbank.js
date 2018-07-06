var fs = require('fs');
var es = require('elasticsearch');

var client = new es.Client({
  host: 'localhost:9200'
});

fs.readFile('world_bank.json', {encoding: 'utf-8'}, function(err, data) {
  if (err) { throw err; }

  // Build up a giant bulk request for elasticsearch.
  bulk_request = data.split('\n').reduce(function(bulk_request, line) {
    var obj, post;

    try {
      obj = JSON.parse(line);
    } catch(e) {
      console.log('Done reading');
      return bulk_request;
    }

    // Rework the data slightly
    post = {
      id: obj._id.$oid, // Was originally a mongodb entry
      countryname: obj.countryname,
      approvalfy: obj.approvalfy,
      sector: obj.sector
    };

    bulk_request.push({index: {_index: 'blog', _type: 'post', _id: post.id}});
    bulk_request.push(post);
    return bulk_request;
  }, []);

  // A little voodoo to simulate synchronous insert
  var busy = false;
  var callback = function(err, resp) {
    if (err) { console.log(err); }

    busy = false;
  };

  // Recursively whittle away at bulk_request, 1000 at a time.
  var perhaps_insert = function(){
    if (!busy) {
      busy = true;
      client.bulk({
        body: bulk_request.slice(0, 1000)
      }, callback);
      bulk_request = bulk_request.slice(1000);
      console.log(bulk_request.length);
    }

    if (bulk_request.length > 0) {
      setTimeout(perhaps_insert, 10);
    } else {
      console.log('Inserted all records.');
      var stdin = process.openStdin();
    }
  };

  perhaps_insert();

  client.search({
  index: 'blog',
  type: 'post',
  body: {
    query: {"match": {"_all": 'Republic of Kenya'}}//query: {"match": {"_all": "Republic of Kenya"}}
  }
}).then(function (resp) {
    var hits = resp.hits.hits;
    var len = Object.keys(hits).length;

    for (i=0; i<len; i++){
      console.log(hits[i]['_source']['approvalfy'] + "\t" + hits[i]['_source']['sector'][0]['Name']);
    }
    
}, function (err) {
    console.trace(err.message);
});

});