![Minke](http://minke.rocks/img/minke_logo.png)
# Minke::Generators::Swift

[![Build Status](https://travis-ci.org/nicholasjackson/minke-generator-swift.svg?branch=master)](https://travis-ci.org/nicholasjackson/minke-generator-swift)  

This generator creates a REST API Microservice in Swift 3.0 using the IBM Kitura framework for the Minke build and test system.

For information on Minke please see the documentation [http://nicholasjackson.github.io/minke/](http://nicholasjackson.github.io/minke/).

## Available variables for templates (erb style)
| Variable                | Description                            |
| ----------------------- | -------------------------------------- |
| <%= application_name %> | The name of the application executable |
| <%= namespace %>        | Namespace of the application           |
| <%= src_root %>         | Source root of the application         |

## Usage
To scaffold a new service run:

```bash
$ mkdir service
$ cd service
$ curl -L -s get.minke.rocks | bash -s ' -g minke-generator-swift -o $(pwd) -n service -a service'
```

## Build and test with Docker
To run a build with a Docker container, to execute the functional and unit tests you can use the following commands.  Please see the main Minke documentation for more information [http://nicholasjackson.github.io/minke/](http://nicholasjackson.github.io/minke/).

### Build Application Code and Execute Unit tests
```bash
$ cd _build
$ ./minke.sh rake app:test
```

### Build a Docker image and execute functional tests with Cucumber
```bash
$ ./minke.sh rake app:build_image
$ ./minke.sh rake app:cucumber
```

## Development

After checking out the repo, run `bin/setup` to install dependencies. Then, run `rake spec` to run the tests. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and tags, and push the `.gem` file to [rubygems.org](https://rubygems.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/nicholasjackson/minke-generator-netmvc. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
