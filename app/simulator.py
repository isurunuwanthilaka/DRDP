import paho.mqtt.client as mqtt
import time
import random
import datetime
import json

# Set up MQTT broker connection
broker = "localhost"
port = 1883
client = mqtt.Client("admin")

try:
    client.connect(broker, port)
except ConnectionError:
    print("Failed to connect to MQTT broker")

# Define list of device IDs and sensor readings
device_ids = ["C001", "C002", "C003", "C004"]
producers = ["isuru", "isuru@mrt.com", "0775556667", "the isu@gmail.com"]

# Set up simulation parameters
start_time = time.time()
sequence_id = 0
limit = 100000
print(datetime.datetime.now())
print("Running...")

# Simulate soap counting messages
for i in range(limit):
    # Choose a random device and increment the sequence ID
    device_id = device_ids[random.randint(0, 3)]
    sequence_id += 1

    # Choose a random sensor reading
    sensor_reading = random.randint(0, 2)

    # Choose a random device and increment the sequence ID
    producer = producers[random.randint(0, 3)]
    sequence_id += 1

    # Construct message and publish to MQTT broker
    data = {
        "device_id": device_id,
        "sequence_id": sequence_id,
        "sensor_reading": sensor_reading,
        "producer": producer
    }

    # Convert the dictionary to a JSON string
    message = json.dumps(data)

    client.publish("/data/soap", message)

    # Print message for debugging purposes
    print(message)

    # Pause for 0.2 seconds between messages
    time.sleep(0.2)

# Calculate simulation statistics
end_time = time.time()
print("Stopped...")
print(datetime.datetime.now())
print("Avg Rate : "+str(limit/(end_time-start_time)))
print("time taken : " + str(end_time-start_time))
