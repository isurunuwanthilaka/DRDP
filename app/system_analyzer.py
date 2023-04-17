import psutil

kb = float(1024)
mb = float(kb ** 2)
gb = float(kb ** 3)

memTotal = int(psutil.virtual_memory()[0]/gb)
memFree = int(psutil.virtual_memory()[1]/gb)
memUsed = int(psutil.virtual_memory()[3]/gb)
memPercent = int(memUsed/memTotal*100)
storageTotal = int(psutil.disk_usage('/')[0]/gb)
storageUsed = int(psutil.disk_usage('/')[1]/gb)
storageFree = int(psutil.disk_usage('/')[2]/gb)
storagePercent = int(storageUsed/storageTotal*100)


class Analyzer:

    # device parameter extraction module

    @staticmethod
    def getRamTotal():
        return memTotal

    @staticmethod
    def getRamFree():
        return memFree

    @staticmethod
    def getRamUsed():
        return memUsed

    @staticmethod
    def getRamPercentUsage():
        return memPercent

    @staticmethod
    def getRunningPIDCount():
        return len(psutil.pids())

    @staticmethod
    def getStorageTotal():
        return storageTotal

    @staticmethod
    def getStorageFree():
        return storageFree

    @staticmethod
    def getStorageUsed():
        return storageUsed

    @staticmethod
    def getStoragePercentUsage():
        return storagePercent
