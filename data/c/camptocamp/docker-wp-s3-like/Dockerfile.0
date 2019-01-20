FROM wordpress:latest
MAINTAINER Christophe Burki, christophe.burki@camptocamp.com

RUN apt-get update && apt-get install -y --no-install-recommends \
    emacs24-nox \
    vim && \
    apt-get autoremove -y && \
    apt-get clean
    
COPY wp-config.php /var/www/html/wp-config.php
COPY wp-plugins/amazon-s3-and-cloudfront /var/www/html/wp-content/plugins/amazon-s3-and-cloudfront
COPY wp-plugins/amazon-web-services /var/www/html/wp-content/plugins/amazon-web-services
COPY wp-plugins/s3-like /var/www/html/wp-content/plugins/s3-like
