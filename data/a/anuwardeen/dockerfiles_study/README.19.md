## Dart runtime Dockerfile


This repository contains **Dockerfile** of [Dart](https://www.dartlang.org/) runtime for [Docker](https://www.docker.com/)'s [automated build](https://registry.hub.docker.com/u/dockerfile/dart-runtime/) published to the public [Docker Hub Registry](https://registry.hub.docker.com/).

This image is a base image that makes it easy to dockerize standard [Dart](https://www.dartlang.org/) application.

It can automatically bundle a `Dart` application with its dependencies and set the default command with no additional Dockerfile instructions.

This project heavily borrowed code from Google's [google/dart-runtime](https://registry.hub.docker.com/u/google/dart-runtime/) Docker image.


### Base Docker Image

* [dockerfile/dart](http://dockerfile.github.io/#/dart)


### Installation

1. Install [Docker](https://www.docker.com/).

2. Download [automated build](https://registry.hub.docker.com/u/dockerfile/dart-runtime/) from public [Docker Hub Registry](https://registry.hub.docker.com/): `docker pull dockerfile/dart-runtime`

   (alternatively, you can build an image from Dockerfile: `docker build -t="dockerfile/dart-runtime" github.com/dockerfile/dart-runtime`)


### Usage

This image assumes that your application:

* has a the `pubspec.yaml` and `pubspec.lock` files listing its dependencies.
* has a file named `bin/server.dart` as the entrypoint script.
* listens on port `8080`.

When building your application docker image, `ONBUILD` triggers fetch the dependencies listed in `pubspec.yaml` and `pubspec.yaml` and cache them appropriatly using `pub get`.

* **Step 1**: Create a Dockerfile in your `Dart` application directory with the following content:

```dockerfile
    FROM dockerfile/dart-runtime
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
