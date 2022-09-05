# E-Learning CMS
This is an E-Learning CMS created with Django

## run memcached with docker

### run memcache
```sh
docker run -d --name my-memcache -p 11211:11211 memcached:alpine memcached -m 128
```

### create a network for redis

```sh
docker network create -d bridge redisnet
```

### run the redis container

```sh
docker run -d -p 6379:6379  --name course-redis --network redisnet redis:alpine
```