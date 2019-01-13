FROM asakaguchi/node:6.2.1
MAINTAINER Akiyoshi Sakaguchi <autumngoodluck@gmail.com>

ENV SRC /usr/local/src/app

RUN mkdir -p ${SRC}
WORKDIR ${src}

ONBUILD COPY package.json ${SRC}/
ONBUILD RUN npm install
ONBUILD COPY . ${SRC}

EXPOSE 3000

CMD ["npm", "start"]
