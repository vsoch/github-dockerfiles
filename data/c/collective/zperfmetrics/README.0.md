StatsD server to go with ennexa/graphite

### Usage

    docker run -ti -d --name statsd -v ./conf:/etc/statsd -P ennexa/statsd
	
Modify ./conf/config.js file to point to your Graphite server

If you are using this image with a graphite container having port 2003 exposed, you can link the graphite container to the statsd container with alias name `graphite`
and the graphite server will be automatically detected.

    docker run -ti -d --name graphite ennexa/graphite
    docker run -ti -d --name statsd -P --link graphite:graphite ennexa/statsd
	
### Ports

The image exposes 2 ports

- StatsD Admin Port  : 8126
- StatsD Input Port : 8125 (UDP)

### Volumes

The image exports 1 volume

- Carbon configuration directory at `/etc/statsd`
