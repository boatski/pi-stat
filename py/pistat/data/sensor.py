
"""
sensor.py acts as an adapter class for different sensor types.
"""
class Sensor(object):
	# Indoor conditions
	indoorTemperature = 0
	indoorHumidity = 0
	indoorData = {}
	
	def __init__(self):
		pass

	def pollSensor(self):
		pass

	# Returns a dictionary with all data
	def getSensorData(self):
		return self.indoorData

	def getIndoorTemperature(self):
		return self.indoorTemperature

	def getIndoorHumidity(self):
		return self.indoorHumidity
