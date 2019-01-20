# meedan/filebeat

https://www.elastic.co/guide/en/beats/filebeat
based on
https://github.com/primait/docker-filebeat/

#### EXAMPLE
 ```
 docker run -v /path/to/logs:/opt/logs -v /path/to/configdir:/path/to/configdir meedan/filebeat -c /path/to/configdir/config.yml
 ```

logs will be delivered to a destination as specified in config.yml