set COMPOSE_CONVERT_WINDOWS_PATHS=1

docker-compose stop daf
docker-compose rm -f daf
docker-compose build --build-arg demo=True daf > nul 2>&1
docker-compose up -d > nul 2>&1
