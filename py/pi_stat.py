import threading
from sensor import Sensor
from thermostat import Thermostat
from output_handler import OutputHandler

class PiStat(object):

    def __init__(self):
        # Time intervals for various functions in seconds
        self.sensorPollInterval = 5
        self.weatherPollInterval = 300

        # Objects
        self.sensor = Sensor()
        self.tstat = Thermostat(self.sensor)

        # start calling pollWeather now and every 300 sec thereafter
        self.pollWeather()

        # start calling pollSensor now and every 5 sec thereafter
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
    Polls Underground Weather for the current conditions. City, State is determined
    in weather_poller.py with the json link.
    """
    def pollWeather(self):
        self.sensor.pollWeather()

        # call pollWeather() again in 'weatherPollInterval' seconds
        threading.Timer(self.weatherPollInterval, self.pollWeather).start()


# Start the script
pistat = PiStat()
