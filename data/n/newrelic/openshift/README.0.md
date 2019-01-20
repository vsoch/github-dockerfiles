# PythonNewRelic

This is a test application for the New Relic Python plugin
Instructions for building and running:
1. Download/clone this git repo
2. Go to https://www.newrelic.com and obtain a license key (offer trial licenses)
3. Edit the newrelic.ini file - find the following:
* `license_key = XXXXXXXXXXX` <-- replace this with your license key
4. Save the file
5. Build the Docker image `docker build -t newrelic-admin-rhel73/python-agent .`
6. Once the image is built, launch the container:
* `docker run newrelic-admin-rhel73/python-agent`
7. This will launch the container and send 5 test messages to your NewRelic account

