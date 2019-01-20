FROM node:8.11.3-jessie

RUN apt-get update

ADD package.json package-lock.json /tmp/

ADD . /code/

WORKDIR /tmp

RUN npm install
RUN rm -rf /code/node_modules
RUN cp -a /tmp/node_modules /code/node_modules

WORKDIR /code

EXPOSE 3000
CMD ["npm start"]