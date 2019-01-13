#
# Ubuntu Desktop (Gnome) Dockerfile
#
# https://github.com/intlabs/Docker-Ubuntu-Desktop-Gnome
#

# Install GNOME3 and VNC server.
# (c) Pete Birley

# Pull base image.
FROM dockerfile/ubuntu

# Setup enviroment variables
ENV DEBIAN_FRONTEND noninteractive

#Update the package manager and upgrade the system
RUN apt-get update && \
apt-get upgrade -y && \
apt-get update

# Install supervisor
RUN apt-get install -y supervisor

# Installing fuse filesystem is not possible in docker without elevated priviliges
# but we can fake installling it to allow packages we need to install for GNOME
RUN apt-get install libfuse2 -y && \
cd /tmp ; apt-get download fuse && \
cd /tmp ; dpkg-deb -x fuse_* . && \
cd /tmp ; dpkg-deb -e fuse_* && \
cd /tmp ; rm fuse_*.deb && \
cd /tmp ; echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst && \
cd /tmp ; dpkg-deb -b . /fuse.deb && \
cd /tmp ; dpkg -i /fuse.deb

# Upstart and DBus have issues inside docker.
RUN dpkg-divert --local --rename --add /sbin/initctl && ln -sf /bin/true /sbin/initctl

# Install GNOME and tightvnc server.
RUN apt-get update && apt-get install -y xorg gnome-core gnome-session-fallback tightvncserver libreoffice

# Install Polydesk base tools
RUN add-apt-repository ppa:webupd8team/sublime-text-3 && apt-get update
RUN apt-get install -y sublime-text-installer git subversion cvs gedit inkscape thunderbird chromium-browser

# Pull in the hack to fix keyboard shortcut bindings for GNOME 3 under VNC
ADD https://raw.githubusercontent.com/CannyComputing/Dockerfile-Ubuntu-Gnome/master/gnome-keybindings.pl /usr/local/etc/gnome-keybindings.pl
RUN chmod +x /usr/local/etc/gnome-keybindings.pl

# Add the script to fix and customise GNOME for docker
ADD https://raw.githubusercontent.com/CannyComputing/Dockerfile-Ubuntu-Gnome/master/gnome-docker-fix-and-customise.sh /usr/local/etc/gnome-docker-fix-and-customise.sh
RUN chmod +x /usr/local/etc/gnome-docker-fix-and-customise.sh

# Set up VNC
RUN mkdir -p /root/.vnc
ADD https://raw.githubusercontent.com/CannyComputing/Dockerfile-Ubuntu-Gnome/master/xstartup /root/.vnc/xstartup
RUN chmod 755 /root/.vnc/xstartup
ADD https://raw.githubusercontent.com/CannyComputing/Dockerfile-Ubuntu-Gnome/master/spawn-desktop.sh /usr/local/etc/spawn-desktop.sh
RUN chmod +x /usr/local/etc/spawn-desktop.sh
RUN apt-get install -y expect
ADD https://raw.githubusercontent.com/CannyComputing/Dockerfile-Ubuntu-Gnome/master/start-vnc-expect-script.sh /usr/local/etc/start-vnc-expect-script.sh
RUN chmod +x /usr/local/etc/start-vnc-expect-script.sh
ADD https://raw.githubusercontent.com/CannyComputing/Dockerfile-Ubuntu-Gnome/master/vnc.conf /etc/vnc.conf

# Set up supervisord
ADD start-vncserver.sh /start-vncserver.sh
ADD chvncpasswd.sh 	/chvncpasswd.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh
ADD supervisord-vncserver.conf /etc/supervisor/conf.d/supervisord-vncserver.conf


RUN sed 's/Exec=chromium-browser %U/Exec=chromium-browser %U --no-sandbox --user-data-dir/g' </usr/share/applications/chromium-browser.desktop >/usr/share/applications/chromium-browser.desktop

# Define mountable directories.
VOLUME ["/data"]

# Define working directory.
WORKDIR /data

# Define default command.
# CMD bash -C '/usr/local/etc/spawn-desktop.sh';'bash'
CMD ["/run.sh"]

# Expose ports.
EXPOSE 5901
