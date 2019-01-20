FROM ubuntu:14.04

ENV PATH /usr/local/go/bin:$PATH
ENV GOROOT /usr/local/go
ENV GOPATH /go

RUN apt-get update -q
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy build-essential curl git
RUN curl -s https://go.googlecode.com/files/go1.2.1.src.tar.gz | tar -v -C /usr/local -xz
RUN cd /usr/local/go/src && ./make.bash --no-clean 2>&1
RUN go get github.com/moneybird/dnsizer
RUN go install github.com/moneybird/dnsizer

EXPOSE 53

ENTRYPOINT ["/go/bin/dnsizer"]
