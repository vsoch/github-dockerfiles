FROM golang:1.8.3

RUN apt-get update
RUN apt-get -y install libpcap-dev

ENV TELEGRAF_SRC=$GOPATH/src/github.com/influxdata/telegraf

RUN go get github.com/opencontainers/runc/libcontainer/user
RUN go get github.com/golang/glog

RUN mkdir -p $TELEGRAF_SRC
COPY src/telegraf/ $TELEGRAF_SRC/
RUN cd $TELEGRAF_SRC; make

RUN mkdir -p /telegraf/
RUN cp $GOPATH/bin/telegraf /telegraf/
COPY telegraf.conf /telegraf/

WORKDIR /telegraf/

ENTRYPOINT ["./telegraf"]
CMD ["--config", "telegraf.conf"]
