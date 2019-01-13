FROM anapsix/alpine-java:8_jdk
MAINTAINER luongbangvh@gmail.com

ENV DIR_ROOT /home/elastic/elasticsearch
ENV DIR_ELASTIC /home/elastic/elasticsearch/elasticsearch-5.5.2
ENV SOURCE_ELASTIC elasticsearch-5.5.2.tar.gz

RUN adduser -D elastic
ADD ${SOURCE_ELASTIC} ${DIR_ROOT}
ADD elasticsearch.yml ${DIR_ELASTIC}/config/elasticsearch.yml

RUN chown -R elastic:elastic ${DIR_ROOT}

USER elastic
WORKDIR ${DIR_ELASTIC}/bin
ENTRYPOINT ["./elasticsearch"]
EXPOSE 9200 9300