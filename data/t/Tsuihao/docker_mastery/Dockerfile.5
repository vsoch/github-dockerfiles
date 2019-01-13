# create your custom drupal image here, based of official drupal
FROM drupal:8.2
# -y means automatically say yes
# during the git install there will be around 10 MB cache which we will not want to expend the size of image
RUN apt-get update && apt-get install -y git \
    && rm -rf /var/lib/apt/lits/*

WORKDIR /var/www/html/themes

# change owener  -R (All files)
RUN git clone --branc 8.x-3.x --single-branch --depth 1 https://git.drupal.org/project/bootstrap.git \
    && chown -R www-data:www-data bootstrap

WORKDIR /var/www/html

# drupal is alreay specify the CMD
