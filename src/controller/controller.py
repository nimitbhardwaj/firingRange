import src.config as config
import array
import pyaudio

class Cont:
    def __init__(self):
        self.play = pyaudio.PyAudio()
        self.stream_play=self.play.open(format=pyaudio.paInt16,
                        channels=2,
                        rate=44100,
                        output=True)

    def controller(self, androidId):
        data = config.sensorDeviceDict[androidId].data.copy()
        config.sensorDeviceDict[androidId].data.clear()
        print(data)
        data = array.array('B', data).tostring()

        while 1:
            self.stream_play.write(data)

        self.stream_play.stop_stream()
        self.stream_play.close()
        self.play.terminate()
