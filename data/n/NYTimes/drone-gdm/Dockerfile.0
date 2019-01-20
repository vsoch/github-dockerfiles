FROM google/cloud-sdk:215.0.0-alpine
RUN /google-cloud-sdk/bin/gcloud components install beta --quiet

# Clean up
RUN rm -rf ./google-cloud-sdk/.install

ADD drone-gdm /bin/
ENTRYPOINT ["/bin/drone-gdm"]
