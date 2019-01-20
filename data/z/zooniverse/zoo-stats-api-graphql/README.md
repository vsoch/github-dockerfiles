# Zoo stats
[![Build Status](https://travis-ci.org/zooniverse/zoo-stats-api-graphql.svg?branch=master)](https://travis-ci.org/zooniverse/zoo-stats-api-graphql)

### Setup Docker and Docker Compose

* Docker
  * [OS X](https://docs.docker.com/installation/mac/) - Docker Machine
  * [Ubuntu](https://docs.docker.com/installation/ubuntulinux/) - Docker
  * [Windows](http://docs.docker.com/installation/windows/) - Boot2Docker

* [Docker Compose](https://docs.docker.com/compose/)

#### Usage

1. Clone the repository `git clone https://github.com/zooniverse/zoo_stats_api_graphql`.

0. Install Docker from the appropriate link above.

0. `cd` into the cloned folder.

0. Run `docker-compose build` to build the containers Panoptes API container. You will need to re-run this command on any changes to `Dockerfile`

0. Install the gem dependencies for the application
    * Run: `docker-compose run --rm --entrypoint="bundle install" zoo_stats`

0. Create and run the application containers with `docker-compose up`

0. If the above step reports a missing database error, kill the docker-compose process or open a new terminal window in the current directory and then run `docker-compose run --rm --entrypoint="bundle exec rake db:setup" zoo_stats` to setup the database. This command will launch a new Docker container, run the rake DB setup task, and then clean up the container.

0. Open up the application in your browser at http://localhost:3000

Once all the above steps complete you will have a working copy of the checked out code base. Keep your code up to date and rebuild the image on any code or configuration changes.

#### Testing

1. Setup the test environment and database
    * Run: `docker-compose run --rm -e RAILS_ENV=test --entrypoint="bundle install" zoo_stats`
    * Run: `docker-compose run --rm -e RAILS_ENV=test --entrypoint="bundle exec rake db:setup" zoo_stats`

0. Run the tests
    * Run: `docker-compose run -T --rm -e RAILS_ENV=test --entrypoint="bundle exec rspec" zoo_stats`
