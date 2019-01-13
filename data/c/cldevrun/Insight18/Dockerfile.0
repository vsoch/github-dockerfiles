# Set base image to Python 3
FROM python:3.6.5

ENV PYTHONUNBUFFERED 1

# Install FreeTDS and dependencies for PyODBC
RUN apt-get update && apt-get install -y tdsodbc unixodbc-dev \
 && apt install unixodbc-bin -y  \
 && apt-get clean -y

RUN echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/arm-linux-gnueabi/odbc/libtdsodbc.so\n\
Setup = /usr/lib/arm-linux-gnueabi/odbc/libtdsS.so" >> /etc/odbcinst.ini

# Create Dockerfile directory
RUN mkdir /pythonFrontEnd

# Add current directory files to the Dockerfile directory
ADD ./* /pythonFrontEnd/

# Set working directory for future RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile.
WORKDIR /pythonFrontEnd

# Install Python modules
RUN pip install -r requirements.txt

# Expose some Docker port to outside world so people can access it
EXPOSE 5001

# The last thing that should be present in a Dockerfile
# Main purpose of CMD is to provide defaults for an existing container, will get app running.
# CMD ./run_server.sh
CMD python app.py

