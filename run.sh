#!/bin/sh

# USAGE: ./run.sh --demo --activemq 127.0.0.1

function cleanup(){
#  echo "down" > daf_fifo
  docker-compose -f docker-compose.yml down --remove-orphans
  #docker network rm daf-network
}

# function restart(){
#   mkfifo daf_fifo
#   cat daf_fifo
#   rm daf_fifo
#   restart &
#   docker-compose logs -f
# }

trap cleanup TERM INT

opts=()
docker_opts=()

while [ $# -gt 0 ]; do

  test=$(echo $1 | cut -c1-2)
  if [ "$test" == "--" ]; then
    command=$(echo $1 | cut -c3-)
    case $command in
      demo)
        opts+=("demo=True"); opts+=("mongo=agents_united_demo") ;;
      testvars)
        opts+=("testvars=True");;
      activemq)
        shift; opts+=("activemq=$1") ;;
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

#create the docker network
# docker network create -d bridge daf-network

# bring up activemq
# docker run --rm --name activemq-external -p 8161:8161 --network="daf-network" webcenter/activemq:latest &

# restart &

# build the docker containers
docker-compose -f docker-compose.yml build --no-cache $buildArgs
docker-compose -f docker-compose.yml up -d --remove-orphans
docker-compose logs -f

# keep-alive even when daf is restarted
# wait
