set COMPOSE_CONVERT_WINDOWS_PATHS=1

docker-compose -f docker-compose.yml build --no-cache --build-arg demo=True --build-arg standalone=True
docker-compose -f docker-compose.yml up --remove-orphans && docker-compose -f docker-compose.yml down --remove-orphans
