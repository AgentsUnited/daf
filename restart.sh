#!/bin/sh

LOCK="daf.lock"

buildArgs=""

if [ -f "$LOCK" ]; then
  while read -r line; do
    echo "$line"
    buildArgs="$buildArgs $line"
  done < "$LOCK"

  docker-compose stop daf
  docker-compose rm -f daf
  docker-compose build $buildArgs daf > /dev/null 2>&1
  docker-compose up -d > /dev/null 2>&1
else
  echo "DAF is not running"
fi
