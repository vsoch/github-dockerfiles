FROM mhart/alpine-node:7.8.0

RUN apk update
RUN apk --update --no-cache \
		add  \
    automake \
		git \
		alpine-sdk  \
		nasm  \
		autoconf  \
		build-base \
		zlib \
		zlib-dev \
		libpng \
		libpng-dev\
		libwebp \
		libwebp-dev \
		libjpeg-turbo \
		libjpeg-turbo-dev

RUN npm install -g bower polymer-cli gulp-cli

ADD bower.json /tmp/
ADD package.json /tmp/

ADD . /code/

WORKDIR /tmp

RUN npm install
RUN bower --allow-root install

RUN rm -rf /code/node_modules
RUN rm -rf /code/bower_components
RUN cp -a /tmp/node_modules /code/node_modules
RUN cp -a /tmp/bower_components /code/bower_components

WORKDIR /code

EXPOSE 8082
CMD ["npm", "run", "dev"]
