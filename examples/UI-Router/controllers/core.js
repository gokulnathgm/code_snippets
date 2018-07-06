myApp = angular.module('myApp', ['ui.router', 'homeController', 'aboutController', 'newService']);

myApp.config(function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise('/');
  $stateProvider
  .state('/', {
    url: '/',
    templateUrl: 'views/home.html',
    controller: 'homeCtrl'
  })
  .state('about', {
    url: '/about',
    templateUrl: 'views/about.html',
    controller: 'aboutCtrl'
  })
});