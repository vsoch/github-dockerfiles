FROM centos:latest
RUN yum install -y git
RUN yum install -y curl
RUN yum install -y vim


RUN git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

RUN git clone https://github.com/aliashq/docker_dev_dockerfile
RUN cp docker_dev_dockerfile/.vimrc ~/

RUN bash docker_dev_dockerfile/install.sh
RUN cp docker_dev_dockerfile/goconfig.sh /etc/profile.d/
RUN mkdir -p /gocode/src
RUN vim +PluginInstall +qall


RUN rm -rf docker_dev_dockerfile
RUN pwd
RUN git clone https://github.com/aliashq/docker_dev_dockerfile
RUN bash docker_dev_dockerfile/goPackageInstall.sh
