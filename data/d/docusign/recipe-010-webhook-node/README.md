# Webhook-Node recipe
This directory includes the source for the Node Webhook recipe and enables it to be run on a free Heroku server.

The /src directory holds the complete example

The top level files are used to manage and configure the example on [Heroku](https://www.heroku.com/) and [MS Azure](https://portal.azure.com/).

## Run the recipe on Heroku
The recipe source can be run on [Heroku](https://www.heroku.com/) using the free service level. No credit card needed!

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Click the Deploy button, then enter your DocuSign Developer Sandbox credentials on the form in the Heroku dashboard. Then press the View button at the bottom of the dashboard screen when it is enabled by the dashboard.

## Run the recipe on MS Azure
The recipe source can be run on [MS Azure](https://portal.azure.com/) using their trial offer.

[![Deploy to Azure](http://azuredeploy.net/deploybutton.png)](https://azuredeploy.net/)

## Run the recipe on your own server

### Get Ready
Your server needs Node 4 or later

Your server **must** have an address that is visible and accessible from the public internet. Unless that is the case, the DocuSign platform will not be able to post the notification messages *to* your server.

You need an email address and password registered with the free DocuSign Developer Sandbox system. You also need a free Integration Key for your DocuSign developer account. See the [DocuSign Developer Center](https://www.docusign.com/developer-center) to sign up.

### How to do it
```sh
% npm install
% heroku local
```

## Run the recipe with Docker

This can be ran on a Docker container.

Build the Docker image
```
docker build . connect_listener
```

Run the Docker image
```
docker run connect_listener
```