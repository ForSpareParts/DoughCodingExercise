import Ember from 'ember';

export default Ember.Route.extend({
  model: function(params) {
    return this.store.query('company', {name: params.name})

    .then((companies) => {
      //there should only be one in this list
      return companies.get('firstObject');
    })
  },

  afterModel: function(model) {
    //cache all stock prices in the store to prevent future GETs:
    return this.store.query('stock-price', {company: model.get('id')});
  }
});
