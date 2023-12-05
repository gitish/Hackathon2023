package main

import (
	"log"
	"net/http"

	"github.com/99designs/gqlgen/graphql/handler"
	"github.com/99designs/gqlgen/graphql/playground"
)

func main() {

	// Define GraphQL schema
	schema := `
    type Query {
      hello: String!
    }
  `

	// Set up GraphQL endpoint
	srv := handler.NewDefaultServer(NewExecutableSchema(Config{Resolvers: &Resolver{}}))

	// Playground endpoint
	http.Handle("/", playground.Handler("GraphQL playground", "/query"))

	// GraphQL endpoint
	http.Handle("/query", srv)

	log.Printf("GraphQL server running on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

// Resolver implements query resolvers
type Resolver struct{}

func (r *Resolver) Hello() string {
	return "Hello world!"
}
