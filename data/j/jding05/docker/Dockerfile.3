#  ******************
#  dockerfiles ex01 *
#  ******************

# ex01.  From a debian image you will add the appropriate sources to create a TeamSpeak 
#   server, that will launch along with your container. It will be deemed valid if 
#   at least one user can connect to it and engage in a normal discussion 
#   (no far-fetched setup), so be sure to create your Dockerfile with the right 
#   options. Your program should get the sources when it builds, they cannot be in your 
#   repository.


FROM debian

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install wget -y
RUN apt-get install bzip2 -y

ENV TS3SERVER_LICENSE=accept

# get the link from https://www.teamspeak.com/en/downloads.html#server
# after tar it, you will get the file [teamspeak3-server_linux_amd64]
RUN wget http://dl.4players.de/ts/releases/3.1.3/teamspeak3-server_linux_amd64-3.1.3.tar.bz2
RUN tar -xjvf teamspeak3-server_linux_amd64-3.1.3.tar.bz2
RUN rm teamspeak3-server_linux_amd64-3.1.3.tar.bz2




# PORT 
#--------------------------
# 9987 default voice
# 10011 server query
# 30033 file transport

EXPOSE 9987/udp
EXPOSE 30033
EXPOSE 10011
# EXPOSE 41144

CMD ["sh", "teamspeak3-server_linux_amd64/ts3server_minimal_runscript.sh"]



# note:
# ------------------------------------------------------------------------------------
# 
# UDP (User Datagram Protocol) is an alternative communications protocol to 
#   Transmission Control Protocol (TCP) used primarily for establishing low-latency 
#   and loss tolerating connections between applications on the Internet. 
#   Both protocols send short packets of data, called datagrams.

# 9987 (Voice, UDP), 10011 (ServerQuery), 30033 (FileTransfer, TCP), 41144 (DNS)


# use debian
# set up the env with certificate
# download essential packages
# download the teamspeak file
# unzip it 
# run the file
# to test it do: docker build -t teamspeak .
# to test it do: docker run --name testfile teamspeak
# you will get the token
# paste it to the app to connect it. 

# test:
# ------------------------------------------------------------------------------------
# 
#docker/01_dockerfiles/ex01                                                                               
#▶ docker build ../ex01 -t teamspeak

#docker/01_dockerfiles/ex01
#▶ docker run -p 9987:9987/udp -it teamspeak

# open the teamspeak app
# enter docker-machine ip address
# enter the token from the docker run output
