angular.module('myApp', [])
.controller('myCtrl', ['myService', function(myService) {
  console.log('controller ready');
  var msg = myService.someService();
  console.log(msg);
}]);