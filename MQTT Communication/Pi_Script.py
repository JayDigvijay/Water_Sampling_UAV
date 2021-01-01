import paho.mqtt.client as mqtt
import time

data = "test"
status = "Ongoing"

def on_message(client, userdata, message):
    global status
    data = message.payload.decode('utf-8')
    print(data)
    if data == "Location Reached":
        take_sample()
        take_readings()
        client.publish('FC', "Measurement Done", qos = 1)
        time.sleep(2)
        status = "Finished"

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("Pi")
   
client = mqtt.Client("Pi")
broker = 'broker.hivemq.com'
client.connect(broker)

def take_sample():
    time.sleep(2)
    print("Sample Collected")
def take_readings():
    time.sleep(2)
    print("Readings taken")

client.on_connect = on_connect
client.on_message = on_message
while status == "Ongoing":
    client.loop()  

print(status)
    
    
