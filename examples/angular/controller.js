var spaceApp = angular.module('spaceApp', ['ngRoute']);

spaceApp.config(function($routeProvider) {
	$routeProvider

		.when('/', {
			templateUrl: 'home.html',
			controller: 'AppCtrl'
		})
		.when('/profile', {
			templateUrl: 'profile.html',
			controller: 'AppCtrl'
		})
		.otherwise({redirectTo: '/'});

		// $locationProvider.html5Mode(true);

});

spaceApp.controller('AppCtrl', function ($scope) {
	console.log("Controller ready!");
});
