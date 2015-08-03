import DS from 'ember-data';
import Ember from 'ember';
import moment from 'moment';

import config from 'dough-code-exercise/config/environment';

/* global window */

/**
 * Maintains a separate cache of price history data.
 *
 * This is a workaround for problems caused by singleton Routes/Controllers:
 * it lets us cache data from each company while ensuring that we don't show
 * data from the last company while the new stuff is loading.
 *
 * Another solution would be to make PriceHistory a model and let Ember Data
 * handle caching. This would be awkward, however, since we don't have IDs for
 * history records, or a full suite of RESTful routes for them -- and
 * implementing these would require a great deal of abstraction on top of the
 * Yahoo API.
 */
export default Ember.Service.extend({
  getPriceHistory: function(companyID) {
    if (companyID === undefined) {
      return undefined;
    }

    //if we already have a cached record, return that
    var cached = this.getCachedHistory(companyID);
    if (cached) {
      return Ember.RSVP.resolve(Ember.Object.create(cached));
    }

    var host = config.APP.API_HOST;
    var namespace = config.APP.API_NAMESPACE;
    var startDate = moment().subtract(30, 'days').format('YYYY-MM-DD');
    var historyURL = (host + '/' + namespace + '/companies/' + companyID +
      '/price-history/?start_date=' + startDate);

    return new Ember.RSVP.Promise((resolve, reject) => {
      Ember.$.getJSON(historyURL).then((response) => {
        this.setCachedHistory(companyID, response);
        resolve(this.getCachedHistory(companyID));
      });
    });
  },

  priceHistoryCache: Ember.Object.create(),

  getCachedHistory: function(companyID) {
    var found = window.localStorage.getItem('' + companyID);
    var timestamp = window.localStorage.getItem(companyID + '_time');

    if (
      found &&
      timestamp &&
      moment(timestamp) > moment().subtract(1, 'days')) {
      return JSON.parse(found);
    }

    window.localStorage.setItem('' + companyID, undefined);
    window.localStorage.setItem(companyID + '_time', undefined);
  },

  setCachedHistory: function(companyID, historyData) {
    var timestamp = moment().format();
    var historyJSON = JSON.stringify(historyData);

    window.localStorage.setItem('' + companyID, historyJSON);
    window.localStorage.setItem(companyID + '_time', timestamp);
  }
});
