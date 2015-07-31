import { moduleForModel, test } from 'ember-qunit';

moduleForModel('stock-price', 'Unit | Model | stock price', {
  // Specify the other units that are required for this test.
  needs: ['model:company']
});

test('it exists', function(assert) {
  var model = this.subject();
  // var store = this.store();
  assert.ok(!!model);
});
