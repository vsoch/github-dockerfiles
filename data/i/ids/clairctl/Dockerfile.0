FROM alpine:3.5

ENV GOPATH=/go
ENV PATH=${GOPATH}/bin:${PATH}
ENV DOCKER_API_VERSION=1.24
ARG DOCKER_VERSION=${DOCKER_VERSION:-latest}
ARG CLAIRCTL_VERSION=${CLAIRCTL_VERSION:-master}
ARG CLAIRCTL_COMMIT=

RUN apk add --update curl \
 && apk add --update --virtual build-dependencies go gcc build-base glide git \
 && adduser clairctl -D \
 && mkdir -p /reports \
 && chown -R clairctl:clairctl /reports /tmp \
 && curl https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz -o docker.tgz \
 && tar xfvz docker.tgz --strip 1 -C /usr/bin/ docker/docker \
 && rm -f docker.tgz \
 && go get -u github.com/jteeuwen/go-bindata/... \
 #&& curl -sL https://github.com/ids/clairctl/archive/${CLAIRCTL_VERSION}.zip -o clairctl.zip \
 && mkdir -p ${GOPATH}/src/github.com/ids/ 
 #&& unzip clairctl.zip -d ${GOPATH}/src/github.com/ids/ \
 #&& rm -f clairctl.zip \
 #&& mv ${GOPATH}/src/github.com/ids/clairctl-* ${GOPATH}/src/github.com/ids/clairctl \

COPY ./ /tmp/clairctl 

RUN  mv /tmp/clairctl ${GOPATH}/src/github.com/ids/clairctl \
 && cd ${GOPATH}/src/github.com/ids/clairctl \
 && glide install -v \
 && go generate ./clair \
 && go build -o /usr/local/bin/clairctl -ldflags "-X github.com/ids/clairctl/cmd.version=${CLAIRCTL_VERSION}-${CLAIRCTL_COMMIT}" \
 && apk del build-dependencies \
 && rm -rf /var/cache/apk/* \
 && rm -rf /root/.glide/ \
 && rm -rf /go \
 && echo $'clair:\n\
  port: 6060\n\
  healthPort: 6061\n\
  uri: http://clair-api\n\
  priority: Low\n\
  report:\n\
    path: /reports\n\
    format: html\n\
clairctl:\n\
  port: 44480\n\
  tempfolder: /tmp'\
    > /home/clairctl/clairctl.yml

RUN apk upgrade git
RUN apk upgrade bin-utils

USER clairctl

COPY ./clair-config.yml /config/config.yml

WORKDIR /home/clairctl/

EXPOSE 44480

VOLUME ["/tmp/", "/reports/"]
 
CMD ["/usr/sbin/crond", "-f"]