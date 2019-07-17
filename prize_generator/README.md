# Prize Generator

bigReward.py is the more generous prize generator which provides bigger rewards (50% of £50)

smallReward.py is the less generous prize generator which provides smaller rewards (25% of £10)

default = bigReward.py 

Building the image

`docker build --tag prize --no-cache --build-arg REWARD=[bigReward.py/smallReward.py] .`
