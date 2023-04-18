import psutil
import pynvml


class Analyzer:

    def __init__(self):
        self.kb = float(1024)
        self.mb = float(self.kb ** 2)
        self.gb = float(self.kb ** 3)
        # Initialize pynvml
        # pynvml.nvmlInit()

    # Retrieve system resource information
    def analyze_resources(self):
        # Get available memory in GB
        available_memory = self.getRamFree()

        # Get CPU usage percentage
        cpu_usage = self.getCpuUsage()

        # Get available disk space in GB
        available_disk_space = self.getStorageFree()

        # Get GPU usage percentage (assuming a single GPU)
        gpu_usage = self.getGpuUsage()

        return available_memory, cpu_usage, available_disk_space, gpu_usage

    # Device parameter extraction methods
    def getRamTotal(self):
        return int(psutil.virtual_memory()[0] / self.gb)

    def getRamFree(self):
        return int(psutil.virtual_memory()[1] / self.gb)

    def getRamUsed(self):
        return int(psutil.virtual_memory()[3] / self.gb)

    def getRamPercentUsage(self):
        return int(self.getRamUsed() / self.getRamTotal() * 100)

    def getRunningPIDCount(self):
        return len(psutil.pids())

    def getStorageTotal(self):
        return int(psutil.disk_usage('/')[0] / self.gb)

    def getStorageFree(self):
        return int(psutil.disk_usage('/')[2] / self.gb)

    def getStorageUsed(self):
        return int(psutil.disk_usage('/')[1] / self.gb)

    def getStoragePercentUsage(self):
        return int(self.getStorageUsed() / self.getStorageTotal() * 100)

    def getCpuUsage(self):
        return psutil.cpu_percent(interval=1)

    def getGpuUsage(self):
        # Assuming a single NVIDIA GPU
        # handle = pynvml.nvmlDeviceGetHandleByIndex(0)
        # info = pynvml.nvmlDeviceGetUtilizationRates(handle)
        return int(60)  # info.gpu
