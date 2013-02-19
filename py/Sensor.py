from SensorPoller import SensorPoller

class Sensor(object):
	
	def __init__(self):
		self.poller = SensorPoller()
		self.pollSensor()

	def pollSensor(self):
		self.poller.updateSensorData()
		self.data = self.poller.getSensorData()

		self.temperature = self.data['Temp']
		self.humidity = self.data['Hum']

	# Returns a dictionary with both readings
	def getSensorData(self):
		return {'Temp':self.temperature, 'Hum':self.humidity}

	def getTemperature(self):
		return self.temperature

	def getHumidity(self):
		return self.humidity