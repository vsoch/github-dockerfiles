FROM ubuntu

RUN apt-get -q update && \
    apt-get -yq install automake autoconf pkg-config libtool software-properties-common && \
    apt-get -yq install git wget net-tools vim && \
    apt-get -y autoclean

RUN git clone https://github.com/vstakhov/libucl /libucl && \
    cd /libucl && \
    ./autogen.sh && \
    ./configure --disable-debug --disable-dependency-tracking --disable-silent-rules --prefix=/usr/local/ && \
    make install && \
    rm -rf /libucl

RUN mkdir /phc-winner-argon2 && \
    wget -qO- https://github.com/P-H-C/phc-winner-argon2/archive/20161029.tar.gz | tar zx --strip-components 1 -C /phc-winner-argon2 && \
    cd /phc-winner-argon2 && \
    make && make install PREFIX=/usr/local && \
    cp /phc-winner-argon2/*.pc /usr/lib/pkgconfig/ && \
    rm -rf /phc-winner-argon2

RUN add-apt-repository ppa:longsleep/golang-backports && apt-get -q update && apt-get install -yq golang-go libzmq3-dev

RUN apt-get install -y maven openjdk-8-jdk && apt-get -y autoclean
RUN git clone https://github.com/bitmark-inc/bitmark-pay /bitmark-pay && cd /bitmark-pay && \
    mvn -Dmaven.repo.local="local-maven-repository/m2" package && \
    sed -i -e "s/%%BITMARK_PAY_JAR%%/\/bitmark-pay\/target\/bitmarkPayService-3.1-jar-with-dependencies.jar/g" bin/bitmark-pay && \
    mv bin/bitmark-pay /usr/local/bin/

ENV GOPATH /go
ENV PATH="/go/bin:${PATH}"

RUN wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash && \
    bash -c "source ~/.nvm/nvm.sh && nvm install v7"

RUN go get github.com/yudai/gotty
RUN go get -d github.com/bitmark-inc/bitmarkd || \
    go install github.com/bitmark-inc/bitmarkd/command/...
RUN go get -d github.com/bitmark-inc/bitmark-cli && \
    rm -r /go/src/github.com/bitmark-inc/bitmark-cli/vendor/github.com/bitmark-inc/bitmarkd/vendor/github.com/bitmark-inc/go-argon2 && \
    rm -r /go/src/github.com/bitmark-inc/bitmarkd/vendor/github.com/bitmark-inc/go-libucl && \
    go install github.com/bitmark-inc/bitmark-cli

COPY ui /.config/webgui/ui

RUN go get github.com/bitmark-inc/bitmark-webgui && \
    /go/bin/bitmark-webgui -c /.config/webgui/webgui.conf setup


RUN bash -c "source ~/.nvm/nvm.sh && cd /.config/webgui/ui && \
             npm install && npm run build"

EXPOSE 2130 2135 2136 2150
CMD ["/go/bin/bitmark-webgui", "-c", "/.config/webgui/webgui.conf", "start"]

