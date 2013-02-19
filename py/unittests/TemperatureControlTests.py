import unittest
import sys
sys.path.append('../')
from TemperatureControl import TemperatureControl

class LockoutTests(unittest.TestCase):

	def testGetter(self):
		temperature = 60
		setpoint = Lockout(temperature)
		self.failIf(setpoint.getSetpoint() != temperature)

def main():
    unittest.main()

if __name__ == '__main__':
    main()