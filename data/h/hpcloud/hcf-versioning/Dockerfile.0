FROM package/git

ADD https://github.com/colstrom/git-notary/releases/download/2.1.1/git-notary /usr/local/bin/
RUN chmod +x /usr/local/bin/git-notary
RUN apk-install bc openssh-client
RUN mkdir ~/.ssh
RUN chmod 0700 ~/.ssh
RUN ssh-keyscan github.com | tee ~/.ssh/known_hosts
