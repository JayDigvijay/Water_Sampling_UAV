import paho.mqtt.client as mqtt
import time

data = "test"
status = "Ongoing"

def on_message(client, userdata, message):
    global status
    data = message.payload.decode('utf-8')
    print(data)
    if data == "Measurement Done":
        status = "Finished"
        
    #time.sleep(2)

def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	client.subscribe("FC")

  
client = mqtt.Client("Flight-Controller")
broker = 'broker.hivemq.com'
client.connect(broker, 1883, 8000)
client.on_connect = on_connect

client.publish('Pi', "Location Reached", qos = 1)


#time.sleep(10)
client.on_message = on_message
while status == "Ongoing":
    client.loop()
    
print(status)   
