# Event Data Live Demo

Very simple live-stream of Event Data in the browser. Listens on an ActiveMQ Topic and broadcasts to web browsers via websocket. A Topic is used rather than a Queue because there may be more than one instance listening and there is no need for keeping history on restart.

This is not intended to be an API for live data access, or an information-critical system. It is just an illustration of the events that come through the system.

An Artifact containing a list of source-ids as a plaintext file is required, configured with `SOURCES_ARTIFACT`. For Crossref, this is `crossref-sourcelist`. This is read when the service starts. To reload, restart.

If the special value of "*" is passed as sources artifact, everything will accepted.

## To run

You can run a local copy with Docker Compose:

    docker-compose run -w /usr/src/app -p "8101:8101" demo lein run

## Configuration

Note that this service can be run in Docker Swarm with replication. The Swarm routing mesh might load-balance in-coming events, but they are all sent to the Redis instance for pubsub before being rebroadcast on websockets.

 - GLOBAL_BUS_OUTPUT_TOPIC
 - GLOBAL_STATUS_TOPIC
 - GLOBAL_KAFKA_BOOTSTRAP_SERVERS
 - LIVE_PORT

## License

Copyright © Crossref

Distributed under the The MIT License (MIT).

