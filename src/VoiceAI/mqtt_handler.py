import paho.mqtt.client as mqtt
from config import BROKER_IP, TOPIC

'''
Implement you're own server/host to use this feature
'''

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(BROKER_IP, 1883, 60)
client.loop_start()

def publish(*args, **kwargs) -> None:
    client.publish(TOPIC, *args, **kwargs)