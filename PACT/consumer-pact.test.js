// Consumer 
const pact = require('@pact-foundation/pact').createV3();

describe('Consumer', () => {

  beforeAll(() => {
    // Set up Pact and define expectation  
    return pact.with({provider: 'MyProvider', port: 1234}).uponReceiving('a request for xyz').then(interaction => {
      interaction.withRequest({
        method: 'GET',
        path: '/api/xyz',
        headers: {Accept: 'application/json'}
      }).willRespondWith({
        status: 200,
        headers: {'Content-Type': 'application/json'},
        body: {results: 'xyz data'}
      });
    });
  });

  // Run test to confirm expectation met
  it('validates the response', () => {
    return fetch('http://localhost:1234/api/xyz', {
      headers: {Accept: 'application/json'}
    }).then(response => // assert status, data, etc. 
  });
  
  afterAll(() => pact.finalize());
});

// Provider 
const pact = require('@pact-foundation/pact').createServer({port: 9123});

describe('Provider', () => {

  beforeAll((done) => {
    server.listen(9123, done);
  });
  
  // Validate expected interactions
  it('validates the expectations of MyConsumer', () => {
    return pact.verifyProvider({provider: 'MyProvider'}).then(() => {
      // API responds as expected
    });
  });

  afterAll((done) => {
    server.close();
    done();
  });
});