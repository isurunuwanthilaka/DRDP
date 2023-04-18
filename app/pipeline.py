import time

from system_analyzer import Analyzer
from data_cleaner import DataCleaner
from data_enricher import DataEnricher


class DataPipeline:
    def __init__(self, analyzer: Analyzer, data_cleaner: DataCleaner, data_enricher: DataEnricher):
        self.analyzer = analyzer
        self.data_cleaner = data_cleaner
        self.data_enricher = data_enricher

    def process_data(self, data):
        # Analyze system resources
        available_memory, cpu_usage, available_disk_space, gpu_usage = self.analyzer.analyze_resources()

        # Determine which cleaning method to use based on system resources
        if available_memory < 500:
            data['producer'] = self.data_cleaner.clean_data_advanced(
                data['producer'])
        else:
            data['producer'] = self.data_cleaner.clean_data_simple(
                data['producer'])

        # Enrich the data
        if available_memory < 500:
            data['producer'] = self.data_enricher.enrich_data_simple(
                data['producer'])
        else:
            data['producer'] = self.data_enricher.enrich_data_hard(
                data['producer'])

        # Return the result
        return data
