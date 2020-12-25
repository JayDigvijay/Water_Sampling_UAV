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
broker = '15.206.122.229'
client.connect(broker)

client.subscribe('FC', qos = 2)

while(1):
    #print("started")
    if data == "Done":
        break    
    client.publish('Pi', "Location Reached", qos = 2)
    client.on_message = on_message
    client.loop()
    
    
print("Finished")