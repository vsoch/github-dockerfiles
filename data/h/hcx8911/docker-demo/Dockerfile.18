FROM alpine-nodejs
# FROM node:alpine

LABEL MAINTAINER="WaterBolik@163.com"

VOLUME /usr/src/app

WORKDIR /usr/src/app

ARG REACT_APP_USERS_SERVICE_URL
ARG NODE_ENV
ENV NODE_ENV=$NODE_ENV
ENV REACT_APP_USERS_SERVICE_URL=$REACT_APP_USERS_SERVICE_URL
ARG REACT_APP_EVAL_SERVICE_URL
ENV REACT_APP_EVAL_SERVICE_URL=$REACT_APP_EVAL_SERVICE_URL

RUN set -euxo pipefail \
    && npm install --global \
        --registry=https://registry.npm.taobao.org \
        pushstate-server
        # create-react-app \
        # react-scripts \
# add app
# ADD . /usr/src/app

EXPOSE 9000

# start app
CMD ["npm", "start"]

# start app
# CMD ["pushstate-server", "build"]
# CMD sh

# 编译及执行方法如下:
# $ docker build -t users-client ~/OpenSource/WaterBolik/docker-demo/flask/flask-microservices-users/users-client/
# $ docker build -t users-client B:\OpenSource\WaterBolik\docker-demo\flask\flask-microservices-users\users-client\
# $ docker run -it --rm -p 3000:3000 -v ~/OpenSource/WaterBolik/docker-demo/flask/flask-microservices-users/users-client/app:/usr/src/app users-client

# --registry=https://registry.npm.taobao.org
# $ npm install --global create-react-app
# 创建 react 项目
# $ create-react-app .
# 安装 Axios to manage the AJAX call
# $ npm install axios --save
# $ yarn add axios
