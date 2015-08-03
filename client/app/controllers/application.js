import Ember from 'ember';

export default Ember.Controller.extend({
  searchQuery: '',

  actions: {
    search: function(query) {
      return this.transitionToRoute('companies/search', query);
    }
  }
});
