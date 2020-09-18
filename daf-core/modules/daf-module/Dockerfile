###############################################
# Base image for modules in the Agents United #
# Dialogue and Argumentation Framework        #
###############################################

FROM python:3.7-stretch
MAINTAINER mark@arg.tech

# Get the necessary binaries
RUN apt-get update && \
    apt-get install -y unzip lighttpd python-flup python3-pip python-dev git-all &&\
    apt-get clean

# Update pip
RUN pip3 install --upgrade pip

# Add the daf module library
ADD src /daf-libs/daf

# Install the daf module library
RUN pip3 install -e /daf-libs/daf
