FROM daf:latest

ADD ./src /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "-u", "-m", "main"]
