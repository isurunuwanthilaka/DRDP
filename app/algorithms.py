import time


class Algorithms:
    def __init__(self):
        pass

    def simple_algorithm(self, data):
        """
        A simple algorithm that consumes low resources.

        Parameters:
            data (list): A list of integers.

        Returns:
            The sum of the integers in the input list.
        """
        result = sum(data)
        return result

    def complex_algorithm(self, data):
        """
        A complex algorithm that creates high resource usage.

        Parameters:
            data (list): A list of integers.

        Returns:
            The sum of the squared integers in the input list.
        """
        result = sum([x**2 for x in data])
        return result
