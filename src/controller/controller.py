import src.config as config

def controller(androidId):
    data = config.sensorDeviceDict[androidId].data
    data.sort(key=lambda x: x[0])
    print(data)