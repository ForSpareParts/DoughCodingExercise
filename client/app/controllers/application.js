import Ember from 'ember';

export default Ember.Controller.extend({
  searchQuery: '',

  actions: {
    search: function(query) {
      return this.transitionTo('companies/search', query);
    }
  }
});
