import src.config as config

def controller(androidId):
    data = config.sensorDeviceDict[androidId].data.copy()
    config.sensorDeviceDict[androidId].data.clear()
    data.sort(key=lambda x: x[0])
    sound = ""
    for item in data:
        sound = sound + item[1] 
    print(sound)