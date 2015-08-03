import Ember from 'ember';

export default Ember.Controller.extend({

  stockPrices: Ember.inject.service('stock-prices'),

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

  priceHistory: null,
  priceHistoryObserver: function() {
    this.set('priceHistory', null);

    return this.get('stockPrices').getPriceHistory(this.get('model.id'))
    .then((priceHistory) => this.set('priceHistory', priceHistory));
  }.observes('model.id'),
});
