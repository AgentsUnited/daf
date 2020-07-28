#FROM phusion/baseimage:latest
FROM debian:buster
MAINTAINER m.snaith@dundee.ac.uk

# Get the necessary binaries
#RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3 unzip lighttpd python-flup python3-pip python-dev git-all

ADD ./src /app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN pip3 install git+git://github.com/arg-tech/py-aspic

RUN pip3 freeze

CMD ["python3", "-u", "-m", "main"]
