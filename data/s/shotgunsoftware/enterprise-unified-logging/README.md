# Enterprise Unified Logging

This repository contains example configurations for running an Elasticsearch stack to monitor and log Shotgun Enterprise. The visualizations and dashboards provided are examples of what could be useful for monitoring Shotgun Enterprise, clients may choose to modify the configuration as needed.

The solution uses [Fluentd](https://www.fluentd.org/) as the data collector between the Shotgun application and the Elasticsearch database.

# Getting started

First, you will need to build the Fluentd image and the Kibana image using the following command.
    
    docker-compose build

Then start Fluentd and Elasticsearch along with Kibana.

    docker-compose up
    
Finally, you will need to change the Shotgun application logging driver in its `docker-compose.yml` file from `json-file` to `fluentd`:

Remove 
```yaml
# json-file
logging:
  driver: "json-file"
  options:
    max-size: "2g"
    max-file: "20"
```

And add
```yaml        
# fluentd
logging:
  driver: "fluentd"
  options:
    fluentd-address: "<fluentd_server_address>:24224"
    tag: "sg.app.{{.ID}}"
```

# How to access logs

## Kibana

Logs can be access via Kibana at [http://localhost:5601/](http://localhost:5601/)

From there you can create your indexes (ex: `shotgun_logs-*` already created by default) and then query Elasticsearch.

### Saved Objects

Customizations (visualizations, dashbaords, etc) can be saved. Please refer to [Kibana documentation](https://www.elastic.co/guide/en/kibana/current/managing-saved-objects.html) on how to manage saved objects. However, once changes are made in Kibana they persist as long as the database is not removed.

Saved objects can be provisioned by default by modifying the appropriate json file in the `kibana/files_docker/provision.d/` directory.

## Log files

Logs are also available (not by default) in json file in the `logs/` directory.

# Fluentd

## Configuration

All the configuration takes place in the `fluentd/files_docker/fluent.conf` file.

Further details on configuring `fluentd` is availabe in the [config-file documentation](https://docs.fluentd.org/v1.0/articles/config-file).

## Plugins

For Elasticsearch, we use the [fluent-plugin-elasticsearch](https://github.com/uken/fluent-plugin-elasticsearch) plugin.

To install additional plugin see the Dockerfile at `fluentd/Dockerfile`.
