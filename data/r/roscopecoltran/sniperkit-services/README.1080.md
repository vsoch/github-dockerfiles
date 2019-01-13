[![Build Status](https://travis-ci.org/CoorpAcademy/docker-scspark.svg)](https://travis-ci.org/CoorpAcademy/docker-scspark)

# docker-scspark

This Docker image helps you to run Spark (on Docker) with the following
installed:

1. [Apache Spark](https://spark.apache.org/) 2.0.0
  + running on Hadoop 2.7.2 and Java openjdk version "1.8.0_92-internal"
2. SBT 0.13.13

# How to install

## On Mac OS X

### 1. Install [homebrew](http://brew.sh)

### 2. Install docker and launch docker daemon
    brew cask install docker

Launch the Docker.app application, and make sure it displays "Docker is running".

## On other OSes

Follow the installation guide from the [official docker guide](
https://docs.docker.com/machine/install-machine/).

# Starting scspark

## On any OS

### 1. Pull the docker image
    docker pull coorpacademy/docker-scspark:latest

### 2. Start the container
Run the following command to start the container and get a bash prompt

    docker run -it coorpacademy/docker-scspark:latest /bin/bash

### 3. Start scspark
    ./bin/spark-shell  # open an interactive scala shell with SparkContext as sc

### 4. Verify installation
To verify scspark, run the following example Spark program:

    sc.parallelize(1 to 1000).count()

This should print: `res0: Long = 1000`.

To quit the interpreter, hit `<Ctrl> + D`.

# How to run a cluster of containers with [Docker Compose](http://docs.docker.com/compose)

## docker-compose.yml example files

    cd example
    docker-compose up  # launch cluster (Ctrl-C to stop)

The SparkUI will be running at `http://${YOUR_DOCKER_HOST}:8080` with one
worker listed. To run `spark-shell`, exec into a container:

    docker exec -it example_master_1 /bin/bash
    spark-shell

Another interesting way of running your script is to use:

    docker exec -it example_master_1 bash -c "sbt package && spark-submit target/scala-2.11/my-awesome-project_2.11-0.1.jar"

And in another terminal:

    docker exec -it example_master_1 nc -l -p 9999

Now whatever words you type in netcat (`nc`) are counted by spark.

# (OPTIONAL) Building the docker image yourself

You can build this docker image, by running the following command in
the same directory as this =README= file. The command will be slow (a
few minutes) the first time, since all dependencies need to be fetched and
compiled from source, but the result is then cached. This step should
only be necessary if you modify the `Dockerfile`.

    docker build -t docker-scspark .

# Troubleshooting
If you are unable to access HDFS from scspark, try running scspark with the
`--master yarn` flag.
