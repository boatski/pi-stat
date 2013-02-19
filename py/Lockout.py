from Setpoint import Setpoint

"""
An outdoor temperature lockout is used to either disable heat or disable cool. For example,
if the outdoor lockout = 60 and the outdoor temperature = 78, then heat will be disabled
until the outdoor temperature is less than 60 and vice versa.
"""
class Lockout(Setpoint):
	maxSetpoint = 70
	minSetpoint = 50

	def __init__(self, temperature = None):
		if temperature != None:
			super(Lockout, self).setpointCheck(temperature)