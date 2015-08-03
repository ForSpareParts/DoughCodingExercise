import Ember from 'ember';
import DS from 'ember-data';

import config from 'dough-code-exercise/config/environment';

export default Ember.Controller.extend({
  priceHistory: null,
  priceHistoryObserver: function() {
    var host = config.APP.API_HOST;
    var namespace = config.APP.API_NAMESPACE;
    var id = this.get('model.id');
    var historyURL = (host + '/' + namespace + '/companies/' + id +
      '/price-history/?start_date=2015-06-01');

    var promise = new Ember.RSVP.Promise((resolve, reject) => {
      Ember.$.getJSON(historyURL).then((response) => {
        this.set('priceHistory', Ember.Object.create(response));
      });
    });

    return new DS.PromiseObject({promise: promise});
  }.observes('model.id'),

  chartData: function() {
    if (!this.get('chartDataset') || !this.get('chartLabels')) {
      return undefined;
    }

    return {
      labels: this.get('chartLabels'),
      datasets: [this.get('chartDataset')]
    };
  }.property('chartDataset', 'chartLabels'),

  chartLabels: function() {
    return this.get('priceHistory.dates');
  }.property('priceHistory.dates'),

  chartDataset: function() {
    return {
      label: 'Price History',
      fillColor: 'rgba(151,187,205,0.2)',
      strokeColor: 'rgba(151,187,205,1)',
      pointColor: 'rgba(151,187,205,1)',
      pointStrokeColor: '#fff',
      pointHighlightFill: '#fff',
      pointHighlightStroke: 'rgba(151,187,205,1)',
      data: this.get('priceHistory.prices')
    };
  }.property('priceHistory.prices'),
});
