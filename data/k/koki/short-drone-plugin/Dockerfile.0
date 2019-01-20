FROM golang:1.8-alpine

RUN apk update && \
    apk add ca-certificates wget && \
    update-ca-certificates

ADD . /go/src/github.com/koki/short-drone-plugin

WORKDIR /go/src/github.com/koki/short-drone-plugin

RUN go build github.com/koki/short-drone-plugin && mv short-drone-plugin /bin/short-drone-plugin

RUN wget https://github.com/koki/short/releases/download/v0.3.0/short_linux_amd64 -O /bin/short

RUN chmod a+x /bin/short

ENTRYPOINT ["short-drone-plugin"]
