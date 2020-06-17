FROM python:3.8.3-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    XDG_CONFIG_HOME=/config

WORKDIR /usr/src/app

ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ADD . /usr/src/app

RUN pip3 install .

ENTRYPOINT ["/usr/local/bin/prometheus2mqtt"]

ARG VCS_REF
ARG VERSION
ARG BUILD_DATE
LABEL maintainer="Andrew Cole <andrew.cole@illallangi.com>" \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.description="Acts as a bridge between Prometheus and MQTT" \
      org.label-schema.name="Prometheus2MQTT" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.url="http://github.com/illallangi/Prometheus2MQTT" \
      org.label-schema.usage="https://github.com/illallangi/Prometheus2MQTT/blob/master/README.md" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/illallangi/Prometheus2MQTT" \
      org.label-schema.vendor="Illallangi Enterprises" \
      org.label-schema.version=$VERSION
