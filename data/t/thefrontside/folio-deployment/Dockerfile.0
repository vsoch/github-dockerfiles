FROM maven:3.5

#ENV DEBIAN_FRONTEND=teletype

# Dependencies for Ruby/RVM and Postgres
RUN apt-get update -qq && apt-get install -qq -y jq postgresql postgresql-contrib openssh-server git-core openssh-client build-essential openssl libreadline7 libreadline-dev curl zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev autoconf libc6-dev libncurses5-dev automake libtool bison subversion pkg-config > /dev/null

# RVM needed to react properly to ruby version
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
RUN echo 'export rvm_prefix="$HOME"' > /root/.rvmrc
RUN echo 'export rvm_path="$HOME/.rvm"' >> /root/.rvmrc
RUN echo 'export rvm_install_on_use_flag=1' >> /root/.rvmrc
RUN curl -sSL https://get.rvm.io | rvm_path=/opt/rvm bash -s
ENV PATH="/root/.rvm/bin:${PATH}"
RUN /bin/bash -c "source $HOME/.rvm/scripts/rvm"
RUN /bin/bash -c "rvm requirements"



# Scripts for registration/discovery/provisioning
COPY *.sh /usr/local/bin/folio/

ENTRYPOINT []
