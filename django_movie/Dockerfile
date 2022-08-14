FROM ubuntu:latest

RUN mkdir -p $HOME/docker/volumes/postgres
RUN sudo docker pull postgres
RUN sudo docker run --rm --name baza -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=postgres -e POSTGRES_DB=db -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres


FROM python:3.8.3

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install netcat -y
RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y
RUN pip install --upgrade pip

COPY ./req.txt .
RUN pip install -r req.txt

# COPY ./entrypoint.sh .

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]

ENTRYPOINT ["sh", "/usr/src/app/prestart.sh"]
