import paho.mqtt.client as mqtt
import time
import random
import datetime

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
sensor_readings = {
    1: "T",
    2: "T",
    3: "F",
    4: "F",
    5: "T",
    6: "F",
    7: "T"
}

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
    sensor_id = random.randint(1, 7)
    sensor_reading = sensor_readings[sensor_id]

    # Construct message and publish to MQTT broker
    message = f"{device_id},{sequence_id},{sensor_reading},1"
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
