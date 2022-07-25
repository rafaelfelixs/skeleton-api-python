FROM python:3.8-slim

RUN apt-get update \
 && apt-get install -y gcc python3-dev python3-mysqldb \
 && apt-get clean \

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app .

EXPOSE 8000