angular.module('myApp')
.service('myService', function() {
  this.someService = function() {
    console.log('Service ready');
    return 'hello';
  }
});