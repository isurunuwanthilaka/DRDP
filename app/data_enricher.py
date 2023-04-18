import re


class DataEnricher:
    def __init__(self):
        pass

    def enrich_data_simple(self, data):
        
        enriched_data = [data]

        # Check if the word is a number
        if data.isdigit():
            enriched_data.append("NUMBER")
        # Check if the word is a date
        elif re.match(r"\d{1,2}/\d{1,2}/\d{4}", data):
            enriched_data.append("DATE")
        else:
            enriched_data.append(data)
        return enriched_data

    def enrich_data_hard(self, data):
        
        enriched_data = [data]

        # Check if the word is a number
        if data.isdigit():
            enriched_data.append("NUMBER")
        # Check if the word is a date
        elif re.match(r"\d{1,2}/\d{1,2}/\d{4}", data):
            enriched_data.append("DATE")
        # Check if the word is an email
        elif re.match(r"[^@]+@[^@]+\.[^@]+", data):
            enriched_data.append("EMAIL")
        # Check if the word is a URL
        elif re.match(r"(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?", data):
            enriched_data.append("URL")
        # Check if the word is a phone number
        elif re.match(r"\d{3}-\d{3}-\d{4}", data):
            enriched_data.append("PHONE")
        else:
            enriched_data.append(data)
        return enriched_data
