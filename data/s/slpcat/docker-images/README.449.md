# android-java7
DEPRECATED use [java7-8](../java7-8/README.md)

This docker is to build Android Gradle project with Java 7.
It is available on Docker Hub https://registry.hub.docker.com/u/jacekmarchwicki/android/ .

Contains:

* Android SDK: r24.1.2
* Build tools: 22.0.1
* Android API: 22
* Support maven repository
* Google maven repository
* Arm emulator: v22
* Platform tools
* Created emulator image named: "Nexus 5"

## Build image

```bash
docker build -t jacekmarchwicki/android .
```

If building fail you can debug via where `1b372b1f76f2` is partial build

```bash
docker run --tty --interactive --rm 1b372b1f76f2 /bin/bash
```

## Push build version to repository

```bash
docker push jacekmarchwicki/android:java7
```

## Usage
Change directory to your project directory, than run:

```bash
docker run --tty --interactive --volume=$(pwd):/opt/workspace --workdir=/opt/workspace --rm jacekmarchwicki/android:java7  /bin/sh -c "./gradlew build"
```

