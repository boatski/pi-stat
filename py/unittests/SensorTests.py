import unittest
import sys
sys.path.append('../')
from Sensor import Sensor

class LockoutTests(unittest.TestCase):

	def testData(self):
		sensor = Sensor()

		data = sensor.getSensorData()
		dataTemp = data['Temp']
		dataHum = data['Hum']

		# Default readings used when sensor is unavailable
		self.failUnless(75 == dataTemp or 35 == dataHum)

	def testTemperature(self):
		sensor = Sensor()

		temperature = sensor.getTemperature()

		self.failUnless(temperature == 75)

	def testTemperatureBounds(self):
		sensor = Sensor()
		maxTemp = 90
		minTemp = 40

		temperature = sensor.getTemperature()

		self.failIf(temperature < minTemp or temperature > maxTemp)

	def testHumidity(self):
		sensor = Sensor()

		humidity = sensor.getHumidity()

		self.failUnless(humidity == 35)

	def testHumidityBounds(self):
		sensor = Sensor()
		maxHum = 100
		minHum = 0

		humidity = sensor.getHumidity()

		self.failIf(humidity < minHum or humidity > maxHum)

def main():
    unittest.main()

if __name__ == '__main__':
    main()