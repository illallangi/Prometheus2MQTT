FROM python:3.8.3-alpine
LABEL maintainer="Andrew Cole <andrew.cole@illallangi.com>"

ENV MQTT_TOPIC={{sample.name}}/status/{{sample.labels.id}}
ENV METRICS_ENDPOINT=http://localhost:9330/metrics

RUN pip install \
  jinja2 \
  paho-mqtt \
  prometheus_client \
  requests

ADD . /src/

WORKDIR /src
CMD /src/app.py
