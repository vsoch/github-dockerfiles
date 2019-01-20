FROM alpine:3.3

RUN apk update && apk add curl ruby ruby-json

COPY docker-gc.rb /opt/docker-gc.rb

CMD ["ruby", "/opt/docker-gc.rb"]
