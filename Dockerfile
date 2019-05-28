FROM python:3.6.8-alpine

EXPOSE 80

WORKDIR /app

ADD . /app

RUN apk add gcc musl-dev 

RUN pip install pipenv && pipenv install

ENTRYPOINT ./docker-entrypoint.sh

CMD /bin/sh
