FROM alpine:3.6

ADD ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
ADD drone-openapi /bin/
ENTRYPOINT ["/bin/drone-openapi"]
