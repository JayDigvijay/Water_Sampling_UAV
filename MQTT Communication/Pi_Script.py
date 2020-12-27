import paho.mqtt.client as mqtt
import time
import json
data = "test"
data2 = "test"

def on_message(client, userdata, message):
    global data
    data = message.payload.decode('utf-8')
    print(data)
    #time.sleep(2)
    
client = mqtt.Client("Flight-Controller")
broker = '13.232.250.241'
client.connect(broker)

client.subscribe('Pi', qos = 2)

def take_sample():
    time.sleep(2)
    print("Sample Collected")
def take_readings():
    time.sleep(2)
    print("Readings taken")

while(1):
    if data == "Location Reached" and data2 == "test":
        data2 = data
        take_sample()
        take_readings()
        client.publish('FC', "Measurement Done", qos = 1)
        client.loop(3)
        client.on_message = on_message
        break
    client.on_message = on_message
    client.loop(0.1)    

    
    
