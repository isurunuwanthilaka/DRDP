import paho.mqtt.client as mqtt
import json
import time
# Import the required classes
from system_analyzer import Analyzer
from data_cleaner import DataCleaner
from data_enricher import DataEnricher
from algorithms import Algorithms
from pipeline import DataPipeline

# Initialize the global buffer
buffer = []
b = time.time()


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("/data/soap")


def on_message(client, userdata, msg):
    # Decode the message payload and load it into a Python dictionary
    s = time.time()
    global b
    try:
        message = msg.payload.decode("utf-8")
        json_data = json.loads(message)

        # Extract the soap data from the message and store it in a list
        soap_data = json_data

        # Initialize the required objects for the data pipeline
        analyzer = Analyzer()
        data_cleaner = DataCleaner()
        data_enricher = DataEnricher()
        algorithms = Algorithms()
        data_pipeline = DataPipeline(analyzer, data_cleaner, data_enricher)

        # Process the soap data using the data pipeline
        result = data_pipeline.process_data(soap_data)
        print(f"Pipeline Result: {result}")
        print(f"Pipeline Result T: {time.time()-s}")

        # Add the result to the buffer
        buffer.append(result)

        # Check if the buffer has enough items to be processed by the algorithms module
        if len(buffer) >= 10:
            # Analyze system resources
            available_memory, cpu_usage, available_disk_space, gpu_usage = analyzer.analyze_resources()

            # Determine which algorithm to use based on system resources
            if cpu_usage > 80 or gpu_usage > 80:
                algorithm_result = algorithms.complex_algorithm(buffer)
            else:
                algorithm_result = algorithms.simple_algorithm(buffer)

            # Print the algorithm result
            print(f"Algorithm Result: {algorithm_result}")
            print(f"Algorithm Result T: {time.time() - b }")
            b = time.time()

            # Clear the buffer
            buffer.clear()

    except UnicodeDecodeError as e:
        print(f"Error decoding message payload: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")
    except Exception as e:
        print(f"Error processing message: {e}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 3600)

client.loop_forever()
