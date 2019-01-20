# Kafka GeoServer Plugin
Plugin for [GeoServer](http://geoserver.org/) adding a WFS-T transaction listener that will send a message to [Kafka](https://kafka.apache.org/) for each affected feature.

## Running the plugin
Build a jar and drop it in your `geoserver/WEB-INF/lib` directory.

Use [`bootstrap.servers`](https://kafka.apache.org/documentation/#producerconfigs) java system property when running GeoServer to configure the location of your Kafka. Defaults to `localhost:9092`.

Use `kafkaFormat` java system property when running GeoServer to configure the format of your Kafka messages. Options are `pbf` and `json`. Defaults to `pbf`.

The plugin will send events to layer specific topics named `workspace.layerName`. It assumes that kafka is using the [auto.create.topics.enable](https://kafka.apache.org/documentation/#brokerconfigs) setting or that the topics will already exist.

POST a WFS-T request to your GeoServer WFS endpoint (eg., http://localhost:8080/geoserver/wfs) and the plugin should fire message(s) to Kafka. See the [examples](examples) folder for some sample requests.

To verify that the messages are being sent to the kafka topic, you can use the command line consumer:
```
bin/kafka-console-consumer.sh --new-consumer --from-beginning --bootstrap-server localhost:9092 --topic workspace.layer
```

## Message Format
You can use the aforementioned `kafkaFormat` to switch message formats.  
Examples of the currently supported formats:

### JSON (json)
An event is a simple json structure that contains the **operation** (insert, update, or delete), **source** (same as the topic name), and **feature** (GeoJSON formatted).

Example:
```json
{
  "operation": "insert",
  "source": "boundless.countries",
  "feature": {
    "type":"Feature",
    "geometry":{"type":"MultiPolygon","coordinates":[[[[0.0,0.0],[0.0,20],[-20,20],[-20,0.0],[0.0,0.0]]]]},
    "properties":{"sovereignt":"Country","admin":"Test Country"},
    "id":"countries.178"
  }
}
```

### Protobuf (pbf)
The protobuf schema is define at https://github.com/boundlessgeo/spatialconnect-schema/blob/develop/Feature.proto  
This format largely mirrors the JSON format with the main difference coming in the feature section. Instead of using GeoJSON to capture the feature information we are using a simple structure that contains the `fid`, a map of `properties`, and a `geometry`, where the geometry is [well-known binary](https://en.wikipedia.org/wiki/Well-known_text).

Example:
```pbf
boundless.countries?
countries.178
adminTest Countryf@4?4@4?4
```

## Running in Docker
`docker-compose` will create an environment that includes zookeeper, kafka, postgis, and geoserver. By default GeoServer data directory is bound to `$HOME/geoserver_data` and the postgres data directory is bound to `$HOME/postgres_data` so that you don't have to recreate layers/tables/etc. between builds.

The GeoServer [Dockerfile](Dockerfile) is copied from https://github.com/kartoza/docker-geoserver with a slight modification to allow changing the GeoServer version using the `GS_VERSION` build-arg.

The plugin is built and included in the `resources/plugins` folder. Other GeoServer plugin zipfiles can also be included in that folder.

1. Build the plugin which will create the zip in the `resources/plugins` folder.
    - `mvn package`
2. Build the GeoServer docker image.
    - `docker-compose build geoserver`
3. Run the docker cluster.
    - `docker-compose up`
