## Lapis Example

An application to be used as an example for Lapis framework

### Installation

#### Non-Docker-based

* Configure `config/config.yml`, `config/database.yml`, `config/initializers/errbit.rb` and `config/initializers/secret_token.rb` (check the example files)
* Run `bundle install`
* Run `bundle exec rake db:migrate`
* Create an API key: `bundle exec rake lapis:api_keys:create`
* Start the server: `rails s`
* Go to [http://localhost:3000/api](http://localhost:3000/api) and use the API key you created

#### Docker-based

* You can also start the application on Docker by running `rake lapis:docker:run` (it will run on port 3000 and your local hostname) - you first need to create an API key after entering the container (`lapis:docker:shell`) before using the web interface

### API

#### GET /api/languages/classify

Use this method in order to identify the language of a given text

**Parameters**

* `text`: Text to be classified _(required)_

**Response**

200: Text language
```json
{
  "type": "language",
  "data": "english"
}
```

400: Parameter "text" is missing
```json
{
  "type": "error",
  "data": {
    "message": "Parameters missing",
    "code": 2
  }
}
```

401: Access denied
```json
{
  "type": "error",
  "data": {
    "message": "Unauthorized",
    "code": 1
  }
}
```

### Running the tests

* `bundle install --without nothing`
* `RAILS_ENV=test bundle exec rake db:migrate`
* `RAILS_ENV=test bundle exec rake test:coverage`

### Integration

Other applications can communicate with this service (and test this communication) using the client library, which can be automatically generated.

### Rake tasks

There are rake tasks for a few tasks (besides Rails' default ones). Run them this way: `bundle exec rake <task name>`

* `test:coverage`: Run all tests and calculate test coverage
* `application=<application name> lapis:api_keys:create`: Create a new API key for an application
* `lapis:api_keys:delete_expired`: Delete all expired keys
* `lapis:error_codes`: List all error codes that this application can return
* `lapis:licenses`: List the licenses of all libraries used by this project
* `lapis:client:ruby`: Generate a client Ruby gem, that allows other applications to communicate and test this service
* `lapis:client:php`: Generate a client PHP library, that allows other applications to communicate and test this service
* `lapis:docs`: Generate the documentation for this API, including models and controllers diagrams, Swagger, API endpoints, licenses, etc.
* `lapis:docker:run`: Run the application in Docker
* `lapis:docker:shell`: Enter the Docker container
* `lapis:graphql:update_schema_json`: Update the schema JSON
* `swagger:docs:markdown`: Generate the documentation in markdown format

### GraphQL

There is a GraphQL interface that exposes the data model as a GraphQL schema. The GraphQL files should be under `app/graph`.

You can update the schema file by running `rake lapis:graphql:update_schema_json`.

### Credits

Meedan (hello@meedan.com)
