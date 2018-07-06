angular.module('homeController', [])
.controller('homeCtrl', ['$scope', '$state', 'service', function ($scope, $state, service) {
  console.log('Home Controller');
  $scope.property = true;
  const msg = service.someService();
  console.log(msg);
  
  $scope.about = function() {
    console.log('Clicked');
    $state.go('about');
  }

  $scope.enable = function() {
    console.log('Enable');
    $scope.property = false;
  }

}]);