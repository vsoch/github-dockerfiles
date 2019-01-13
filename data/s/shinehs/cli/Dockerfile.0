FROM node:8.11.4

SHELL ["/bin/bash", "-c"]
RUN apt-get update \
  && apt-get install vim -y \
  && git clone https://github.com/shinehs/cli.git \
  && mkdir Dockerfile \
  && cd /cli/task \
  && cp -rv package.json /Dockerfile/ \
  && cp -rv config-overrides.js /Dockerfile/ \
  && cd / \
  && cd Dockerfile \
  && npm install \
  && cd / \
  && cd /Dockerfile/node_modules/react-scripts/config \
  && rm -f paths.js \
  && cd / \
  && cd /cli/task \
  && cp -rv paths.js /Dockerfile/node_modules/react-scripts/config \
  && echo 'registry=https://npm-registry.yy.com' >> ~/.npmrc \
