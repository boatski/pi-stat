import json
from sensor_poller import SensorPoller
from weather_poller import WeatherPoller

class Sensor(object):
	indoorTemperature = 0
	indoorHumidity = 0

	outdoorTemperature = 0
	outdoorHumidity = 0

	
	def __init__(self):
		self.sensor = SensorPoller()
		self.weather = WeatherPoller()

		self.pollSensor()
		self.pollWeather()
		self.buildJSON()

	"""
	Calls the SensorPoller to poll the sensor and update the dictionary with new
	temperature and humidity values.
	"""
	def pollSensor(self):
		self.sensor.updateSensorData()
		self.data = self.sensor.getSensorData()
		
		"""
		If the dictionary returned from the SensorPoller is empty, then
		do not update the temperature/humidity.
		"""
		if self.data:
			self.indoorTemperature = self.data['Temp']
			self.indoorHumidity = self.data['Hum']

	def pollWeather(self):
		self.jsonWeather = self.weather.pollWeather()

	"""
	Builds the data into a json object.
	"""
	def buildJSON(self):
		hum = str(self.indoorHumidity) + '%'
		jsonSensor = {'indoorTemperature':self.indoorTemperature, 'indoorHumidity':hum}

		jsonCombined = {'sensor':jsonSensor, 'weather':self.jsonWeather}

		# Return a json object string to php
		print json.dumps(jsonCombined)

sensor = Sensor()
