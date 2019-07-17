# Prize Generator

### Implementations
* **bigReward.py** is the more generous prize generator which provides bigger rewards (50% chance of getting £50)
* **smallReward.py** is the less generous prize generator which provides smaller rewards (25% chance of getting £10)

_Default = bigReward.py_

### Building the image

Use the following command to build the docker image:

`docker build --tag prize --no-cache --build-arg REWARD=[bigReward.py/smallReward.py] .`
