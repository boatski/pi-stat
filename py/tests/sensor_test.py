import unittest
import sys
print (sys.path)
from pistat.snsr import Sensor

class SensorTests(unittest.TestCase):

	def testTemperature(self):
		sensor = Sensor()
		temperature = sensor.getTemperature()
		self.failIf(temperature < 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()