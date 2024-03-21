FROM ubuntu:22.04

ENV REFRESHED_AT 2024-03-22
ENV LANG en_US.UTF-8
ENV PYTHONUNBUFFERED 1

RUN apt-get update -qq
RUN apt-get install locales && locale-gen en_US.UTF-8
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip build-essential python3-dev \
    libxml2-dev libxslt1-dev libssl-dev libffi-dev vim git wget libpq-dev

RUN echo 'alias pm="python3 manage.py"' >> ~/.bashrc

WORKDIR /app
COPY requirements/ /app/requirements/
RUN pip3 install -r /app/requirements/production.txt
COPY . /app

EXPOSE 8000

RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
