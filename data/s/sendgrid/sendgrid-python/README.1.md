Use Docker to easily try out or contribute to the sendgrid-python library. 

This Docker image contains:
 - Python 3.6
 - A running instance of [Stoplight.io's Prism](https://stoplight.io/platform/prism/), which lets you try out the SendGrid API without actually sending email
 - A mirrored copy of sendgrid-php so that you may develop locally and then run the tests within the Docker container.

# Table of Contents

* [Quick Start](#quick-start)
* [Testing](#testing)
* [Contributing](#contributing)

<a name="quick-start"></a>
# Quick Start

1. Clone the sendgrid-python repo
  - `git clone https://github.com/sendgrid/sendgrid-python.git`
  - `cd sendgrid-python`
  - `python setup.py install`
2. [Install Docker](https://docs.docker.com/install/)
3. [Setup local environment variable SENDGRID_API_KEY](https://github.com/sendgrid/sendgrid-php#setup-environment-variables)
4. Build Docker image, run Docker container, login to the Docker container
  - `docker image build --tag="sendgrid/python3.6" ./docker-test`
  - `docker run -itd --name="sendgrid_python3.6" -v $(pwd):/root/sendgrid-python sendgrid/python3.6 /bin/bash`
5. Run the tests within the Docker container
  - `sudo docker exec -it sendgrid_python3.6 /bin/bash -c 'cd sendgrid-python; python3.6 -m unittest discover -v; exec "${SHELL:-sh}"'`

Now you can continue development locally, and run `python3.6 -m unittest discover -v` inside of the container to test.

To clean up the container: `docker stop sendgrid_python3.6 && docker rm sendgrid_python3.6`.

Happy Hacking! 

<a name="testing"></a>
# For Testing the Library (Kick the Tires)

- After step 5 in the QuickStart, within the Docker container: 
  - `cd ../`
  - `python sendmail.py` 

<a name="contributing"></a>
# For Contributors

- Develop per usual locally, but before pushing up to GitHub, you can run the tests locally in the Docker container per step 5 of the quickstart.
- To run all the tests: `python3.6 -m unittest discover -v`
- To run an individual test: `python3.6 -m unittest [Filename].[Class].[TestName]`
# Supported tags and respective `Dockerfile` links
 - `v5.4.1`, `latest` [(Dockerfile)](https://github.com/sendgrid/sendgrid-python/blob/master/docker/Dockerfile)
 - `v5.4.0`
 - `v5.3.0`
 - `v5.2.1`
 - `v5.2.0`
 - `v5.1.0`
 - `v5.0.1`
 - `v5.0.0`
 - `v4.2.1`
 - `v4.2.0`
 - `v4.1.0`
 - `v4.0.0`
 - `v3.6.5`
 - `v3.6.4`
 - `v3.6.3`
 - `v3.6.2`
 - `v3.3.0`
 - `v3.2.3`
 - `v3.2.2`
 - `v3.2.1`
 - `v3.2.0`
# Quick reference
 - **Where to get help:**
   [Contact SendGrid Support](https://support.sendgrid.com/hc/en-us)

 - **Where to file issues:**
   https://github.com/sendgrid/sendgrid-python/issues

 - **Where to get more info:**
   [USAGE.md](https://github.com/sendgrid/sendgrid-python/blob/master/docker/USAGE.md)

 - **Maintained by:**
   [SendGrid Inc.](https://sendgrid.com)

# Usage examples
 - Most recent version: `docker run -it sendgrid/sendgrid-python`.
 - Old version: `docker run -it sendgrid/sendgrid-python:v4.2.0`
 - Old version predating this Docker image:
   ```sh-session
   $ git clone https://github.com/sendgrid/sendgrid-python.git --branch v3.6.1
   $ realpath sendgrid-python
   /path/to/sendgrid-python
   $ docker run -it -v /path/to/sendgrid-python:/mnt/sendgrid-python sendgrid/sendgrid-python
   ```
 - Your own fork:
   ```sh-session
   $ git clone https://github.com/you/cool-sendgrid-python.git
   $ realpath cool-sendgrid-python
   /path/to/cool-sendgrid-python
   $ docker run -it -v /path/to/cool-sendgrid-python:/mnt/sendgrid-python sendgrid/sendgrid-python
   ```

For more detailed information, see [USAGE.md](https://github.com/sendgrid/sendgrid-python/blob/master/docker/USAGE.md).

# About

sendgrid-python is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

sendgrid-python is maintained and funded by SendGrid, Inc. The names and logos for sendgrid-python are trademarks of SendGrid, Inc.

![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)
