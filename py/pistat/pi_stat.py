#!/usr/bin/env python

import threading
from data.dht import DHT
from data.wunderground import WeatherUnderground
from tstat.thermostat import Thermostat
from hist.history import History

class PiStat(object):

    def __init__(self):
        # Time intervals for various functions in seconds
        self.sensorPollInterval = 5
        self.weatherPollInterval = 300
        self.historyUpdateInterval = 600

        # Objects
        self.sensor = DHT()
        self.weather = WeatherUnderground()
        self.history = History(self.sensor, self.weather)
        self.tstat = Thermostat(self.sensor, self.weather)

        # start calling updateWeatherData now and every 300 sec thereafter
        self.updateWeatherData()

        # start calling updateSensorData now and every 5 sec thereafter
        self.updateSensorData()

        # start calling updateHistoryData now and every 600sec thereafter
        self.updateHistoryData()


    """
    Poll the sensor for temperature and humidity readings every five seconds, then
    update the Sensor object with the most recent readings.
    """
    def updateSensorData(self):
        # Poll the sensor to grab updated readings
        self.sensor.pollSensor()
        #print "Indoor - Temperature: " + str(self.sensor.getIndoorTemperature()) + " | Humidity: " + str(self.sensor.getIndoorHumidity())

        self.tstat.control()

        # call pollSensor() again in 'sensorPollInterval' seconds
        threading.Timer(self.sensorPollInterval, self.updateSensorData).start()

    """
    Polls Underground Weather for the current conditions. City, State is determined
    in weather_poller.py with the json link.
    """
    def updateWeatherData(self):
        self.weather.pollWeather()

        #print "Updating weather..."
        #print "Outdoor - Temperature: " + str(self.weather.getOutdoorTemperature()) + " | Humidity " + str(self.weather.getOutdoorHumidity())

        # call pollWeather() again in 'weatherPollInterval' seconds
        threading.Timer(self.weatherPollInterval, self.updateWeatherData).start()

    def updateHistoryData(self):
        self.history.getHistoryData()
        self.history.writeHistoryData()

        threading.Timer(self.historyUpdateInterval, self.updateHistoryData).start()

# Start the script
pistat = PiStat()
