FROM python
ARG FILE_VERSION=1
COPY . .
COPY prize_gen${FILE_VERSION}.py app.py
RUN pip install flask
RUN pip install requests
ENTRYPOINT ["python", "app.py"]
