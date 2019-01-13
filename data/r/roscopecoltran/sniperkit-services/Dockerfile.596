FROM alpine:3.5

LABEL maintainer "autumngoodluck@gmail.com"

ENV TEXTLINT_VERSION=7.3.0 \
    SHELL=/bin/sh
RUN set -x \
    && apk add --update --no-cache build-base python nodejs \
    && npm install -g chokidar-cli \
                      textlint@${TEXTLINT_VERSION} \
                      textlint-rule-no-todo \
                      textlint-rule-preset-ja-technical-writing \
                      textlint-rule-ja-yahoo-kousei \
                      textlint-rule-preset-ja-spacing \
                      textlint-rule-spellchecker \
                      textlint-plugin-html \
    && apk del build-base python

RUN set -x \
    && mkdir /textlint \
    && echo -e '{\n\
  "rules": {\n\
    "no-todo": true,\n\
    "preset-ja-technical-writing": true\n\
  }\n\
}' > /textlint/.textlintrc

WORKDIR /textlint

ENTRYPOINT ["textlint"]
CMD ["--help"]