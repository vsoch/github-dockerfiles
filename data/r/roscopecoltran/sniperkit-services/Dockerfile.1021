FROM alpine:edge

ARG VIPS_VERSION=8.5.5
ARG IMAGINARY_VERSION=1.0.0

ENV GOROOT=/usr/lib/go \
    GOPATH=/tmp/go

RUN apk update && apk add --no-cache openssl ca-certificates && mkdir -p ${GOPATH}/src && \
    wget -O- https://github.com/jcupitt/libvips/releases/download/v${VIPS_VERSION}/vips-${VIPS_VERSION}.tar.gz | tar xzC /tmp && \
    wget -O- https://github.com/h2non/imaginary/archive/v${IMAGINARY_VERSION}.tar.gz | tar xzC ${GOPATH}/src && \
    echo "@edge http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    apk update && apk upgrade && apk add --no-cache --virtual .build-dependencies \
        build-base \
        zlib-dev libxml2-dev glib-dev gobject-introspection-dev \
        libjpeg-turbo-dev libexif-dev lcms2-dev fftw-dev giflib-dev libpng-dev \
        libwebp-dev orc-dev tiff-dev poppler-dev librsvg-dev libgsf-dev openexr-dev \
        go git glide@edge && \
    cd /tmp/vips-${VIPS_VERSION} && \
    ./configure \
        --disable-static \
        --disable-dependency-tracking \
        --without-python && \
    make && \
    make install && \

    cd ${GOPATH}/src/imaginary-${IMAGINARY_VERSION} && \
    glide install && \
    go build -o $GOPATH/bin/imaginary && \
    cp $GOPATH/bin/imaginary /usr/bin/imaginary && \

    apk del --purge .build-dependencies && \
    rm -rf ${GOPATH} && \
    rm -rf /tmp/vips-${VIPS_VERSION} && \

    apk add --no-cache \
    zlib libxml2 glib gobject-introspection \
    libjpeg-turbo libexif lcms2 fftw giflib libpng \
    libwebp orc tiff poppler-glib librsvg libgsf openexr && \

    rm -rf /var/cache/apk/*

ENV PORT 9000
EXPOSE 9000

ENTRYPOINT ["/usr/bin/imaginary"]
