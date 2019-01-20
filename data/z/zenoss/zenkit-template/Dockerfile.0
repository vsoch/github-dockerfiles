{{ $pkg := print ((print (env "GOPATH") "/src/") | trimPrefix (env "PWD")) "/" Name -}}
ARG ZENKIT_BUILD_VERSION=1.7.3

FROM zenoss/zenkit-build:${ZENKIT_BUILD_VERSION}

COPY . /go/src/{{$pkg}}
WORKDIR /go/src/{{$pkg}}
RUN go build -o /bin/{{Name}}

FROM alpine
RUN apk add --no-cache curl

COPY --from=0 /bin/{{Name}} /bin/{{Name}}
RUN addgroup -S zing && adduser -S -G zing -u 512 512
USER 512

EXPOSE {{Port}}

CMD ["/bin/{{Name}}"]
