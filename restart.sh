#!/bin/sh

docker-compose stop daf && docker-compose rm -f daf && docker-compose build daf && docker-compose up -d > /dev/null 2>&1 
