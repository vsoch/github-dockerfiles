ARG node_version

FROM node:${node_version}-alpine
ARG yarn_version

ENV NODE_PATH /workspace/node_modules
ENV PATH $PATH:/workspace/node_modules/.bin

WORKDIR /home/node/thumbler

RUN \
	apk add --no-cache \
		dumb-init \
		g++ \
		gcc \
		git \
		make \
		openssh \
		python \
		tmux \
		vim && \
	rm -rf /opt/yarn* && \
	apk add --no-cache --repository  http://dl-cdn.alpinelinux.org/alpine/edge/community \
		"yarn>${yarn_version}"

COPY ./authorize.sh /usr/local/bin/ssh-auth

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
