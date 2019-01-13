## Node.js w/ Bower & Grunt runtime Dockerfile


This repository contains **Dockerfile** of [Node.js](http://nodejs.org/) w/ [Bower](http://bower.io/) & [Grunt](http://gruntjs.com/) runtime for [Docker](https://www.docker.com/)'s [automated build](https://registry.hub.docker.com/u/dockerfile/nodejs-bower-grunt-runtime/) published to the public [Docker Hub Registry](https://registry.hub.docker.com/).

This image is a base image for easily running [Node.js](http://nodejs.org/) application.

It can automatically bundle a `Node.js` application with its dependencies and set the default command with no additional Dockerfile instructions.

This project heavily borrowed code from Google's [google/nodejs-runtime](https://registry.hub.docker.com/u/google/nodejs-runtime/) Docker image.


### Base Docker Image

* [dockerfile/nodejs-bower-grunt](http://dockerfile.github.io/#/nodejs-bower-grunt)


### Installation

1. Install [Docker](https://www.docker.com/).

2. Download [automated build](https://registry.hub.docker.com/u/dockerfile/nodejs-bower-grunt-runtime/) from public [Docker Hub Registry](https://registry.hub.docker.com/): `docker pull dockerfile/nodejs-bower-grunt-runtime`

   (alternatively, you can build an image from Dockerfile: `docker build -t="dockerfile/nodejs-bower-grunt-runtime" github.com/dockerfile/nodejs-bower-grunt-runtime`)


### Usage

This image assumes that your application:

* has a file named [package.json](https://www.npmjs.org/doc/json.html) listing its dependencies.
* has a file named [bower.json](http://bower.io/docs/creating-packages/) listing its dependencies.
* has a file named [Gruntfile.js](http://gruntjs.com/sample-gruntfile) registering `build` task.
* has a file named `server.js` as the entrypoint script or define in package.json the attribute: `"scripts": {"start": "node <entrypoint_script_js>"}`
* listens on port `8080`

When building your application docker image, `ONBUILD` triggers install NPM module dependencies of your application using `npm install`.

* **Step 1**: Create a Dockerfile in your `Node.js` application directory with the following content:

```dockerfile
    FROM dockerfile/nodejs-bower-grunt-runtime
```

* **Step 2**: Build your container image by running the following command in your application directory:

```sh
    docker build -t="app" .
```

* **Step 3**: Run application by mapping port `8080`:

```sh
    APP=$(docker run -d -p 8080 app)
    PORT=$(docker port $APP 8080 | awk -F: '{print $2}')
    echo "Open http://localhost:$PORT/"
```
## Node.js w/ Bower & Grunt Dockerfile


This repository contains **Dockerfile** of [Node.js](http://nodejs.org/) w/ [Bower](http://bower.io/) & [Grunt](http://gruntjs.com/) for [Docker](https://www.docker.com/)'s [automated build](https://registry.hub.docker.com/u/dockerfile/nodejs-bower-grunt/) published to the public [Docker Hub Registry](https://registry.hub.docker.com/).


### Base Docker Image

* [dockerfile/nodejs](http://dockerfile.github.io/#/nodejs)


### Installation

1. Install [Docker](https://www.docker.com/).

2. Download [automated build](https://registry.hub.docker.com/u/dockerfile/nodejs-bower-grunt/) from public [Docker Hub Registry](https://registry.hub.docker.com/): `docker pull dockerfile/nodejs-bower-grunt`

   (alternatively, you can build an image from Dockerfile: `docker build -t="dockerfile/nodejs-bower-grunt" github.com/dockerfile/nodejs-bower-grunt`)


### Usage

    docker run -it --rm dockerfile/nodejs-bower-grunt

#### Run `node`

    docker run -it --rm dockerfile/nodejs-bower-grunt node

#### Run `npm`

    docker run -it --rm dockerfile/nodejs-bower-grunt npm

#### Run `bower`

    docker run -it --rm dockerfile/nodejs-bower-grunt bower

#### Run `grunt`

    docker run -it --rm dockerfile/nodejs-bower-grunt grunt