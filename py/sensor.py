from sensor_poller import SensorPoller
from weather_poller import WeatherPoller

class Sensor(object):
	# Indoor weather
	indoorTemperature = 0
	indoorHumidity = 0

	# Outdoor wather
	outdoorTemperature = 0
	outdoorHumidity = 0
	
	def __init__(self):
		self.sensorPoller = SensorPoller()
		self.weatherPoller = WeatherPoller("Indianapolis", "IN")

		self.pollSensor()
		self.pollWeather()

	"""
	Calls the SensorPoller to poll the sensor and update the dictionary with new
	temperature and humidity values.
	"""
	def pollSensor(self):
		self.sensorPoller.updateSensorData()
		self.sensorData = self.sensorPoller.getSensorData()
		
		"""
		If the dictionary returned from the SensorPoller is empty, then
		do not update the temperature/humidity.
		"""
		if self.sensorData:
			self.indoorTemperature = self.sensorData['Temp']
			self.indoorHumidity = self.sensorData['Hum']

	"""
	Calls the WeatherPoller to get the json object from Weather Underground
	with current outdoor weather conditions and update the outdoor
	temperature/humidity values.
	"""
	def pollWeather(self):
		self.weatherPoller.updateWeatherData()
		self.weatherData = self.weatherPoller.getWeatherData()

		"""
		If the dictionary returned from the WeatherPoller is empty, then
		do not update the temperature/humidity.
		"""
		if self.weatherData:
			self.outdoorTemperature = self.weatherData['current_observation']['temp_f']
			self.outdoorHumidity = self.weatherData['current_observation']['relative_humidity']

	# Returns a dictionary with both readings
	def getSensorData(self):
		return self.sensorData

	def getWeatherData(self):
		return self.weatherData

	def getTemperature(self):
		return self.indoorTemperature

	def getOutdoorTemperature(self):
		return self.outdoorHumidity

	def getHumidity(self):
		return self.indoorHumidity

	def getOutdoorHumidity(self):
		return self.outdoorHumidity
