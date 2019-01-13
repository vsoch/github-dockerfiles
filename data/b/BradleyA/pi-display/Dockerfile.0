###
#		Dockerfile  3.24.118  2018-07-03_19:35:35_CDT  https://github.com/BradleyA/pi-display  uadmin  one-rpi3b.cptx86.com 3.18  
#		   testing test1 
#		Dockerfile  3.17.116  2018-06-26_19:50:50_CDT  https://github.com/BradleyA/pi-display  uadmin  two-rpi3b.cptx86.com 3.16-2-g490b53f  
#		   more setup for testing yaml 
#		Dockerfile  3.07.82  2018-03-05_19:57:10_CST  https://github.com/BradleyA/pi-display  uadmin  two-rpi3b.cptx86.com 3.06-3-g39a0ee9  
#		   create-message.sh change directory for /usr/local/data/cluster-1 
#		Dockerfile	2.6.38	2018-02-26_21:15:17_CST uadmin three-rpi3b.cptx86.com 2.6 
#		   first pass at Dockerfile 
#		Dockerfile	2.6.37	2018-02-26_20:10:10_CST uadmin three-rpi3b.cptx86.com 2.5-1-gf452ccf 
#		   start working Dockerfile 
#	--rm -v /usr/local/data:/usr/local/data/ 
#	FROM resin/raspberry-pi-alpine                  # The bare bones Alpine Linux OS image for Ras
FROM resin/rpi-raspbian
LABEL MAINTAINER Bradley Allen
#	RUN apt-get update \
#		&& apt-get install 
COPY create-message.sh .
CMD ["/bin/bash", "create-message.sh"]

#	FROM blinkt
#	LABEL MAINTAINER Bradley Allen
#	COPY rainbow.py .
#	CMD ["python", "rainbow.py"]
###
##		ARG buildno
##		ARG gitcommithash
##		
##		RUN echo "Build number: $buildno"
##		RUN echo "Based on commit: $gitcommithash"
