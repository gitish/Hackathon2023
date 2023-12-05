// Define GraphQL schema
var schema = `
    type Query {
      books: [Book!]!  
      book(id: ID!): Book
    }

    type Book {
      id: ID!  
      name: String!
      author: Author!
    }

    type Author {
      id: ID!
      name: String!
    }
`

// Resolver implementation
type Resolver struct {
}

func (r *Resolver) GetBooks() []Book {
	// Logic to fetch books
	return books
}

func (r *Resolver) GetBook(ctx context.Context, id string) (Book, error) {
	// Lookup single book by id
	book := findBook(id)
	return book, nil
}

type Book struct {
	ID     string
	Name   string
	Author Author
}

type Author struct {
	ID   string
	Name string
}

// Additional helper methods and data logic

func findBook(id string) Book {
	// Code to get book from datastore
	return book
}

// This shows how you can define the queries and any auxiliary data types in the schema,
// while writing corresponding resolver functions to fetch the actual data from databases/APIs etc. and return the response.