"""
Setpoint is used as a control temperature for the TemperatureControl class.
"""
class Setpoint(object):
	maxSetpoint = 80
	minSetpoint = 60
	temperature = 72

	def __init__(self, temperature = None):
		if temperature != None:
			self.setpointCheck(temperature)

	def getSetpoint(self):
		return self.temperature

	def setSetpoint(self, temperature):
		self.setpointCheck(temperature)

	def setpointCheck(self, temperature):
		# Enforce min and max setpoints even though they're enforced on the front-end
		if temperature > self.maxSetpoint:
			self.temperature = self.maxSetpoint
		elif temperature < self.minSetpoint:
			self.temperature = self.minSetpoint
		else:
			self.temperature = temperature