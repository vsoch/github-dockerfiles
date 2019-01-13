# see http://container-solutions.com/running-docker-in-jenkins-in-docker/
FROM jenkins:2.60.1

#ENV BASE_APKS="sudo openssl openssh-client ttf-dejavu maven git curl " \
#BUILD_APKS="build-essential make gcc clang g++ autoconf bison"
ENV BASE_APKS="sudo openssl openssh-client git curl jq git mercurial rsync" \
    BUILD_APKS="build-essential autoconf ansible make binutils bison gcc " 

USER root
RUN apt-get update \
      && apt-get install -y $BASE_APKS $BUILD_APKS \
      && rm -rf /var/lib/apt/lists/*
#RUN apt-get install -y libapparmor-dev

RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

#RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - \
#  && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
#  && apt-get update \
RUN curl -sSL https://get.docker.com/ | sh \
  && usermod -a -G staff,docker jenkins  

#  Add Go
ENV GOLANG_VERSION 1.7.6

RUN set -eux; \
	\
# this "case" statement is generated via "update.sh"
	dpkgArch="$(dpkg --print-architecture)"; \
	case "${dpkgArch##*-}" in \
		ppc64el) goRelArch='linux-ppc64le'; goRelSha256='8b5b602958396f165a3547a1308ab91ae3f2ad8ecb56063571a37aadc2df2332' ;; \
		i386) goRelArch='linux-386'; goRelSha256='99f79d4e0f966f492794963ecbf4b08c16a9a268f2c09053a5ce10b343ee4082' ;; \
		s390x) goRelArch='linux-s390x'; goRelSha256='d692643d1ac4f4dea8fb6d949ffa750e974e63ff0ee6ca2a7c38fc7c90da8b5b' ;; \
		armhf) goRelArch='linux-armv6l'; goRelSha256='fc5c40fb1f76d0978504b94cd06b5ea6e0e216ba1d494060d081e022540900f8' ;; \
		amd64) goRelArch='linux-amd64'; goRelSha256='ad5808bf42b014c22dd7646458f631385003049ded0bb6af2efc7f1f79fa29ea' ;; \
		*) goRelArch='src'; goRelSha256='1a67a4e688673fdff7ba41e73482b0e59ac5bd0f7acf703bc6d50cc775c5baba'; \
			echo >&2; echo >&2 "warning: current architecture ($dpkgArch) does not have a corresponding Go binary release; will be building from source"; echo >&2 ;; \
	esac; \
	\
	url="https://golang.org/dl/go${GOLANG_VERSION}.${goRelArch}.tar.gz"; \
	wget -O go.tgz "$url"; \
	echo "${goRelSha256} *go.tgz" | sha256sum -c -; \
	tar -C /usr/local -xzf go.tgz; \
	rm go.tgz; \
	\
	if [ "$goRelArch" = 'src' ]; then \
		echo >&2; \
		echo >&2 'error: UNIMPLEMENTED'; \
		echo >&2 'TODO install golang-any from jessie-backports for GOROOT_BOOTSTRAP (and uninstall after build)'; \
		echo >&2; \
		exit 1; \
	fi; \
	\
	export PATH="/usr/local/go/bin:$PATH"; \
	go version

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH

#COPY go-wrapper /usr/local/bin/

USER jenkins
