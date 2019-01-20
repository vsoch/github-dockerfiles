# ext-react-docker

A docker image for a React app using ExtReact components.

## Setup

If you haven't already, sign in to Sencha's NPM registry.  You can get credentials 
by [signing up for a trial of ExtReact](https://www.sencha.com/products/extreact/evaluate/).

```
npm login --registry=http://npm.sencha.com --scope=@extjs
```

This command above saves your authentication information to ~/.npmrc, which is later copied into
the docker container when running `npm run docker:build`, thus allowing the docker container
to download ext-react during `npm install`.

## Building and Running in Docker

Run the following build the docker image and run this app in docker:

    npm install
    npm run docker:build
    npm run docker:start

This will start the app and open it in a browser window.  

## Running Locally

Run the following to run the app outside of docker

```
npm install
npm start
```

By default it tries to find an open port starting with 8080.  You can override the 
default port by providing `--env.port=(port)` as a command line argument.

For example to use port 8081:

    npm start -- --env.port=8081

You can also run and serve a production build using:

    npm run build
    npm run prod

## Tests

This application uses jest to run unit tests.  You can run them with:

```
npm test
```

When you make changes, update test snapshots by running:

```
npm run update-snapshots
```