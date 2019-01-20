# RamlParser

Welcome to your new gem! In this directory, you'll find the files you need to be able to package up your Ruby library into a gem. Put your Ruby code in the file `lib/api_specs`. To experiment with that code, run `bin/console` for an interactive prompt.

TODO: Delete this and the text above, and describe your gem

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'api_specs'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install api_specs

## Usage

TODO: Write usage instructions here

## Development

After checking out the repo, run `bin/setup` to install dependencies. Then, run `rake spec` to run the tests. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and tags, and push the `.gem` file to [rubygems.org](https://rubygems.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/[USERNAME]/api_specs. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

# SemaphoreClientGenerator

Welcome to your new gem! In this directory, you'll find the files you need to be able to package up your Ruby library into a gem. Put your Ruby code in the file `lib/semaphore_client_generator`. To experiment with that code, run `bin/console` for an interactive prompt.

TODO: Delete this and the text above, and describe your gem

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'semaphore_client_generator'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install semaphore_client_generator

## Usage

Running `bundle exec rake generate` will take the specification from
../api.json and the source code from ./client_source, use it to
generate a new version of the client and will place it inside ./output.

For using custom paths, see the method that is called from the above-mentioned
Rake task.

## Development

After checking out the repo, run `bin/setup` to install dependencies. Then, run `rake spec` to run the tests. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and tags, and push the `.gem` file to [rubygems.org](https://rubygems.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/[USERNAME]/semaphore_client_generator. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the SemaphoreClientGenerator project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/[USERNAME]/semaphore_client_generator/blob/master/CODE_OF_CONDUCT.md).
# Semaphore Client

[![Build Status](https://semaphoreci.com/api/v1/projects/a07c1244-d53a-462d-9c3b-0794881935df/1452738/badge.svg)](https://semaphoreci.com/renderedtext/semaphore-client)

![Semaphore logo](https://d1dkupr86d302v.cloudfront.net/assets/application_bootstrap/layout/semaphore-logo-a6d954e176b6975b511f314a0cc808dc94a8030210077e3a6e904fbe69dc5354.svg)

Semaphore Client is used to access Semaphore's API v2.

For more info about Semaphore see <https://www.semaphoreci.com>

For more info about Semaphore's API v2 see
<http://semaphoreci.com/docs/api-v2-overview.html>

## Issues

For problems directly related to the Client, [add an issue on GitHub](https://github.com/renderedtext/semaphore-client/issues/new).

For other issues, [submit a support ticket](https://semaphoreci.com/support).
