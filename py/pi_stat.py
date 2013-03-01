import threading
import atexit
from sensor import Sensor
from thermostat import Thermostat
from output_handler import OutputHandler

class PiStat(object):

    def __init__(self):
        # Time intervals for various functions in seconds
        self.sensorPollInterval = 5

        # Objects
        self.sensor = Sensor()
        self.tstat = Thermostat(self.sensor)

        # Call exitCleanup() when the program is ended or if it crashes
        atexit.register(self.exitCleanup)
        
        # start calling f now and every 60 sec thereafter
        self.pollSensor()


    """
    Poll the sensor for temperature and humidity readings every five seconds, then
    update the Sensor object with the most recent readings.
    """
    def pollSensor(self):
        # Poll the sensor to grab updated readings
        self.sensor.pollSensor()

        self.tstat.control()

        # call pollSensor() again in 'sensorPollInterval' seconds
        threading.Timer(self.sensorPollInterval, self.pollSensor).start()


    """
    Ensure that all three outputs are off when the program is ended or if it crashes.
    """
    def exitCleanup(self):
        print 'Shutting down...\nDisabling all outputs...'
        output = OutputHandler()
        output.disableAllOutputs()


# Start the script
pistat = PiStat()
