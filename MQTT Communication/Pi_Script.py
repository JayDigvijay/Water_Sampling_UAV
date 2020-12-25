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
def take_sample():
    time.sleep(2)
    print("Sample Collected")
def take_readings():
    time.sleep(2)
    print("Readings taken")
      
client = mqtt.Client("Raspberry-Pi")
broker = '15.206.122.229'
client.connect(broker)

client.subscribe('FC', qos = 2)
client.subscribe('Pi', qos = 2)

while(1):
	if data == "Location Reached" and data2 != data:
		client.loop()
		data2 = data
		take_sample()
		take_readings()
        client.publish('FC', "Done", qos = 2)
		break
	client.on_message = on_message
	client.loop()    

    
    
