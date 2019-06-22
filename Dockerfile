FROM python:3.6.8-alpine

EXPOSE 80

WORKDIR /app

RUN apk add gcc musl-dev

COPY Pipfile .

RUN pip install pipenv && pipenv install

COPY . /app

ENTRYPOINT ./docker-entrypoint.sh

CMD /bin/sh
