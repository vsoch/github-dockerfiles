# Caspr

The ultimate lean digital tool to develop faster and better.

# How to develop

Run `npm install` in client and backend folders.

Run `docker-compose up`.

You're all set! Go to http://localhost to access to Caspr.

# Migrations

The ORM we use is [sequelize](http://docs.sequelizejs.com). Follow following command to update the database.

## Create a new model

Run `node_modules/.bin/sequelize model:generate --name User --attributes firstName:string,lastName:string,email:string` with correct model name and model attributes.

## Run migrations

Run `node_modules/.bin/sequelize db:migrate`.
