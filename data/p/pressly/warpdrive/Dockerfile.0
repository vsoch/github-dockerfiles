FROM alpine

RUN apk add --no-cache ca-certificates

# copy the executable to root path
COPY ./bin/server/warpdrive-linux-server /

# running the code
ENTRYPOINT ["/warpdrive-linux-server"]
