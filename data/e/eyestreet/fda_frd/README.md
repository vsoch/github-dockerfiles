# [FDA Food Recall Dashboard - http://fda-frd.eyestreet.com](http://fda-frd.eyestreet.com)

The FDA Food Recall Dashboard provides the user with an interactive map based view of food recall distribution patterns. This allows the user to quickly see locations of food recall events and then drill down into each event to view event information and statistics.

## Description of Approach

We used a hybridized Scrum agile development process in conjunction with multiple agile practices and tools to manage the software and systems engineering life cycles.

The basic requirements for the prototype were gathered at the [initial kick off meeting](https://github.com/eyestreet/fda_frd/raw/gh-pages/documents/GSA_18F_Agile_Delivery_Services_Kick-Off_Meeting_Minutes.pdf) which also included establishment of role assignments and tasking.  Detailed requirements, additional features, bug fixes, and chores were gathered iteratively, as they arose, from user and team feedback and testing.

Our sprints are typically two weeks long, but in this case were reduced to one day due to the short prototype development duration.  Stories were managed using [PivotalTracker](https://www.pivotaltracker.com/n/projects/1375328 "PivotalTracker FDA Food Recall Dashboard Project").

We used over [two dozen open source technologies](http://fda-frd.eyestreet.com/about) at least five of which (bootstrap 3, bower, docker, leaflet, and puma) were initially released within the last five years.  Additionally, the application was created using a mobile-first responsive front end web design.

Unit tests were created using [RSpec](http://rspec.info/), a behavior driven testing framework.  Test data was generated using the [factory_girl](https://github.com/thoughtbot/factory_girl) fixture replacement gem.  Tests were continuously run, on every develop branch push received by github using the [Jenkins CI](https://jenkins-ci.org/) open source continuous integration tool.

Releases of the prototype were managed using the [git-flow](https://github.com/nvie/gitflow) utility and branching model.  Releases were deployed to [Heroku](https://dashboard.heroku.com/) [frequently](https://github.com/eyestreet/fda_frd/releases) for immediate user and team review, interaction, testing, and feedback.  This created an extremely fluid feedback loop.

Once deployed to Heroku the application was continuously monitored using [Airbrake](https://airbrake.io/), [Compose MongoDB Dashboard](https://www.compose.io/), [New Relic APM](https://newrelic.com/), and [Pingdom](https://www.pingdom.com).  Airbrake was used for intelligent exception handling and quickly finding and fixing errors.  The Compose MongoDB Dashboard was integrated with Heroku as part of the Compose MongoDB add-on and provided monitoring and management of our cloud based MongoDB replica set.  New Relic APM, a SaaS-based Application Performance Monitoring tool, was used to monitor end-to-end application performance metrics. Lastly, Pingdom was set up to monitor and track, with notifications, the availability of the application

The prototype can be run either natively, directly on the local machine, or virtually using a combination of [boot2docker](https://github.com/boot2docker/boot2docker), [docker](https://www.docker.com/), and [docker-compose](https://github.com/docker/compose).  In the virtual case, the configuration management and orchestration of the applications is handled using the Dockerfile and docker-compose.yml configuration files and the docker-compose utility.  Instructions for running the application natively or virtually are provided below.  Configuration management of the deployed Heroku application was handled using [Heroku config vars](https://devcenter.heroku.com/articles/config-vars).  We considered using Chef or Puppet for configuration management but decided against that because of the limited configuration required for our prototype application (there is only one config file with one production env var which is automatically configured by Heroku).

Team communication and interaction was facilitated using the [Slack](https://slack.com/) messaging app.  We set up Slack integrations with GitHub, Heroku, Jenkins CI, and Pingdom for centralizing application information.

## Prototype Installation Instruction

### Install and Run Application on OS X Yosemite

Install Ruby 2.2.2. NOTE: The application supports rbenv or rvm using a .ruby-version file.

Install Bundler for your Ruby 2.2.2 installation:

    $ gem install bundler

Install MongoDB (currently version 3.0.4):

    $ brew install mongodb

Import data. From the applications root directory:

    $ cd db
    $ mongorestore -v

Install application gems. From the applications root directory:

    $ bundle install

Start Puma server. From the applications root directory:

    $ bundle exec rails server

View the [running application](http://localhost:3000).

### Install and Run Application with Docker on OS X Yosemite

Install Docker (currently version 1.7.0):

    $ brew install docker

Install Docker Compose (currently version 1.3.1):

    $ brew install docker-compose

Install boot2docker (currently version 1.7.0):

    $ brew install boot2docker

Install VirtualBox (currently version 4.3.28).

Initialize and start boot2docker:

    $ boot2docker init
    $ boot2docker start

Build and run application with Docker Compose. From the applications root directory:

    $ docker-compose build
    $ docker-compose up

Determine boot2docker image ip address:

    $ boot2docker ip

Import data. From the applications root directory and using the ip address from above:

    $ cd db
    $ mongorestore -v -h ip-from-boot2docker

In a browser, using the ip address from above, open http://ip-from-boot2docker:3000

## License

FDA Food Recall Dashboard is released under the [MIT License](http://www.opensource.org/licenses/MIT).
