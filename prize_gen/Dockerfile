ARG FILE_VERSION=prize_gen1.py
FROM python:latest
COPY . .
RUN pip install flask
RUN pip install requests
ENTRYPOINT ["python", "${FILE_VERSION}"]
