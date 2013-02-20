from SensorPoller import SensorPoller

class Sensor(object):
	temperature = 0
	humidity = 0
	
	def __init__(self):
		self.poller = SensorPoller()
		self.pollSensor()

	"""
	Calls the SensorPoller to poll the sensor and update the dictionary with new
	temperature and humidity values.
	"""
	def pollSensor(self):
		self.poller.updateSensorData()
		self.data = self.poller.getSensorData()
		
		if self.data:
			self.temperature = self.data['Temp']
			self.humidity = self.data['Hum']

	# Returns a dictionary with both readings
	def getSensorData(self):
		return {'Temp':self.temperature, 'Hum':self.humidity}

	def getTemperature(self):
		return self.temperature

	def getHumidity(self):
		return self.humidity
