# recruitment-task-katowice

## Setup
- `docker network create recruitment-task-katowice`
- `bin/docker-build`
- `bin/composer install`
- `docker-compose up`
- Add entry to `/etc/hosts`: `'127.0.0.1 msales-katowice-trial.local'`
- Visit `http://msales-katowice-trial.local:8082/app_dev.php` to check if docker is working

## Tools

In order to use symfony console - use tool designed to it:
- `bin/sf`

You can also use one of the prepared statements like:
- `bin/cache-clear`
- `bin/composer`
- `bin/php`

## Task description

1. Create an `Offer` entity with the given fields:
    * `application_id`
    * `country`
    * `payout`
    * `name`
    * `platform`
2. Create a command that will take `Advertiser ID` as a parameter.
3. Command should fetch data from the specified endpoint and save the data within the entity.
4. Keep in mind that in the future we will have new Advertisers that should be integrated.

#### Requirements

* `payout` should be stored in USD
* `country` should be stored as ISO 3166-1 alpha-2
* `application_id` should be unique
* `platform` should be an enum `['Android', 'iOS']`

#### Additional information

* For `Advertiser` with `ID = 2` to get payout amount for each offer you have to calculate it from `points`, where
`10 points = $0.01`.

Example routes to fetch data:

* `v` to fetch all offers data by the given Advertiser
* `/advertiser/{advertiserId}/offer/{offerId}` to fetch one offer data by the given Advertiser
