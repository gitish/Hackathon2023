## Pact Contract Testing
This Docker container executes Pact contract tests between a consumer and provider service.

### Container Details
* Base image: Node 12 Alpine
* Packages included:
    * @pact-foundation/pact
    * Jest, supertest (dev dependencies)
* Exposed port: 1234

### Quickstart
Build container image
``` 
docker build -t myorg/pact-test .
```

Run consumer tests
```
docker run -it --name consumer myorg/pact-test npm run test:consumer
```

Start provider API server
```
docker run -d -p 3000:3000 myorg/pact-test npm run server
```


Execute provider verification
```
docker run --network=host myorg/pact-test npm run test:provider
```


The provider verification sends requests to the provider API container to validate if expected contracts are satisfied.

### More Info
Port 1234 is used for Pact's mock server to perform consumer tests
Jest is included as the test runner with helpful extensions
This Docker setup helps easily verify integration pacts between the linked consumer-provider services.