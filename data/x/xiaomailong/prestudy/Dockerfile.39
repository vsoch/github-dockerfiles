FROM alpine_base

MAINTAINER Bolik WaterBolik@163.com

RUN set -ex \
    && apk --no-cache add \
        lighttpd \
        php5-cgi \
        php5-curl \
        php5-gd \
        php5-json \
		php5-openssl \
        php5-xml \
        php5-zlib \
        curl \
        tar \
        git \
    && echo "end"

RUN set -ex \
    # && VERSION=`git ls-remote -t https://github.com/splitbrain/dokuwiki \
	#     | grep -Po '(?<=release_stable_)[0-9a-z-]*' \
	#     | sort -ubt - -k 1,1nr -k 2,2nr -k 3,3r \
	#     | head -n 1` \
    && VERSION=2017-02-19b \
    && echo ${VERSION} \
	&& curl -sL https://github.com/splitbrain/dokuwiki/archive/release_stable_$VERSION.tar.gz \
		| tar xz -C /srv --strip-components=1 \
	&& chown -R lighttpd. /srv \
    && apk del curl tar \
    && sed -ie "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php5/php.ini \
    && echo "end"

COPY lighttpd.conf /etc/lighttpd/

USER lighttpd

VOLUME ["/srv/data", "/srv/lib/plugins", "/srv/conf", "/srv/lib/tpl"]

EXPOSE 8080

ENTRYPOINT ["lighttpd"]

CMD ["-D", "-f", "/etc/lighttpd/lighttpd.conf"]


# 编译及执行方法如下: 
#     $ docker build -t dokuwiki /Volumes/Work/OpenSource/WaterBolik/prestudy/bdocker/dokuwiki/
#     $ docker run -it --rm -p 8080:8080 -v /Volumes/Work/OpenSource/WaterBolik/prestudy/bdocker/dokuwiki/data/:/srv/data/ dokuwiki
#     docker build -t dokuwiki B:/OpenSource/WaterBolik/prestudy/bdocker/dokuwiki/
#     docker run -it --rm -p 8080:8080 -v B:/OpenSource/WaterBolik/prestudy/bdocker/dokuwiki/data/:/srv/data/ dokuwiki