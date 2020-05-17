"""This script is an example of subscriber to CloudMQTT Broker"""

from urllib.parse import urlparse
import os
import paho.mqtt.client as paho

# Define event callbacks
def on_connect(mosq, obj, rc):
    print('Reconnect: {}'.format(str(rc)))

def on_message(mosq, obj, msg):
    # message = str(msg.payload)
    print('Topic: {}/{}'.format(msg.topic, msg.payload.decode('utf-8')))

def on_subscribe(mosq, obj, mid, granted_qos):
    print('Subscribed: {}, QoS: {}'.format(str(mid), str(granted_qos)))

def on_log(mosq, obj, level, string):
    print(string)

#username = 'test'
#password = '123'
host_url = 'mqtt.eclipse.org'
host_port = 8000 # do not type string, but change to integer

paho = mqtt.Mosquitto()
# Assign event callbacks
paho.on_message = on_message
paho.on_connect = on_connect
paho.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get('CLOUDMQTT_URL', host_url)
url = urlparse(url_str)

# Connect
#username = 'test'
#password = '123'
#paho.username_pw_set(username, password)
paho.connect(url.hostname, url.port)

# Subscribe to a topic
paho.subscribe('myhome/+/kitchen', 0)

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = paho.loop()
print('Reconnect: ' + str(rc))