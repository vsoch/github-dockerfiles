FROM alpine_base

MAINTAINER Bolik WaterBolik@163.com

ENV ELECTRON_VERSION=3.2.2 \
	ELECTRON_DATA_DIR=/ElectronData 

RUN set -x \
	&& mkdir -p ${ELECTRON_DATA_DIR} \
	&& apk add --update --no-cache \
        nodejs \
        nodejs-npm \
        git \
    && NPM_MIRROR=npm.taobao.org \
    &&  { \
            echo "registry=https://registry.${NPM_MIRROR}/"; \ 
            echo "sass_binary_site=https://${NPM_MIRROR}/mirrors/node-sass/"; \
            echo "phantomjs_cdnurl=http://${NPM_MIRROR}/mirrors/phantomjs/"; \
            echo "ELECTRON_MIRROR=http://${NPM_MIRROR}/mirrors/electron/"; \
        } > ${HOME}/.npmrc \
    && cat ${HOME}/.npmrc \
    && npm install -g --registry=https://registry.${NPM_MIRROR}/ \
        cnpm \
        electron \
        electron-packager \
    && git clone https://github.com/electron/electron-quick-start ${ELECTRON_DATA_DIR} \
    && cd ${ELECTRON_DATA_DIR} \
    && cnpm install \
    && npm cache clear \
	&& rm -rf /tmp/* \
	&& echo "end"

VOLUME ${ELECTRON_DATA_DIR} 

WORKDIR ${ELECTRON_DATA_DIR}

EXPOSE 4000

CMD npm start
# ENTRYPOINT ["/entrypoint.sh"]

# CMD ["sh"]

# 编译及执行方法如下: 
# docker build -t electron /Volumes/Work/OpenSource/WaterBolik/prestudy/bdocker/electron/
# docker run -it --rm -p 8080:4000 -v /Volumes/Work/OpenSource/WaterBolik/prestudy/bdocker/electron/ElectronData/:/ElectronData/ electron

# docker build -t electron B:\OpenSource\WaterBolik\prestudy\bdocker\electron\
# docker run -it --rm -p 8080:4000 -v B:/OpenSource/WaterBolik/prestudy/bdocker/electron/ElectronData/:/ElectronData/ electron
