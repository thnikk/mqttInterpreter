import paho.mqtt.client as mqtt

modes = 2 - 1

lCount = 0
sCount = 0
dCount = 0
mode = 0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global lCount
    if msg.topic == "feeds/light":
        if msg.payload != 'TOGGLE':
            lCount = int(msg.payload)
        if msg.payload == 'TOGGLE':
            if msg.topic == "feeds/light":
                if lCount == 0:
                    lCount = 1
                    print("Light on!")
                elif lCount == 1:
                    lCount = 0
                    print("Light off!")
                client.publish(msg.topic, lCount)

    global sCount
    if msg.topic == "feeds/shelf":
        if msg.payload != 'TOGGLE':
            sCount = int(msg.payload)
        if msg.payload == 'TOGGLE':
            if msg.topic == "feeds/shelf":
                if sCount == 0:
                    sCount = 1
                    print("Shelf on!")
                elif sCount == 1:
                    sCount = 0
                    print("Shelf off!")
                client.publish(msg.topic, sCount)

    global dCount
    if msg.topic == "feeds/desk":
        if msg.payload != 'TOGGLE':
            dCount = int(msg.payload)
        if msg.payload == 'TOGGLE':
            if msg.topic == "feeds/desk":
                if dCount == 0:
                    dCount = 1
                    print("desk on!")
                elif dCount == 1:
                    dCount = 0
                    print("desk off!")
                client.publish(msg.topic, dCount)

    global mode
    global modes
    if msg.topic == "feeds/mode":
        if msg.payload != 'CYCLE':
            mode = int(msg.payload)
        if msg.payload == 'CYCLE':
            if msg.topic == "feeds/mode":
                mode+=1
                if mode > modes:
                    mode = 0;
                print("Mode = {0}".format(mode))
                client.publish(msg.topic, mode)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.0.0.20")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
