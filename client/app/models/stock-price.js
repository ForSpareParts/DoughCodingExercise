import DS from 'ember-data';

export default DS.Model.extend({
  company: DS.belongsTo('company', {async: true}),
  time: DS.attr('date'),
  price: DS.attr('number')
});
