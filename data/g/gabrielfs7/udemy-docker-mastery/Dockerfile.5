# create your custom drupal image here, based of official drupal
FROM drupal:8.2

# Install git to clone template in
RUN apt-get update \ 
    && apt-get install -y git \
    && rm -rf /var/lib/apt/lists/*

# Changing the working dir to execute command inside it
WORKDIR /var/www/html/themes

# Dowloads Drupal theme 'bootstratp' for 'themes' folder
RUN git clone --branch 8.x-3.x --single-branch --depth 1 https://git.drupal.org/project/bootstrap.git \
    && chown -R www-data:www-data bootstrap

# Changing the working dir to the default one
WORKDIR /var/www/html