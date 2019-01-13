# Loopback-sdk-builder

![](https://images.microbadger.com/badges/image/superbuddy/loopback-sdk-builder.svg)](https://microbadger.com/images/superbuddy/loopback-sdk-builder "Get your own image badge on microbadger.com")


## Usage

Run as a normal docker and mount your project to `/project`.
For the sdk create a mount to `/sdk`, and generate your sdk using `lb-sdk /project/server/server.js /sdk`

## Auto reload

By default, you can add a gruntfile to enable auto-reload. Add it to your project and install the dependencies.
Gruntfile:
[https://github.com/SuperBuddy/dockerfiles/blob/master/loopback-sdk-builder/gruntfile.js](https://github.com/SuperBuddy/dockerfiles/blob/master/loopback-sdk-builder/gruntfile.js)

Dependencies:
`npm install --save grunt grunt-cli grunt-nodemon`


## Docker-compose

	version: '2'
	services:
	  loopback:
	    image: superbuddy/loopback-sdk-builder
	    ports:
	      - 3000:3000
	      - 5858:5858
	    volumes:
	      - /your/loopback/application/root:/project
	      - /your/loopback/sdk/root:/sdk
	    entrypoint: ["grunt"]