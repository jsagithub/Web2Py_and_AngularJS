//Note AngularJS code is included within the layout
var demoAngular = angular.module('demoAngular', []);

demoAngular.config(function($interpolateProvider) {
    //allow Web2py views and Angular to co-exist
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
