FROM golang:1.9 AS build
WORKDIR /go/src/github.com/networkteam/minicron
COPY main.go .
COPY vendor vendor
RUN GOOS=linux go build .

FROM alpine:latest
WORKDIR /root/
COPY --from=build /go/src/github.com/networkteam/minicron/minicron .
ENTRYPOINT ["./minicron"]
