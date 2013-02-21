import unittest
import sys
sys.path.append('../')
from Setpoint import Setpoint

class SetpointTests(unittest.TestCase):

	def testGetter(self):
		temperature = 75
		setpoint = Setpoint(temperature)
		self.failIf(setpoint.getSetpoint() != temperature)
	
	def testSetter(self):
		temperature = 75
		setpoint = Setpoint(temperature)

		#Set new setpoint
		newTemperature = 72
		setpoint.setSetpoint(newTemperature)
		self.failIf(setpoint.getSetpoint() != newTemperature)

	def testHighSetpoint(self):
		temperature = 85
		setpoint = Setpoint(temperature)
		self.failIf(setpoint.getSetpoint() != 80)

	def testLowSetpoint(self):
		temperature = 55
		setpoint = Setpoint(temperature)
		self.failIf(setpoint.getSetpoint() != 60)

	def testEmptySetpoint(self):
		setpoint = Setpoint()

def main():
    unittest.main()

if __name__ == '__main__':
    main()