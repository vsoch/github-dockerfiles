FROM smizy/scikit-learn:0.18-alpine

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.docker.dockerfile="/Dockerfile" \
    org.label-schema.license="Apache License 2.0" \
    org.label-schema.name="smizy/gensim" \
    org.label-schema.url="https://gitlab.com/smizy" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-type="Git" \
    org.label-schema.version=$VERSION \
    org.label-schema.vcs-url="https://github.com/smizy/docker-gensim"

ENV GENSIM_VERSION  $VERSION

RUN set -x \
    && apk update \
    ## word2vec/fasttext
    && apk --no-cache add \
        bash \
        libstdc++ \
    && apk --no-cache add --virtual .builddeps \
        build-base \
        git \
        openblas-dev \
        python3-dev \
    # fastText
    && git clone https://github.com/facebookresearch/fastText.git \
    && cd fastText \
    && make \
    && mv fasttext /usr/local/bin/ \
    && rm -rf .git \       
    && cd .. \
    ## word2vec
    && git clone https://github.com/svn2github/word2vec.git \
    && cd word2vec \
    && make \
    && mv word2vec /usr/local/bin/ \
    && mv word2phrase /usr/local/bin/ \
    && mv distance /usr/local/bin/ \
    && mv word-analogy /usr/local/bin/ \
    && mv compute-accuracy /usr/local/bin/ \
    && rm -rf .git \
    && cd .. \
    ## gensim
    && pip install \
        cython \
        gensim==${GENSIM_VERSION} \
    ## clean 
    && apk del  .builddeps \
    && find /usr/lib/python3.5 -name __pycache__ | xargs rm -r \
    && rm -rf /root/.[acpw]* 