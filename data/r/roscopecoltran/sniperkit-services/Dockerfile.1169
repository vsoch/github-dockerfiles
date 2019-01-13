FROM smizy/scikit-learn:0.18-alpine

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.docker.dockerfile="/Dockerfile" \
    org.label-schema.license="Apache License 2.0" \
    org.label-schema.name="smizy/keras" \
    org.label-schema.url="https://github.com/smizy" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-type="Git" \
    org.label-schema.version=$VERSION \
    org.label-schema.vcs-url="https://github.com/smizy/docker-keras-theano"

ENV KERAS_VERSION  $VERSION
ENV KERAS_BACKEND  theano

RUN set -x \
    && apk update \
    ## keras/theano
    && apk --no-cache add \
        g++ \
        python3-dev \
    && pip3 install keras==${KERAS_VERSION} \
    && mkdir -p /home/jupyter/.keras \
    ## clean 
    && find /usr/lib/python3.5 -name __pycache__ | xargs rm -r \
    && rm -rf /root/.[acpw]* 

COPY keras.json  /home/jupyter/.keras/