FROM phusion/baseimage:latest

RUN apt-get update && apt-get install -y python3 python3-pip

ADD ./app /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "-u", "main.py"]
