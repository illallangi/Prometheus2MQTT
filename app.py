#!/usr/bin/env python

import os
import json
import sys
import time
import paho.mqtt.client as mqtt
from jinja2 import Template
from prometheus_client.parser import text_string_to_metric_families
import requests

MQTT_BROKER      = os.environ.get("MQTT_BROKER")
if (MQTT_BROKER is None):
  print("MQTT_BROKER must be set")
  sys.exit(-1)

MQTT_TOPIC       = os.environ.get("MQTT_TOPIC", "{{sample.name}}/status/{{sample.labels.id}}")
if (MQTT_TOPIC is None):
  print("MQTT_TOPIC must be set")
  sys.exit(-1)

METRICS_ENDPOINT = os.environ.get("METRICS_ENDPOINT", "http://localhost:9330/metrics")
if (METRICS_ENDPOINT is None):
  print("METRICS_ENDPOINT must be set")
  sys.exit(-1)

UPDATE_INTERVAL  = os.environ.get("UPDATE_INTERVAL", 60)
if (UPDATE_INTERVAL is None):
  print("UPDATE_INTERVAL must be set")
  sys.exit(-1)

def main(argv):
  #with open('prom.txt', 'r') as file:
  #  metrics = file.read()

  mqttc = mqtt.Client()
  mqttc.connect(MQTT_BROKER)

  starttime=time.time()
  while True:
    metrics = requests.get(METRICS_ENDPOINT).text
    for family in text_string_to_metric_families(metrics):
      for sample in family.samples:
        j = {
            'name': sample[0],
            'labels': sample[1],
            'value': sample[2],
            'timestamp': sample[3],
            'exemplar': sample[4]
          }
        topic = Template(MQTT_TOPIC).render(sample=j)
        print(topic)
        print(f"{json.dumps(j, indent=2)}")
        mqttc.publish(topic, json.dumps(j), qos=1, retain=True)
    if float(UPDATE_INTERVAL) == 0:
      break
    sleep = max(0, float(UPDATE_INTERVAL) - ((time.time() - starttime) % float(UPDATE_INTERVAL)))
    if sleep > 1:
      print('{0}    Sleeping {1:00.0f} seconds'.format(datetime.datetime.now().isoformat(), sleep), flush=True)
      time.sleep(sleep)
  mqttc.disconnect()

if __name__ == "__main__":
  main(sys.argv)