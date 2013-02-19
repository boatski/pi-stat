import unittest
import sys
sys.path.append('../')
from SensorPoller import SensorPoller

class LockoutTests(unittest.TestCase):

	def testData(self):
		poll = SensorPoller()

		data = poll.getSensorData()
		dataTemp = data['Temp']
		dataHum = data['Hum']

		# Default readings used when sensor is unavailable
		self.failUnless(75 == dataTemp or 35 == dataHum)

def main():
    unittest.main()

if __name__ == '__main__':
    main()