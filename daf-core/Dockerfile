FROM docker/compose

ADD . /daf
WORKDIR /daf
RUN mv demo modules/daf-controller2/

ARG demo=False
ARG activemq=activemq-external

# build the run file
RUN echo -e "#!/bin/sh\n\ndocker build -t daf:latest modules/daf-module/\n\n docker-compose up --build" >> run-daf.sh && \
    chmod 777 run-daf.sh

RUN echo -e "DEMO=$demo\nactivemq=$activemq" >> daf-config.env

CMD ["./run-daf.sh"]
