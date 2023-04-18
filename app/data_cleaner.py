import re
import time
from nltk.stem import PorterStemmer


class DataCleaner:
  
    def __init__(self):
        self.stop_words = set(["the", "and", "in", "is", "it"])

    def clean_data_simple(self, data):
        """
        Cleans and processes data received from an MQTT subscription using a simple method.

        Parameters:
            data (str): The raw data received from the MQTT subscription.

        Returns:
            A list of strings containing the cleaned and processed data.
        """
        # Remove all non-alphanumeric characters and convert to lowercase
        cleaned_data = re.sub('[^0-9a-zA-Z]+', '-', data).lower()

        return cleaned_data

    def clean_data_advanced(self, data):
        """
        A more resource-intensive method for cleaning and processing data received from an MQTT subscription.

        Parameters:
            data (str): The raw data received from the MQTT subscription.

        Returns:
            A list of strings containing the cleaned and processed data.
        """
        # Remove all non-alphanumeric characters and convert to uppercase

        cleaned_data = re.sub('[^0-9a-zA-Z@.]+', '-', data).upper()
        time.sleep(0.001)

        return cleaned_data
