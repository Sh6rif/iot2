# Import the necessary modules
import paho.mqtt.client as mqtt
from time import sleep
import sys

# MQTT broker address
broker_ip = "192.168.137.1"

# MQTT broker port
port = 1883

# MQTT topic to which the publisher will publish messages
topic = "home/led2"

# Quality of Service (QoS)
qos = 0

# Create an MQTT client instance with the name "publisher"
client = mqtt.Client("publisherShifo")

# Connect to the MQTT broker using the specified IP address and port
client.connect(broker_ip, port)

# Infinite loop to continuously publish messages
while True:
    # Message to be published
    message = sys.argv[1] if len(sys.argv) > 1 else None

    # Publish the message to the specified topic
    client.publish(topic, message, qos)

    # Print a message indicating that the message has been published
    print("Published message:", message)

    # Wait for 2 seconds before publishing the next message
    sleep(2)

# Disconnect from the MQTT broker
client.disconnect()