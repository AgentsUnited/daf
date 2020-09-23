FROM daf:latest

FROM daf:latest

ADD ./src /app
ADD ./demo /demo
WORKDIR /app

#RUN "/bin/sh -c echo 'python3 -um internal.main & python3 -um external.main' > /app/run.sh"

#RUN echo "python3 -um internal.main & python3 -um external.main" >> /app/run.sh

RUN chmod 777 run.sh

RUN pip3 install -r requirements.txt

RUN ls -l /app
RUN cat /app/run.sh

CMD ["/bin/sh", "-c", "/app/run.sh"]
