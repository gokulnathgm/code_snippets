function AppCtrl($scope, $http) {
	console.log("Controller OK");
	$scope.date = new Date();
	var refresh = function() {
		$scope.btnText = "Add"
		console.log($scope.btnText);
		$http.get('/todo').success(function(response) {
		console.log("Received the requested data");
		$scope.todo = response;
		$scope.tod = "";
		});
	};

	refresh();


	$scope.addTodo = function () {
		console.log($scope.tod);
		date = new Date();
		console.log(date);
		if ($scope.btnText == "Update") {
			console.log("Update function called");
			console.log($scope.tod._id);
			$http.put('/todo/' + $scope.tod._id, $scope.tod).success(function(response) {
				refresh();
			});
		}

		else {
			if ($scope.tod.action != undefined) {
				$scope.tod.time = date;
				$http.post('/todo', $scope.tod).success(function(response) {
				console.log(response);
				refresh();
			});
			};
		} 
	}	
	$scope.remove = function(id) {
		console.log(id);
		$http.delete('/todo/' + id).success(function(response) {
			refresh();
		});
	};

	$scope.edit = function(id) {
		$scope.btnText = "Update"
		console.log(id);
		$http.get('/todo/' + id).success(function(response) {
			$scope.tod = response;
		});
	};

}