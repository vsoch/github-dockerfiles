# docker-logstash
Logstash 1.5.0-RC3 with added gemfiles. 

## Build and run 
```
docker build . -name logstash
docker run logstash 
```
## Add plugin
Add your plugin to Gemfile and run `bundle install`. Then checkin Gemfile and Gemfile.lock.
## Deploy
Automated build on https://registry.hub.docker.com/u/regius/docker-logstash
