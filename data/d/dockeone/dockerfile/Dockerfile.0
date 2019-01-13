FROM gliderlabs/alpine:latest

#-h DIR          Home directory
#-g GECOS        GECOS field
#-s SHELL        Login shell
#-G GRP          Add user to existing group
#-S              Create a system user
#-D              Do not assign a password
#-H              Do not create home directory
#-u UID          User id

#-g GID  Group id
#-S      Create a system group


#There is no inherent difference between system groups and 'normal' groups, just like there is none between system users and regular users.
#It is by convention that human users are assigned uids from a certain number (e.g. 1000) upwards, whereas system users get uids in a range below that number.

#RUN addgroup -g 999 app && adduser -D  -G app -s /bin/sh -u 999 app

RUN apk add --update \
    python \
    py-pip \
  && pip install flask -U \
  && rm -rf /var/cache/apk/* \
  && adduser -D app \
  && mkdir /foo  \
  && chown -R app:app /foo

USER app

# add directly the jar
ADD main.py /foo/main.py

# creates a mount point
VOLUME /tmp

CMD python /foo/main.py

EXPOSE 8008
