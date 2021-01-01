import paho.mqtt.client as mqtt
import time

data = "test"

def on_message(client, userdata, message):
    global data
    data = message.payload.decode('utf-8')
    print(data)
    #time.sleep(2)
    
client = mqtt.Client("Flight-Controller")
broker = 'broker.hivemq.com'
client.connect(broker, 1883, 8000)
#client.publish('Pi', "Location Reached", qos = 2)
client.loop()
client.subscribe('FC', qos = 2)
client.publish('Pi', "Location Reached", qos = 1)

while(1):
    #print("started")
    if data == "Measurement Done":
        break    
    
    #time.sleep(10)
    client.on_message = on_message
    client.loop_forever()
    
    
print("Finished")