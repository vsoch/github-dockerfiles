FROM rlpowell/fedora_base

# Specifically needed packages, with versions where the package is
# important.
RUN dnf -y install ruby-devel libxml2-devel libxslt-devel redhat-rpm-config bzip2

# Language issues
RUN /bin/echo 'LANG=en_US.UTF-8' >/etc/locale.conf
ENV LANG en_US.UTF-8

# User setup
RUN mkdir /srv/freq
WORKDIR /srv/freq
RUN echo 'freq    ALL=(ALL)    NOPASSWD: ALL' >>/etc/sudoers.d/freq

# Ruby setup
COPY Gemfile /srv/freq/
RUN gem install bundler
RUN bundle config --global silence_root_warning true 
RUN bundle config build.nokogiri --use-system-libraries
RUN bundle install

# Stuff to do on "boot"
COPY docker_init.sh /tmp/docker_init.sh
RUN sudo dos2unix /tmp/docker_init.sh
RUN sudo chmod 755 /tmp/docker_init.sh
