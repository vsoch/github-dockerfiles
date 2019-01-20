FROM golang:1.7.4

RUN apt-get -y install git

ENV DALI_SRC=$GOPATH/src/github.com/att-innovate/dali-server

RUN go get gopkg.in/mgo.v2
RUN mkdir -p $DALI_SRC
COPY src/main.go $DALI_SRC
RUN go install -a github.com/att-innovate/dali-server 

RUN mkdir -p /dali-server/templates/
COPY templates/* /dali-server/templates/
RUN cp $GOPATH/bin/dali-server /dali-server/

WORKDIR /dali-server/

ENTRYPOINT ["./dali-server"]
CMD ["-help"]
