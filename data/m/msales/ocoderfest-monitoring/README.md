# O'CoderFest Monitoring

## Installation

1. Create the network `docker network create --driver bridge ocoderfest-msales`
2. Build the containers `docker-compose build`
3. Add hosts:
    ```
    127.0.0.1       grafana.ocoderfest.msales
    127.0.0.1       influxdb.ocoderfest.msales
    127.0.0.1       graylog.ocoderfest.msales
    ```
4. Start the containers `docker-compose up`
5. Test it out by visiting one of the websites like:
    - grafana (http://grafana.ocoderfest.msales:8888)
    - influxdb (http://influxdb.ocoderfest.msales:8888)
    - graylog (http://graylog.ocoderfest.msales:8888)

## Warning!
Not ready for production, use for testing purposes only.
