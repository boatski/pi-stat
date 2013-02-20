import threading
import atexit
from Sensor import Sensor
from Thermostat import Thermostat

class PiStat(object):

    prevTemperature = 0
    curTemperature = 0
    curHumidity = 0

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

        # Get the sensor readings
        self.data = self.sensor.getSensorData()
	
	if self.data != None:
        	self.curTemperature = self.data['Temp']
        	self.curHumidity = self.data['Hum']

        if self.curTemperature != self.prevTemperature:
            self.prevTemperature = self.curTemperature

            print "Temp: " + str(self.sensor.getTemperature()) + "\nHumidity: " + str(self.sensor.getHumidity())
            self.tstat.control()
        else:
            print "Same temperature."

        # call pollSensor() again in 'sensorPollInterval' seconds
        threading.Timer(self.sensorPollInterval, self.pollSensor).start()


    """
    Ensure that all three outputs are off if the program is ended or if it crashes.
    """
    def exitCleanup(self):
        print 'My application is ending!'


# Start the script
pistat = PiStat()
