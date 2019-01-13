### ElasticSearch and Kibi Docker

see also https://hub.docker.com/_/elasticsearch/

```
git pull zorino/docker-es-kibi

docker run -d --name es-kibi -v $PWD/data:/usr/share/elasticsearch/data -p 9200:9200 -p 5601:5601 zorino/docker-es-kibi
```

ElasticSearch is now running on port 9200 and Kibi on port 5601

