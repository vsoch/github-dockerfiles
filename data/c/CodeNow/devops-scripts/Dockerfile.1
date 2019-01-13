FROM dockerfile/ansible

# Update aptitude with new repo
RUN apt-get update

# Install software
RUN apt-get install -y build-essential wget make git

# Make ssh dir
RUN mkdir /root/.ssh/
ADD ./Test-runnable.pem /root/.ssh/Test-runnable.pem
ADD ./runnablevpc.pem /root/.ssh/runnablevpc.pem

# add .ssh config file
ADD config /root/.ssh/config

# Copy over private key,
ADD id_rsa /root/.ssh/id_rsa

# set correct permissions
RUN chmod 600 /root/.ssh/id_rsa
