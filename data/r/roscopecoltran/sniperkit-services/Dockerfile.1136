FROM jenkins:2.32.1-alpine

MAINTAINER Dragos Cirjan "dragos.cirjan@itmediaconnect.ro"

ENV JENKINS_THEME_MATERIAL_COLOR deep-purple

ENV JENKINS_INSTALL_PLUGINS 'simple-theme-plugin'

COPY docker-entrypoint.sh /

# | Plugin              | Used For                                   |
# | simple-theme-plugin | http://afonsof.com/jenkins-material-theme/ |
# | ssh                 | Deploying over ssh                         |
RUN install-plugins.sh simple-theme-plugin ssh

ENTRYPOINT ["sh", "/docker-entrypoint.sh"]