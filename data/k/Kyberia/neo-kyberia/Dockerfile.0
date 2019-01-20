FROM ubuntu:16.10

ENV KYBERIA_PASSWD what
ENV TERM screen-256color

EXPOSE 80

RUN apt-get update && apt-get install -qy apt-utils && \
    apt-get install -qy zsh aptitude git

RUN apt-get install -qy apache2 postgresql libapache2-mod-php7.0 \
                        php-pgsql \
                        elinks
RUN cd /etc/apache2/mods-enabled && ln -s ../mods-available/rewrite.load

RUN useradd -ms /bin/zsh kyberia

RUN mkdir -p /p && \
    git clone https://github.com/Kyberia/neo-kyberia.git /p/neo-kyberia && \
    chown -R kyberia:kyberia /p/neo-kyberia

RUN cp /p/neo-kyberia/k42/setup/apache/sample_k42.conf \
       /etc/apache2/sites-available/023-kyberia.conf && \
    cd /etc/apache2/sites-enabled && ln -s ../sites-available/023-kyberia.conf && \
    unlink 000-default.conf && \
    \
    ln -s /p/neo-kyberia/k42 /var/www/ &&  \
    mkdir -p /var/www/k42/inc/smarty/templates_c && \
    chown -R www-data:www-data /var/www/k42/inc/smarty/templates_c && \
    \
    sed -i "s/vivatpicat/${KYBERIA_PASSWD}/" /p/neo-kyberia/k42/config/config.inc

USER postgres
RUN /etc/init.d/postgresql start && \
    createuser --superuser root && \
    psql --command "CREATE USER kyberia WITH SUPERUSER PASSWORD '${KYBERIA_PASSWD}';" && \
    createdb -O kyberia kyberia42 && \
    umask 0177 && echo "127.0.0.1:5432:kyberia42:kyberia:${KYBERIA_PASSWD}" > ~/.pgpass

RUN /etc/init.d/postgresql start && \
    psql -U kyberia -h 127.0.0.1 kyberia42 -w < /p/neo-kyberia/k42/setup/psql/psql_init_dump_new.sql && \
    psql --command "ALTER USER kyberia WITH NOSUPERUSER"

USER root
ENTRYPOINT /etc/init.d/postgresql start && \
           /etc/init.d/apache2 start && \
           zsh -l

