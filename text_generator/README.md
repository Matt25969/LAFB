# Text Generator

### Implementations
* **2char.py** generates a 3 char String of lowercase letters.
* **3char.py** generates a 2 char String of uppercase letters.

_Default = 3char.py_

### Building the image

Use the following command to build the docker image:

`docker build --tag prize --no-cache --build-arg REWARD=[2char.py/3char.py] .`
