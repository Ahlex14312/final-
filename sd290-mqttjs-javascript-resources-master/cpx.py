from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        cp.red_led = True
        client.subscribe("switch/#")

def on_message(client, userdata, msg):
    if msg.topic="switch/switch0":
        if msg.payload.decode() == "true":
            cp.pixels[0] = (255, 255, 255)
        else:
            cp.pixels[0] = (0, 0, 0)
    elif msg.topic="switch/switch1":
        if msg.payload.decode() == "true":
            cp.pixels[1] = (255, 255, 255)
        else:
            cp.pixels[1] = (0, 0, 0)
    elif msg.topic="switch/switch2":
        if msg.payload.decode() == "true":
            cp.pixels[2] = (255, 255, 255)
        else:
            cp.pixels[2] = (0, 0, 0)
cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.mosquitto.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt