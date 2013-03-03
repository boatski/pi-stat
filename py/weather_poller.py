import json
import urllib2

class WeatherPoller(object):

	def __init__(self, city, state):
		self.city = city
		self.state = state
		self.jsonLink = 'http://api.wunderground.com/api/3dcd75dc0e162700/conditions/q/' + self.state + '/' + self.city + '.json'

	"""
	Requests the json object from weather underground, reads the response, then returns the json string.
	"""
	def updateWeather(self):
		response = urllib2.urlopen(self.jsonLink)
		jsonData = response.read()
		self.data = json.loads(jsonData)
		print "Updating weather..."

	def getWeatherData(self):
		return self.data