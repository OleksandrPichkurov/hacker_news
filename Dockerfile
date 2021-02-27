FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/hacker_news

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /usr/src/hacker_news

ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /usr/src/hacker_news/docker-entrypoint.sh
ENTRYPOINT [ "/usr/src/hacker_news/docker-entrypoint.sh" ]