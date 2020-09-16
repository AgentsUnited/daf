FROM daf:latest

FROM daf:latest

ADD ./src /app
WORKDIR /app
RUN chmod 777 run.sh

RUN pip3 install -r requirements.txt


CMD ["/bin/sh", "-c", "/app/run.sh"]
