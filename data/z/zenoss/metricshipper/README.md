metricshipper
========

Simulation
------------
metricshipper provides a simulator for testing the shipper. The simulator
requires a redis server running in the background.

1. Build
 make clean ; make
 cd simulate && godep restore && go build

2. Execute - Consumer
  ./simulate/simulate consumer

3. Execute - Shipper
  ./output/metricshipper --consumer-url ws://localhost:8443/ws/metrics/store

4. Execute - Producer
  ./simulate/simulate producer -t 512000 -b 128

# Releasing

Use git flow to release a version to the `master` branch.

The artifact version number is defined in the [VERSION](./VERSION) file.

For Zenoss employees, the details on using git-flow to release a new version is documented on the Zenoss Engineering 
web site [here](https://sites.google.com/a/zenoss.com/engineering/home/faq/developer-patterns/using-git-flow).
After the git flow release process is complete, a jenkins job must be triggered manually to build and publish the artifact. 
