"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
import paho.mqtt.client as mqtt



def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("mousemovement")
        display.show(Image.YES)

def on_message(client, userdata, msg):
    
    if msg.payload.decode() == 'N':
        display.show(Image.ARROW_N)
    if msg.payload.decode() == 'S':
        display.show(Image.ARROW_S)
    if msg.payload.decode() == 'W':
        display.show(Image.ARROW_W)
    if msg.payload.decode() == 'E':
        display.show(Image.ARROW_E)
    if msg.payload.decode() == 'SE':
        display.show(Image.ARROW_SE)
    if msg.payload.decode() == 'SW':
        display.show(Image.ARROW_SW)
    if msg.payload.decode() == 'NW':
        display.show(Image.ARROW_NW)  
    if msg.payload.decode() == 'NE':
        display.show(Image.ARROW_NE)
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt