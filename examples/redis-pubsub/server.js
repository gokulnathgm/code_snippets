const redis = require("redis")
const subscriber = redis.createClient()
const publisher  = redis.createClient();

subscriber.on("message", function(channel, message) {
  console.log("Message '" + message + "' on channel '" + channel + "' arrived!")
});

subscriber.subscribe("asd");

publisher.publish("asd", "haaaaai");
publisher.publish("asd", "kthxbai");