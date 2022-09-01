# E-Learning CMS
This is an E-Learning CMS created with Django

## run memcached with docker

### run memcache
```sh
docker run -d --name my-memcache -p 11211:11211 memcached:alpine memcached -m 128
```