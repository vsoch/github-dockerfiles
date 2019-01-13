# create your custom drupal image here, based of official drupal
FROM drupal:8.2

#APT GET always creates a cache so we need to delete that cache. \ includes the next line in this command && If the first command succeed do the next one
RUN apt-get update && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html/themes

#chown - change owner, -R means all files subdirectoris and subfile. To this user and group ww-data:www-data and the directory bootstrap
RUN git clone --branch 8.x-3.x --single-branch --depth 1 https://git.drupal.org/project/bootstrap.git \
    && chown -R www-data:www-data bootstrap

#Change directory just in case application expects it to in the Working directory it started in
WORKDIR /var/www/html
