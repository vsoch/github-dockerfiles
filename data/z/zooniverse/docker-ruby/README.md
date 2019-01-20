docker-ruby
===========

Minimal Docker Containers for different rubies

## Docker Hub

Docker Containers are automatically build from [zooniverse/ruby](https://hub.docker.com/u/zooniverse/ruby)

## Usage

We use [ruby-build](https://github.com/sstephenson/ruby-build) and
should be able to compile any supported rubies from that probject.

`rake create` compiles the Dockerfile.erb into a Dockerfile after
prompting for the ruby version and any additional dependencies and
moves it into a subfolder with the provided ruby version.

`rake create ruby=version deps=list of deps` skips the configuration
prompts and uses the supplied values.

`rake build hub_name=username` creates a new ruby as `rake create` and
runs docker build on it prefixing the resulting image with the suppied
`hub_name`. Also accepts the same options as `rake create`.

`rake deploy hub_name=username` uploads any locally built containers
to Docker Hub.

## Autobuilds

+ **MRI 2.3.0**

+ **JRuby 1.7.16** - running on OpenJDK 7.

## License

Copyright 2014 by the Zooniverse

Distributed under the Apache Public License v2. See LICENSE
