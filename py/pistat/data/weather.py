
"""
weather.py acts as an adapter class for different weather APIs.
"""
class Weather(object):
	# Outdoor wather
	outdoorTemperature = 0
	outdoorHumidity = 0
	outdoorData = {}

	def __init__(self):
		pass

	def pollWeather(self):
		pass

	# Returns a dictionary with all data
	def getWeatherData(self):
		return self.outdoorData

	def getOutdoorTemperature(self):
		return self.outdoorTemperature

	def getOutdoorHumidity(self):
		return self.outdoorHumidity