FROM phusion/baseimage:latest
MAINTAINER m.snaith@dundee.ac.uk

# Get the necessary binaries
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3.6 unzip lighttpd python-flup python-webpy python3-pip python-dev

ADD ./src /app
WORKDIR /app

RUN pip3 install -r requirements.txt

RUN python3 --version

CMD ["python3", "-u", "-m", "main"]
