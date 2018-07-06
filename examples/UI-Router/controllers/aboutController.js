angular.module('aboutController', [])
.controller('aboutCtrl', ['$state', '$scope', function ($state, $scope) {
  console.log('About Controller');

  $scope.home = function() {
    console.log('Clicked');
    $state.go('/');
  }
}]);