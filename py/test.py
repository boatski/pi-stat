from Sensor import Sensor

sensor = Sensor(72,35)

class A(object):

	def __init__(self, s):
		self.s = s
		print str(self.s.getTemperature())

	def printTemp(self):
		print str(self.s.getTemperature())

class B(object):

	def __init__(self, s):
		self.s = s
		print str(self.s.getTemperature())

	def printTemp(self):
		print str(self.s.getTemperature())

a = A(sensor)
b = B(sensor)

sensor.updateReadings(75,35)

a.printTemp()
b.printTemp()