FROM traefik:1.4.6-alpine

# development tools
RUN apk add --no-cache bind-tools curl bash

RUN addgroup -S zing && adduser -S -G zing -u 512 512
USER 512

COPY ./traefik.toml /etc/traefik/traefik.toml

