FROM ubuntu:20.04

RUN apt-get update -qq

RUN apt-get install locales && locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip build-essential python3-dev \
    libmysqlclient-dev libxml2-dev libxslt1-dev libssl-dev libffi-dev vim

RUN mkdir /logs
ENV LOG_DIR /logs
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY . /app

EXPOSE 8000

RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
