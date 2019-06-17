FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN sed -i '/jessie-updates/d' /etc/apt/sources.list
RUN apt-get update && apt-get -y install poppler-utils python-poppler vim

# # 起動時用スクリプト
COPY run.sh /run.sh

ADD . /app/