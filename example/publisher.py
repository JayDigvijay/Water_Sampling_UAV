#!/usr/bin/env python3

import paho.mqtt.client as mqtt

# This is the Publisher

client = mqtt.Client()
client.connect("broker.hivemq.com",8000)
client.publish("rpi_data", "Hello")
client.disconnect()

import paho.mqtt.client as paho
import time

def on_publish(client, userdata, mid):
    print("Published Message")
 
client = paho.Client()
client.on_publish = on_publish
client.connect("broker.hivemq.com", 1883)
client.loop_start()

while True:
    client.publish("rpi_data", "Hello" , qos=1)
    time.sleep(5)