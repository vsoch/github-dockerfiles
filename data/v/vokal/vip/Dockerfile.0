FROM golang
MAINTAINER Scott Ferguson <scott.ferguson@vokalinteractive.com>

RUN apt-get update -qq
RUN apt-get install -y ca-certificates \
                       libvips38 \
                       libxml2-dev \
                       automake \
                       build-essential \
                       git \
                       gobject-introspection \
                       libglib2.0-dev \
                       libjpeg62-turbo-dev \
                       libpng12-dev \
                       gtk-doc-tools \
    && git clone https://github.com/jcupitt/libvips.git \
    && cd libvips \
    && ./bootstrap.sh \
    && ./configure --enable-debug=no --without-python --without-fftw --without-libexif --without-libgf --without-little-cms --without-orc --without-pango --prefix=/usr \
    && make \
    && make install \
    && ldconfig
RUN mkdir /etc/vip
RUN ln -s /usr/lib/libvips.so.42 /usr/lib/libvips.so.38

ADD ./vip /vip

EXPOSE 8080

CMD /vip
