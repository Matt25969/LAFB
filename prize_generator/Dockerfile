ARG REWARD=smallReward.py

# python base image
FROM python:alpine

# install flask to the container (flask app)
RUN pip install flask

# copy the specified prize .py file to run the prize generator
COPY ./${REWARD} /app.py

# communication over port 9000
EXPOSE 9000

# run the application
ENTRYPOINT ["python", "app.py"]
