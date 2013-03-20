import json
import urllib2
from .weather import Weather

class WeatherUnderground(Weather):

	# Default values
	defaultCity = "Indianapolis"
	defaultState = "IN"

	# API Key
	apiKey = "3dcd75dc0e162700"

	"""
	Setup the json link with city and state.
	"""
	def __init__(self, city = None, state = None):
		if city == None or state == None:
			self.city = self.defaultCity
			self.state = self.defaultState
		else:
			self.city = city
			self.state = state

		self.jsonLink = "http://api.wunderground.com/api/" + self.apiKey + "/conditions/q/" + self.state + "/" + self.city + ".json"

	"""
	Requests the json object from weather underground, reads the response, then copies the data.
	"""
	def pollWeather(self):
		# Get the json object
		response = urllib2.urlopen(self.jsonLink)

		# Read the json object
		jsonData = response.read()

		# Convert json to python dictionary and update temp/humidity
		if jsonData:
			Weather.outdoorData = json.loads(jsonData)
			Weather.outdoorTemperature = Weather.outdoorData['current_observation']['temp_f']
			Weather.outdoorHumidity = Weather.outdoorData['current_observation']['relative_humidity']