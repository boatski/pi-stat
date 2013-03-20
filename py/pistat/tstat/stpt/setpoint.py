"""
Setpoint is used as a control temperature for the Thermostat class.
"""
class Setpoint(object):
	maxSetpoint = 80
	minSetpoint = 60
	setpoint = 72

	def __init__(self, setpoint = None):
		if setpoint != None:
			self.setpointCheck(setpoint)

	def getSetpoint(self):
		return self.setpoint

	def setSetpoint(self, setpoint):
		self.setpointCheck(setpoint)

	def setpointCheck(self, setpoint):
		# Enforce min and max setpoints even though they're enforced on the front-end
		if setpoint > self.maxSetpoint:
			self.setpoint = self.maxSetpoint
		elif setpoint < self.minSetpoint:
			self.setpoint = self.minSetpoint
		else:
			self.setpoint = setpoint