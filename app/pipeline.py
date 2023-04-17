import time

from system_analyzer import Analyzer
from data_cleaner import DataCleaner
from data_enricher import DataEnricher
from algorithms import Algorithms


class DataPipeline:
    def __init__(self, analyzer: Analyzer, data_cleaner: DataCleaner, data_enricher: DataEnricher, algorithms: Algorithms):
        self.analyzer = analyzer
        self.data_cleaner = data_cleaner
        self.data_enricher = data_enricher
        self.algorithms = algorithms

    def process_data(self, data):
        # Analyze system resources
        available_memory, cpu_usage, available_disk_space, gpu_usage = self.analyzer.analyze_resources()

        # Determine which cleaning method to use based on system resources
        if available_memory < 500:
            cleaned_data = self.data_cleaner.clean_data_advanced(data)
        else:
            cleaned_data = self.data_cleaner.clean_data(data)

        # Enrich the data
        if available_memory < 500:
            enriched_data = self.data_enricher.enrich_data_simple(cleaned_data)
        else:
            enriched_data = self.data_enricher.enrich_data_hard(cleaned_data)

        # Determine which algorithm to use based on system resources
        if cpu_usage > 80 or gpu_usage > 80:
            result = self.algorithms.complex_algorithm(enriched_data)
        else:
            result = self.algorithms.simple_algorithm(enriched_data)

        # Return the result
        return result
