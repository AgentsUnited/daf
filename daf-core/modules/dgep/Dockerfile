FROM phusion/baseimage:latest-amd64
MAINTAINER m.snaith@dundee.ac.uk

# Get the necessary binaries
RUN apt-get update
RUN apt-get install -y python unzip lighttpd python-flup python-webpy python-pip python-dev

# Add the DGEP source
ADD src /dgep/src
ADD libs /dgep/libs
WORKDIR /dgep

# Python libraries
ADD requirements.txt /dgep/requirements.txt
RUN pip install -r requirements.txt

# Create a directory for saving dialogues
RUN mkdir -p /dgep/src/dialogues

EXPOSE 8888

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Run
CMD ["python", "-u", "-m", "src.start_dgep"]
