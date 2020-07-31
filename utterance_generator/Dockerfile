FROM python:3.7-stretch
MAINTAINER m.snaith@dundee.ac.uk

# Get the necessary binaries
RUN apt-get update
RUN apt-get install -y unzip lighttpd python-flup python3-pip python-dev git-all

ADD ./src /app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN pip3 install git+git://github.com/arg-tech/py-aspic

CMD ["python3", "-u", "-m", "main"]
