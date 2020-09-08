FROM daf:latest

ADD ./src /app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN pip3 install git+git://github.com/arg-tech/py-aspic

CMD ["python3", "-u", "-m", "main"]
