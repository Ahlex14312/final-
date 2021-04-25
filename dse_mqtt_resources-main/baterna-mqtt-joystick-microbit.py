from microbit import *
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0: #if rc is equal to 0
        client.subscribe('joystick') #client.subscribe topic of joystick
        display.show(Image.YES) #show image yes / check
    else:
        display.show(Image.NO) #show Image.NO

def on_message(client, userdata, msg):
    print(msg.payload.decode()) #print the the message payload decode check if it run(para mahibal an)
    if msg.payload.decode() == "C": #if msg.payload.decode() is equal to C (North)
        display.clear()#clear all the lights 
    elif msg.payload.decode() == "N":#if msg.payload.decode() is equal to N (North)
        display.show(Image.ARROW_N) #display image arrow north
    elif msg.payload.decode() == "S":#if msg.payload.decode() is equal to S (South)
        display.show(Image.ARROW_S)#display image arrow south
    elif msg.payload.decode() == "E":#if msg.payload.decode() is equal to E (East)
        display.show(Image.ARROW_E)#display image arrow east
    elif msg.payload.decode() == "W":#if msg.payload.decode() is equal to W (West)
        display.show(Image.ARROW_W) #display image arrow west
    elif msg.payload.decode() == "NE":#if msg.payload.decode() is equal to NE (Northeast)
        display.show(Image.ARROW_NE)#display image arrow northeast
    elif msg.payload.decode() == "NW":#if msg.payload.decode() is equal to NW (Northwest)
        display.show(Image.ARROW_NW)#display image arrow northwest
    elif msg.payload.decode() == "SE":#if msg.payload.decode() is equal to SE (Southeast)
        display.show(Image.ARROW_SE)#display image arrow southeast
    elif msg.payload.decode() == "SW":#if msg.payload.decode() is equal to SW (Southwest)
        display.show(Image.ARROW_SW)#display image arrow southwest


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60) #client connect to a broker

client.loop_forever()
