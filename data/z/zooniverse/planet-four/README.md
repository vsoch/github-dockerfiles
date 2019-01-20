Planet Four
=======

Will *only* run on Node 0.10.x - use [NVM](https://github.com/creationix/nvm) to install older versions of Node.

## Commands

### Run a local development server

`npm run start`

or

`docker-compose run --service-ports p4 npm run start`

### Build and deploy the frontend to staging

`npm run deploy-to-staging`

or

`docker-compose run --service-ports p4 npm run deploy-to-staging`

Staging URL is [https://www.planetfour.org/beta](https://www.planetfour.org/beta)

### Build and deploy the frontend to production

`npm run deploy`

or

`docker-compose run --service-ports p4 npm run deploy`

### Deploy the translations

`npm run deploy-locale`

or

`docker-compose run --service-ports p4 npm run deploy-locale`

Requires the `OUROBOROS_AUTH` environment variable to be set as `login:apiKey`, for example: `OUROBOROS_AUTH=mylogin:abcd1234`
