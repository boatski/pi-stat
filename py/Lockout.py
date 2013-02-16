from Setpoint import Setpoint

class Lockout(Setpoint):
	maxSetpoint = 70
	minSetpoint = 50

	def __init__(self, temperature = None):
		if temperature != None:
			super(Lockout, self).setpointCheck(temperature)