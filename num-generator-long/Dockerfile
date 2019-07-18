FROM python:2.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 50002
ENTRYPOINT ["python"]
CMD ["app.py"]
