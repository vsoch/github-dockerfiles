# docker-telekibi
TeleKibi: Kibana/Kibi Supercharged with Elasticfence Plugins and much more!

## Usage

Run the image using local Elastic instance
```
$ docker run -i -t -p 9200:9200 -p 5606:5606 qxip/docker-telekibi
```

Run the image using remote Elastic instance
```
$ docker run -i -t -e ELASTICSEARCH_URL=http://192.168.10.20:9200 -p 5606:5606 qxip/docker-telekibi
```
