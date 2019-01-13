FROM alpine:3.4
MAINTAINER smizy

RUN set -x \
    && apk update \
    && apk --no-cache add \
        ca-certificates \
        freetype \
        python3 \
        su-exec \
        tini \
    && apk --no-cache add  \
        --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
        openblas \
        py3-zmq \
    && pip3 install --upgrade pip \
    && pip3 install ipywidgets \
    && pip3 install jupyter-console \   
    ## numpy 
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && apk --no-cache add --virtual .builddeps.edge.community \
        --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
        openblas-dev \
    && apk --no-cache add --virtual .builddeps \
        build-base \
        freetype-dev \
        gfortran \
        python3-dev \
    && pip3 install numpy \
    ## scipy
    && pip3 install scipy \
    ## pnadas 
    && apk --no-cache add  \
        --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ \
        py3-dateutil \
        py3-tz \
    && pip3 install pandas \
    ## scikit-learn 
    && pip3 install scikit-learn \
    ## seaborn/matplotlib
    && pip3 install seaborn \
    ## clean
    && apk del \
        .builddeps \
        .builddeps.edge.community \
    && find /usr/lib/python3.5 -name __pycache__ | xargs rm -r \
    && rm -rf /root/.[acpw]* \
    ## dir
    && mkdir -p /etc/jupyter \
    ## user
    && adduser -D  -g '' -s /sbin/nologin -u 1000 docker \
    && adduser -D  -g '' -s /sbin/nologin jupyter 

WORKDIR /code

COPY entrypoint.sh  /usr/local/bin/
COPY jupyter_notebook_config.py /etc/jupyter/

EXPOSE 8888

ENTRYPOINT ["tini", "--", "entrypoint.sh"]
CMD ["jupyter", "notebook"]