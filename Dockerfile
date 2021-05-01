FROM python:3.8
FROM tiangolo/meinheld-gunicorn:python3.8
LABEL maintainer "Shaleen"

USER root

WORKDIR /app

COPY requirements.txt /
RUN pip install --trusted-host pypi.python.org -r /requirements.txt


COPY ./ ./
EXPOSE 8050

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["gunicorn"  , "-k", "geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "-w", "1", "-b", "0.0.0.0:6007", "main"]
