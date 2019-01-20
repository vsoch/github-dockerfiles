FROM unblibraries/drupal:alpine-nginx-php7-8.x-composer
MAINTAINER UNB Libraries <libsupport@unb.ca>

LABEL name="unbherbarium.lib.unb.ca"
LABEL vcs-ref=""
LABEL vcs-url="https://github.com/unb-libraries/unbherbarium.lib.unb.ca"

# Universal environment variables.
ENV DEPLOY_ENV prod
ENV DRUPAL_DEPLOY_CONFIGURATION TRUE
ENV DRUPAL_SITE_ID unbherb
ENV DRUPAL_SITE_URI unbherbarium.lib.unb.ca
ENV DRUPAL_SITE_UUID 85c96bf2-f1b6-4612-8305-d3d3769d5255
ENV DRUPAL_CONFIGURATION_EXPORT_SKIP devel
ENV DRUPAL_PRIVATE_FILE_PATH /app/private_filesystem

# git-lfs
ENV GIT_LFS_VERSION 2.2.0

# Add scripts, remove delete upstream drupal build.
COPY ./scripts/container /scripts
RUN /scripts/DeployUpstreamContainerScripts.sh && \
  /scripts/deleteUpstreamTree.sh

# Add Mail Sending, Rsyslog and ImageMagick/MagickSlicer, git-lfs
RUN apk --update add tiff-dev tiff postfix imagemagick bash rsyslog openssh-client && \
  rm -f /var/cache/apk/* && \
  curl -O https://raw.githubusercontent.com/VoidVolker/MagickSlicer/master/magick-slicer.sh && \
  mv magick-slicer.sh /usr/local/bin/magick-slicer && \
  chmod +x /usr/local/bin/magick-slicer && \
  touch /var/log/nginx/access.log && touch /var/log/nginx/error.log && \
  mkdir -p /var/spool/rsyslog; chgrp adm /var/spool/rsyslog; chmod g+w /var/spool/rsyslog && \
  /scripts/InstallGitLFS.sh

# Tests.
COPY ./tests ${DRUPAL_TESTING_ROOT}

# Add package conf.
COPY ./package-conf /package-conf
RUN mv /package-conf/postfix/main.cf /etc/postfix/main.cf && \
  mkdir -p /etc/rsyslog.d && \
  mv /package-conf/rsyslog/21-logzio-nginx.conf /etc/rsyslog.d/21-logzio-nginx.conf && \
  mv /package-conf/nginx/app.conf /etc/nginx/conf.d/app.conf && \
  mv /package-conf/php/app-php.ini /etc/php7/conf.d/zz_app.ini && \
  mv /package-conf/php/app-php-fpm.conf /etc/php7/php-fpm.d/zz_app.conf && \
  rm -rf /package-conf

# Deploy the generalized profile and makefile into our specific one.
COPY build/ ${TMP_DRUPAL_BUILD_DIR}
ENV DRUPAL_BUILD_TMPROOT ${TMP_DRUPAL_BUILD_DIR}/webroot
RUN /scripts/deployGeneralizedProfile.sh && \
  /scripts/installNewRelic.sh

# Build the drupal tree.
ARG COMPOSER_DEPLOY_DEV=no-dev
RUN /scripts/buildDrupalTree.sh ${COMPOSER_DEPLOY_DEV} && \
  /scripts/installDevTools.sh ${COMPOSER_DEPLOY_DEV} && \
  /scripts/clearComposerCache.sh

# Copy configuration.
COPY ./config-yml ${TMP_DRUPAL_BUILD_DIR}/config-yml

# Custom modules not tracked in github.
COPY ./custom/modules ${TMP_DRUPAL_BUILD_DIR}/custom_modules
COPY ./custom/themes ${TMP_DRUPAL_BUILD_DIR}/custom_themes
