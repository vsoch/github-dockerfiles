FROM wombat/alpine:v0.1 AS build

ENV helm_version v2.9.1
RUN apk add -U --no-cache \
  bash \
  coreutils \
  curl \
  findutils \
  git \
  go \
  grep \
  libc-dev \
  linux-headers \
  make \
  rsync \
  gcc \
  glide \
  mercurial \
  && true

ENV GOPATH=/go PATH=$PATH:/go/bin
ENV HELM_URL https://github.com/kubernetes/helm.git

#ENV KUBERNETES_BRANCH pull/NNN/head
ENV HELM_COMMIT ${helm_version}
RUN mkdir -p $GOPATH/src/k8s.io && \
    cd $GOPATH/src/k8s.io && \
    git clone $HELM_URL helm

WORKDIR $GOPATH/src/k8s.io/helm

RUN set -e; \
    if [ -n "$HELM_BRANCH" ] ; then \
        git fetch origin "$HELM_BRANCH"; \
    fi; \
    git checkout -q $HELM_COMMIT

RUN glide install && make bootstrap build
RUN ./bin/helm init --client-only

RUN mkdir -p /out/etc/apk && cp -r /etc/apk/* /out/etc/apk/

RUN apk add --no-cache --initdb -p /out \
    alpine-baselayout \
    busybox \
    coreutils \
    curl \
    ebtables \
    ethtool \
    findutils \
    iproute2 \
    iptables \
    musl \
    openssl \
    openrc \
    rpcbind \
    socat \
    util-linux \
    nfs-utils \
    && true

RUN cp $GOPATH/src/k8s.io/helm/bin/helm /out/usr/bin/helm
RUN cp -R /root/.helm /out/root/.helm
ADD host.sh /out/usr/bin/host.sh

FROM scratch
ENTRYPOINT ["/usr/bin/host.sh"]
COPY --from=build /out /
COPY charts /host/charts
WORKDIR /host
EXPOSE 8879/udp 8879
