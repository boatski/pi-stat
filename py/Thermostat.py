from TemperatureControl import TemperatureControl

class Thermostat(object):
	
	def __init__(self, sensor):
		self.sensor = sensor
		self.tempControl = TemperatureControl(self.sensor)

	def control(self):
		self.tempControl.control()