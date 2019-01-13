FROM sdelements/lets-chat

USER root

ENV EXTRACT_VCAP_URL=https://raw.githubusercontent.com/osowski/ibm-containers/master/utils/docker-build/extract-vcap.py

RUN apt-get update && apt-get install -y python

RUN mkdir scripts
ADD scripts scripts
ADD $EXTRACT_VCAP_URL scripts/extract-vcap.py
RUN chmod +r scripts/extract-vcap.py

USER node

CMD ["scripts/start-server.sh"]

