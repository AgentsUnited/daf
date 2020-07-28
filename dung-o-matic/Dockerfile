FROM php:7.1-apache-stretch

RUN mkdir -p /usr/share/man/man1

RUN apt-get update && \
    apt-get -y install default-jdk && \
    apt-get -y install ant

ADD . /dungomatic
WORKDIR /dungomatic

RUN ant && ant jar

ADD html/dom /var/www/html/
