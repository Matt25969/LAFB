# Number Generator

### Implementations
* **6digit.py** generates a 6-digit number.
* **8digit.py** generates a 8-digit number.

_Default = 6digit.py_

### Building the image

Use the following command to build the docker image:

`docker build --tag number --no-cache --build-arg APP_VERSION=[6digit.py/8digit.py] .`
