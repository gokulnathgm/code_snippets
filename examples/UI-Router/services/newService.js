angular.module('newService', [])
.service('service', function () {
  this.someService = function() {
    return "Home/About";
  }
});