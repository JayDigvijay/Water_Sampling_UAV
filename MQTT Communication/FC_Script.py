import paho.mqtt.client as mqtt
import time
import json
data = "test"

def on_message(client, userdata, message):
    global data
    data = message.payload.decode('utf-8')
    print(data)
    #time.sleep(2)
    
client = mqtt.Client("Flight-Controller")
broker = '13.232.250.241'
client.connect(broker)
#client.publish('Pi', "Location Reached", qos = 2)
client.loop()
client.subscribe('FC', qos = 2)

while(1):
    #print("started")
    if data == "Measurement Done":
        break    
    client.publish('Pi', "Location Reached", qos = 2)
    time.sleep(3)
    client.on_message = on_message
    client.loop()
    
    
print("Finished")