FROM alpine:3.5

ARG FFMPEG_VERSION=3.3.2

RUN apk update && \
    apk upgrade && \

    apk add --update ca-certificates && \

    apk add gnutls-dev zlib-dev yasm-dev lame-dev libogg-dev \
    x264-dev libvpx-dev libvorbis-dev x265-dev freetype-dev \
    libass-dev libwebp-dev rtmpdump-dev libtheora-dev opus-dev && \

    apk add --no-cache --virtual .build-dependencies \
    build-base coreutils tar bzip2 x264 gnutls nasm && \

# Install ffmpeg
    wget -O- http://ffmpeg.org/releases/ffmpeg-${FFMPEG_VERSION}.tar.gz | tar xzC /tmp && \
    cd /tmp/ffmpeg-${FFMPEG_VERSION} && \
    ./configure --bindir="/usr/bin" \
                --enable-version3 \
                --enable-gpl \
                --enable-nonfree \
                --enable-small \
                --enable-libmp3lame \
                --enable-libx264 \
                --enable-libx265 \
                --enable-libvpx \
                --enable-libtheora \
                --enable-libvorbis \
                --enable-libopus \
                --enable-libass \
                --enable-libwebp \
                --enable-librtmp \
                --enable-postproc \
                --enable-avresample \
                --enable-libfreetype \
                --enable-gnutls \
                --disable-debug && \
    make && \
    make install && \
    make distclean && \
    cd $OLDPWD && \

# Cleanup
    rm -rf /tmp/ffmpeg-${FFMPEG_VERSION} && \
    apk del --purge .build-dependencies && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["/usr/bin/ffmpeg"]
