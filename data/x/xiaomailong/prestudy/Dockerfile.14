FROM alpine_base

MAINTAINER Bolik WaterBolik@163.com

ENV GITBOOK_VERSION=3.2.2 \
	GITBOOK_DATA_DIR=/GitBookData \
    GITBOOK_HTML_DIR=/GitBookHTML

RUN set -x \
	&& mkdir -p ${GITBOOK_DATA_DIR} ${GITBOOK_HTML_DIR} \
	&& apk add --update --no-cache \
        nodejs \
        nodejs-npm \
    && NPM_MIRROR=npm.taobao.org \
    && npm install -g --registry=https://registry.${NPM_MIRROR}/ \
        gitbook-cli \
    && gitbook fetch ${GITBOOK_VERSION} \
    # && gitbook fetch latest \
    && npm cache clear \
	&& rm -rf /tmp/* \
    # add gitbook wrapper script
    && { \
		echo '#!/bin/sh -eu'; \
		echo '# gitbookw --- Wrapper for gitbook that autoinstalls plugins.'; \
		echo 'gitbook install'; \
		echo 'gitbook \$@'; \
	} > /usr/local/bin/gitbookw \  
    && cat /usr/local/bin/gitbookw \
    && chmod +x /usr/local/bin/gitbookw \
	&& echo "end"

VOLUME ${GITBOOK_DATA_DIR} ${GITBOOK_HTML_DIR}

WORKDIR ${GITBOOK_DATA_DIR}

EXPOSE 4000

CMD gitbook serve ${GITBOOK_DATA_DIR}
# ENTRYPOINT ["/entrypoint.sh"]

# CMD ["sh"]

# 编译及执行方法如下: 
# docker build -t gitbook /Volumes/Work/OpenSource/WaterBolik/prestudy/bdocker/gitbook/
# docker run -it --rm -p 8080:4000 -v /Volumes/Work/OpenSource/WaterBolik/prestudy/bdocker/gitbook/GitBookData/:/GitBookData/ gitbook
# docker run -it --rm -v /Volumes/Work/OpenSource/WaterBolik/prestudy/bdocker/gitbook/GitBookData/:/GitBookData/ -v /Volumes/Work/OpenSource/WaterBolik/prestudy/bdocker/gitbook/GitBookHTML/:/GitBookHTML/ gitbook gitbook build /GitBookData /GitBookHTML

# docker build -t gitbook B:\OpenSource\WaterBolik\prestudy\bdocker\gitbook\
# docker run -it --rm -p 8080:4000 -v B:/OpenSource/WaterBolik/prestudy/bdocker/gitbook/GitBookData/:/GitBookData/ gitbook
# docker run -it --rm -v B:/OpenSource/WaterBolik/prestudy/bdocker/gitbook/GitBookData/:/GitBookData/ -v B:/OpenSource/WaterBolik/prestudy/bdocker/gitbook/GitBookHTML/:/GitBookHTML/ gitbook gitbook build /GitBookData /GitBookHTML