FROM buildpack-deps:jessie-scm

RUN apt-get update
RUN apt-get install -y \
        g++ gcc libc6-dev make \
        vim unzip build-essential autoconf automake libtool \
        --no-install-recommends

WORKDIR /root

# Protobufs
RUN curl -fsSL https://github.com/google/protobuf/releases/download/v3.3.0/protoc-3.3.0-linux-x86_64.zip -o protoc.zip && unzip protoc.zip
RUN mv bin/protoc /usr/bin && chmod +x /usr/bin/protoc

# Golang
ENV GOLANG_VERSION 1.8
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz
ENV GOLANG_DOWNLOAD_SHA256 53ab94104ee3923e228a2cb2116e5e462ad3ebaeea06ff04463479d7f12d27ca
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \
    && echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - \
    && tar -C /usr/local -xzf golang.tar.gz \
    && rm golang.tar.gz
ENV GOPATH /go
ENV GOBIN /go/bin
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"

RUN mkdir -p /go/src/github.com/ReturnPath/protoc-gen-template/vendor

COPY ./vendor /go/src/github.com/ReturnPath/protoc-gen-template/vendor
RUN cd /go/src/github.com/ReturnPath/protoc-gen-template/vendor/github.com/golang/protobuf/protoc-gen-go && go install

COPY . /go/src/github.com/ReturnPath/protoc-gen-template
WORKDIR /go/src/github.com/ReturnPath/protoc-gen-template

CMD ["/bin/bash", "/go/src/github.com/ReturnPath/protoc-gen-template/build.sh"]


