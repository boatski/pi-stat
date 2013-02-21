import unittest
#import sys
#sys.path.append('../')
from py.Lockout import Lockout

class LockoutTests(unittest.TestCase):

	def testGetter(self):
		temperature = 60
		setpoint = Lockout(temperature)
		self.failIf(setpoint.getSetpoint() != temperature)
	
	def testSetter(self):
		temperature = 60
		setpoint = Lockout(temperature)

		#Set new setpoint
		newTemperature = 55
		setpoint.setSetpoint(newTemperature)
		self.failIf(setpoint.getSetpoint() != newTemperature)

	def testHighSetpoint(self):
		temperature = 75
		setpoint = Lockout(temperature)
		self.failIf(setpoint.getSetpoint() != 70)

	def testLowSetpoint(self):
		temperature = 45
		setpoint = Lockout(temperature)
		self.failIf(setpoint.getSetpoint() != 50)

	def testEmptySetpoint(self):
		setpoint = Lockout()

def main():
    unittest.main()

if __name__ == '__main__':
    main()