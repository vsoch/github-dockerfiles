## Lapis

Lapis is a [Ruby On Rails template](http://guides.rubyonrails.org/rails_application_templates.html) to generate APIs that implement some good practices (to be published) that [Meedan](http://meedan.com) follows.

Currently based on Ruby 2.0+ and Rails 4.

### Features

* Documentation: README, license, licenses of dependencies, API endpoints, Swagger, diagrams (models and controllers)
* Tests: Basic testing framework that notifies Slack
* Authentication: webhooks and tokens
* Integrations: Code Climate (code quality and coverage) and Errbit (exception handling)
* API: Versioning and output control
* Clients: Provides a rake task that generates a gem that can be used by clients to integrate and to test
* Docker: Creates a Dockerfile ready to run the application

### How to use this template

* Define settings in `config.yml`
* Generate your application `rails new <application name> -m <path to lapis_template.rb>`
* For each model: create a method that creates an instance of this class at `lib/sample_data.rb`
* Your controllers should inherit from `BaseApiController`... generate them by running `rails g controller Api::V1::<ControllerName>`
* By default, all controller actions require a valid token... you can `skip_before_filter :authenticate_from_token!` in order to avoid that
* Document your API on files at `app/controllers/concerns/<controller name>_doc.rb` (remember to `include YourControllerDoc` in your controller). When documenting the possible inputs, you can use 'test' as the token.
* Add your routes to `config/routes.rb`
* You can apply this template to an existing application by running `rake rails:template LOCATION=<path to lapis_template.rb>`
* Generate the documentation: `rake lapis:docs`
* Generate a Ruby gem that wraps this API to be used and tested by clients, by running: `rake lapis:client:ruby`
* Generate a PHP package that wraps this API to be used and tested by clients, by running: `rake lapis:client:php`
* You can run the application right away on Docker by running  `rake lapis:docker:run` (you may need to update Dockerfile to fit your own needs)
* You can enter a running container by executing `rake lapis:docker:shell`

### Example

Check [this example of an API built on top of this framework](https://github.com/meedan/lapis-example/).
