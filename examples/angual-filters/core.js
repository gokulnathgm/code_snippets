const myApp = angular.module('myApp', []);

myApp.controller('myCtrl', ['$scope', function ($scope) {
  console.log('controller ready');
  const names = [
    {Fname: 'Gokul', Lname: 'Nath'}, 
    {Fname: 'Sachin', Lname: 'Tendulkar'}, 
    {Fname: 'Brad', Lname: 'Pitt'}, 
    {Fname: 'Kate', Lname: 'Winslet'},
    {Fname: 'Oprah', Lname: 'Winfrey'}, 
    {Fname: 'Raj', Lname: 'Kumar'}
    ];
    console.log(names);
    $scope.names = names;
}]);