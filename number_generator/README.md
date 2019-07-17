# Number Generator

### Implementations
* **6digit.py** generates a 6-digit number.
* **8digit.py** generates a 8-digit number.

_Default = 6digit.py_

### Building the image

Use the following command to build the docker image:

`docker build --tag number --no-cache --build-arg REWARD=[6digit.py/8digit.py] .`

### DockerHub images

The images can found in their DockerHub [repository](https://cloud.docker.com/u/teamdeadweight/repository/docker/teamdeadweight/number_generator).
