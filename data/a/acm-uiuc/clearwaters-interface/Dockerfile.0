FROM node:boron
MAINTAINER ACM@UIUC

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json /usr/src/app/
RUN yarn install

# Bundle app source
COPY . /usr/src/app

EXPOSE 3001

CMD [ "yarn", "run", "start"]