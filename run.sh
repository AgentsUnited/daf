#!/bin/sh

# USAGE: ./run.sh --demo --activemq 127.0.0.1

function cleanup(){
  docker-compose -f docker-compose.yml down --remove-orphans
  docker network rm daf-network
  rm daf.lock
}

trap cleanup TERM INT

LOCK="daf.lock"

if [ -f "$LOCK" ]; then
    echo "DAF is already running"
    exit 1
fi

opts=()
docker_opts=()

while [ $# -gt 0 ]; do

  test=$(echo $1 | cut -c1-2)
  if [ "$test" == "--" ]; then
    command=$(echo $1 | cut -c3-)
    case $command in
      demo)
        opts+=("demo=True") ;;
      testvars)
        opts+=("testvars=True") ;;
    esac
  else
    test=$(echo $1 | cut -c1)
    if [ "$test" == "-" ]; then
      option=$(echo $1 | cut -c2-)
      case $option in
        d)
          docker_opts+=("-d");;
      esac
    fi
  fi
  shift
done

buildArgs=""

for i in "${opts[@]}"
do
	buildArgs="$buildArgs --build-arg $i"
done

echo "$buildArgs" > daf.lock

docker network create -d bridge daf-network

# build the docker containers
docker-compose -f docker-compose.yml build --no-cache $buildArgs
docker-compose -f docker-compose.yml up -d --remove-orphans
docker-compose logs -f
