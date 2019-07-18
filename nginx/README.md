# docker-nginx
NGINX in Docker

This project is mainly used for quickly creating reverse proxies for other services

New location contexts can loaded, or copied into the running container at this location: `/etc/nginx/conf.d/*.conf`.  
When the config has been reloaded by nginx: `nginx -s reload` then it will be applied

Images with different tags have been uploaded to Docker Hub for specific services such as Jenkins: `bobcrutchley/nginx:jenkins`. 
These images have a reverse proxy already configured for that service, as long as the service contactable and running on its default port.
For instance the `bobcrutchley/nginx:jenkins` image contains this location context:
```nginx
location / {
    proxy_pass http://jenkins:8080/;
}
```
This will proxy any requests on `/` to the Jenkins host which is useful in setups with docker-compose and Kubernetes
