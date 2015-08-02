import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  symbol: DS.attr('string'),

  priceHistory: DS.hasMany('stock-price', { async: true }),
});
