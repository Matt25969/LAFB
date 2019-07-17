# Prize Generator

### Implementations
* **bigReward.py** is the more generous prize generator which provides bigger rewards (50% of £50)
* **smallReward.py** is the less generous prize generator which provides smaller rewards (25% of £10)

_Default = bigReward.py_

### Building the image

Use the following command to build the docker image:

`docker build --tag prize --no-cache --build-arg REWARD=[bigReward.py/smallReward.py] .`
