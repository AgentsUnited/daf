#!/bin/sh

docker-compose down && docker-compose build && docker-compose up -d > /dev/null 2>&1
echo "restarted" > daf_fifo
