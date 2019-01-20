# Tolaboard

WARNING: THIS APPLICATION IS CURRENTLY IN DEVELOPMENT, AND NOT COMPLETELY FUNCTIONAL. IT HAS NOT BEEN RELEASED TO PRODUCTION!

TolaBoard is a tool for building dynamic data visualizations within TolaData. It's intention is to improve reporting and visualization of data inside TolaTables. The software introduces a new technology into the TolaData stack, namely, client-side based MVC using Ember.js.

## Overview

The app has a back-end created in Node.js and Express.js, along with other middleware libraries for Node. It consists mainly of an API for CRUD functionality of TolaBoards. It also has an API call that serves as a proxy for retrieving data from TolaTables. The front-end of the app is built in Ember.js using ember-cli which creates a build of the app via running "ember server". A build is created which is a standard build from running either ember server or ember build. It can be hosted on the backend Node server, or as a stand-alone set of static files served from a content server. The repo is divided into ember and express directories for each of these app components. Development with Ember CLI is easy... you run CLI commands to create the structure of your app. Then while running Ember Server, as you save changes, a new build is created in the dist folder. 


## Prerequisites

You will need the following things properly installed on your computer.

* [Git](http://git-scm.com/)
* [Node.js](http://nodejs.org/) (with NPM)
* [Bower](http://bower.io/)
* [Ember CLI](http://ember-cli.com/)

## Installation

* `git clone <repository-url>` this repository
* change into the new directory
* `npm install`
* `bower install`

You can develop locally by just running servers for Ember and Node. They both make use of npm, so after pulling down the code, go into their respective app folders, and run npm install. The package.json files contain all the dependencies, and so everything should get installed. For ember, you'll also need to run bower install. bower.json contains all the client side dependencies. Update the configuration files (see below) and then for node, run nodemon in the express app folder. Install nodemon if you don't have it. Updates to the files automatically restart the server. You can configure the port it runs on in the config. For ember, update it's config file with your node server location. You can test the backend API is working by hitting the route localhost:port/api... should see "Welcome to the TolaBoard API"

For ember, run "ember server" from the ember directory (not inside ember/app). You should eventually see a message telling you the server is running.

## Configuration

For Node/Express: In the app root... config.json. Note, the actual file is excluded via .gitignore. config.template.json needs updated and renamed for the app to work. 

For Ember: In ember/config/environment.js 

## Running / Development

Default location for the ember app is on localhost:4200. You can change this in the .ember-cli file by creating another keypair entry in the JSON... "port": 4444 (for example)

* `ember server` 
* Visit your app at [http://localhost:4200](http://localhost:4200).


### Code Generators

Make use of the many generators for code, try `ember help generate` for more details

### Running Tests

* `ember test`
* `ember test --server`

### Building

* `ember build` (development)
* `ember build --environment production` (production)

### Deploying

Specify what it takes to deploy your app.

## Further Reading / Useful Links

* [ember.js](http://emberjs.com/)
* [ember-cli](http://ember-cli.com/)
* Development Browser Extensions
  * [ember inspector for chrome](https://chrome.google.com/webstore/detail/ember-inspector/bmdblncegkenkacieihfhpjfppoconhi)
  * [ember inspector for firefox](https://addons.mozilla.org/en-US/firefox/addon/ember-inspector/)

* [Ember Screencasts](https://www.emberscreencasts.com/) - Lots of free content, but also premium stuff for more advanced learning
* [Traversy Media](https://www.youtube.com/watch?v=owDmPTSJkrg&list=PLillGF-RfqbYlw550JoiJrHsy0BT0tCgU) - free YouTube content that's basic, but gets you started.

