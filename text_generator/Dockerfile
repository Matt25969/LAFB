ARG APP_VERSION=3char

# python base image
FROM python:alpine

# install flask to the container (flask app)
RUN pip install flask
 
# copy the required files to run the notification server
COPY ./${APP_VERSION}.py /app.py

# communication over port 9000
EXPOSE 9000

# run the application
ENTRYPOINT ["python3", "app.py"]
