#
# Base image for PostgreSQL 9.3 containers.
#
FROM    centos:centos6

MAINTAINER ddoyle <ddoyle@redhat.com>

# Update the system
RUN yum -y update && yum clean all

RUN echo "root:redhat" | chpasswd

# Expose the postgresql port.
EXPOSE 5432

############################################################################
# Install PostgreSQL 9.3
#
# Code taken from: https://github.com/DataVirtualizationByExample/DVWorkshop
###########################################################################
RUN yum -y install http://yum.postgresql.org/9.3/redhat/rhel-6-x86_64/pgdg-redhat93-9.3-1.noarch.rpm && yum -y install postgresql93-server postgresql93-contrib sudo && yum clean all

# Initialize the DB
RUN service postgresql-9.3 initdb

# Set Postgres environment variables
ENV PGDATA /var/lib/pgsql/9.3/data
ENV PGINST /usr/pgsql-9.3

# Create a homedir for the postgres user.
ENV HOME /home/postgres
RUN usermod -d $HOME postgres

# Set user to postgres.
USER postgres

#############################################
# Set the standard database user.
#############################################
RUN $PGINST/bin/pg_ctl start -w -D $PGDATA && \ 
    $PGINST/bin/psql --command "ALTER USER postgres PASSWORD 'postgres';" 

############################################
# Copy generic artifacts.
# Need to change back to root as COPY currently doesn't set file ownership to USER.
############################################
USER root
COPY dockerfile_copy/pgpass $HOME/.pgpass
COPY dockerfile_copy/pg_hba.conf $PGDATA/pg_hba.conf
RUN chown postgres:postgres $PGDATA/pg_hba.conf && chown postgres:postgres $HOME/.pgpass && chmod 0600 $HOME/.pgpass
USER postgres

# Adjust PostgreSQL configuration so that remote connections to the database are possible. 
RUN echo "listen_addresses='*'" >> $PGDATA/postgresql.conf && \
    echo "" >> $PGDATA/postgresql.conf

#CMD ["/bin/bash","-l"]
CMD /usr/pgsql-9.3/bin/postgres -D /var/lib/pgsql/9.3/data -c config_file=/var/lib/pgsql/9.3/data/postgresql.conf
