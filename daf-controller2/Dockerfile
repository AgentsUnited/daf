FROM daf:latest

FROM daf:latest

ADD ./src /app
WORKDIR /app
RUN chmod 777 run

RUN pip3 install -r requirements.txt

RUN ls -l /app

CMD ["/bin/sh", "-c", "/app/run"]
