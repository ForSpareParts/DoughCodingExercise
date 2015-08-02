import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route('companies/search', {path: '/companies/search/:query'});
  this.route('company', {path: '/companies/:name'});
});

export default Router;
