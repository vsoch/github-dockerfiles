FROM quay.io/yeebase/neos-production:php71

COPY --chown=1001:1001 /app /app

RUN rm -rf /var/www && ln -s /app/Web /var/www && rm -Rf /app/Data/Temporary && \
    cp /app/Configuration/Settings.yaml.docker /app/Configuration/Production/Settings.yaml && \
    cp /app/Configuration/Caches.yaml.docker /app/Configuration/Production/Caches.yaml
