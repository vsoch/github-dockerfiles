FROM ubuntu:14.04

RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y -q unzip build-essential python-pip python-dev python-yaml libxml2-dev libxslt1-dev zlib1g-dev git curl sshpass openssh-client
RUN pip install --upgrade pyyaml jinja2 pycrypto

RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - && \
    apt-get install -y nodejs

RUN curl -O https://releases.hashicorp.com/vault/0.6.3/vault_0.6.3_linux_amd64.zip && \
    unzip ./vault_0.6.3_linux_amd64.zip -d /bin && \
    chmod +x /bin/vault

RUN git clone git://github.com/ansible/ansible.git --recursive /opt/ansible

RUN cd /opt/ansible && \
    git checkout v2.1.3.0-1 && \
    git submodule update --init --recursive && \
    bash -c 'source ./hacking/env-setup'

ENV PATH        /opt/ansible/bin:$PATH
ENV PYTHONPATH  /opt/ansible/lib:$PYTHONPATH
ENV MANPATH     /opt/ansible/docs/man:$MANPATH

ADD ./ssh /root/.ssh
RUN echo 'eval `ssh-agent`' >> /root/start.sh
RUN echo 'ssh-add /root/.ssh/id_rsa' >> /root/start.sh
RUN echo 'npm start' >> /root/start.sh
RUN chmod +x /root/start.sh

ADD ./ansible/ /ansible
RUN cd /ansible && npm install

ADD ./deployer/ /deployer
RUN cd /deployer && npm install

WORKDIR /deployer
CMD /root/start.sh
