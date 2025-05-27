import paho.mqtt.client as mqtt
import requests
from config import BROKER_IP, TOPIC

'''
Implement you're own server/host to use this feature
'''
#PI_IP = f"http://{BROKER_IP}:5000"
'''
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.connect(BROKER_IP, 1883, 60)
client.loop_start()

def publish(*args, **kwargs) -> None:
    client.publish(TOPIC, *args, **kwargs)
'''
def publish(*args, **kwargs):
    pass
'''def send_http(msg: str):
    #response = requests.get(f"{PI_IP}/{msg}")
    #print("Flask Output: ", response.text)
    #return response
    return None'''