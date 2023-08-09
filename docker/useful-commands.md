# Some useful commands

## Getting Container ip

```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id_or_name>
```

## Deleting all images from the docker system

```
docker rmi -f $(docker images -aq)
```

## Delete all running and stopped containers

```
docker rm -f $(docker ps -aq)
```

## Delete all unused objects

```
docker system prune -a --volumes
```

## Stopping all the container

```
docker stop $(docker ps -q)
```
