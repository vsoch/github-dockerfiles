![Docker Badge](https://img.shields.io/docker/automated/reload/harvester.svg) ![Docker Badge](https://img.shields.io/docker/build/reload/harvester.svg)

Harvester
=========

Welcome to Harvester, a service which fetch data from HarvestApp and have a simple API to get data out. This is so much
faster than the actual HarvestApp API since everything is stored locally.


## Installing

When it comes to installing Harvester you will need to clone the repository from GitHub.

    git clone https://github.com/reload/harvester.git

And install Harvester with composer.

If you don't have Composer yet, download it following the instructions on
http://getcomposer.org/ or just run the following command:

    curl -s http://getcomposer.org/installer | php

Then, install the application:

    cd harvester/

    docker-compose run composer install

Composer will install Harvester and all its dependencies. And you will need to configure database and the system.

Install the database

    docker-compose exec harvester app/console doctrine:database:create

Import the database schema

    docker-compose exec harvester app/console doctrine:schema:create

Setup your apache/nginx virtualhost, and a few urls is now available

[http://yourho.st/api/doc]()

[http://yourho.st/admin]()


## Configuration

For the HarvestApp API fetcher to work you need to configure the API info via environment variables in the container:

    cp docker-compose.override.yml-example docker-compose.override.yml

Then edit the variables in docker-compose.override.yml, which correspond to those in `parameters.yml`. You will need to restart the container if it is already running.


## Usage

There is a commmand line command available for fetching data from the HarvestApp API.
This could be executed from crontab

To see the command

    docker-compose exec harvester app/console help harvester:fetch

To run the command without parameters, will fetch everything from Harvest (could tak several minutes)

    docker-compose exec harvester app/console harvester:fetch

To fetch updated data from this month

    docker-compose exec harvester app/console harvester:fetch `date "+%Y%m01"`

To fetch that has been updated since yesterday

    docker-compose exec harvester app/console harvester:fetch --updated-yesterday

To delete entries and repopulate within a given timespan

    docker-compose exec harvester app/console harvester:refresh `date "+%Y%m01"`

To delete entries and repopulate within a static amount of days

    docker-compose exec harvester app/console harvester:refresh --days=30
