import json
import urllib2

class WeatherPoller(object):

	def __init__(self):
		pass

	"""
	Requests the json object from weather underground, reads the response, then returns the json string.
	"""
	def updateWeatherData(self):
		response = urllib2.urlopen('http://api.wunderground.com/api/3dcd75dc0e162700/conditions/q/IN/Indianapolis.json')
		data = response.read()
		return json.loads(data)