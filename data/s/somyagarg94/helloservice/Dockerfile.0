FROM scratch
MAINTAINER Somya Garg <contact.somyagarg@gmail.com>

ARG git_repository="Unknown"
ARG git_commit="Unknown"
ARG git_branch="Unknown"
ARG built_on="Unknown"

LABEL git.repository=$git_repository
LABEL git.commit=$git_commit
LABEL git.branch=$git_branch
LABEL build.dockerfile=/Dockerfile
LABEL build.on=$built_on

EXPOSE 12345

COPY ./Dockerfile /Dockerfile

ADD bin/linux/helloservice /
CMD ["/helloservice"]