import subprocess
import ast

class OutputHandler(object):

	fanPin = 0
	fanOutput = False
	heatPin = 1
	heatOutput = False
	coolPin = 2
	coolOutput = False

	outputOn = 1
	outputOff = 0

	gpioCommand = "gpio"
	write = "write"
	mode = "mode"
	outputMode = "out"

	def __init__(self):
		self.__setupGPIO()

	"""
	Runs the command 'gpio mode pin# out' to set the mode for that specific pin number
	"""
	def __setupGPIO(self):
		process = subprocess.Popen([self.gpioCommand, self.mode, str(self.fanPin), self.outputMode], stdout=subprocess.PIPE)
		process = subprocess.Popen([self.gpioCommand, self.mode, str(self.heatPin), self.outputMode], stdout=subprocess.PIPE)
		process = subprocess.Popen([self.gpioCommand, self.mode, str(self.coolPin), self.outputMode], stdout=subprocess.PIPE)

	def disableAllOutputs(self):
		self.disableFan()
		self.disableHeat()
		self.disableCool()

	"""
	The fan should be enabled before heat or cool is enabled. Ideally, there should be a small delay before
	enabling heat or cool as well.
	"""
	def enableFan(self):
		process = subprocess.Popen([self.gpioCommand, self.write, str(self.fanPin), str(self.outputOn)], stdout=subprocess.PIPE)

	"""
	The fan should be disabled after heat or cool is disabled. Ideally, there should be a small delay after
	disabling heat or cool as well.
	"""
	def disableFan(self):
		process = subprocess.Popen([self.gpioCommand, self.write, str(self.fanPin), str(self.outputOff)], stdout=subprocess.PIPE)

	def enableCool(self):
		self.enableFan()
		process = subprocess.Popen([self.gpioCommand, self.write, str(self.coolPin), str(self.outputOn)], stdout=subprocess.PIPE)

	def disableCool(self):
		process = subprocess.Popen([self.gpioCommand, self.write, str(self.coolPin), str(self.outputOff)], stdout=subprocess.PIPE)
		self.disableFan()

	def enableHeat(self):
		self.enableFan()
		process = subprocess.Popen([self.gpioCommand, self.write, str(self.heatPin), str(self.outputOn)], stdout=subprocess.PIPE)

	def disableHeat(self):
		process = subprocess.Popen([self.gpioCommand, self.write, str(self.heatPin), str(self.outputOff)], stdout=subprocess.PIPE)
		self.disableFan()

	"""
	Used for debugging. Prints the status of all three outputs.
	"""
	def printOutputStatus(self):
		print "Fan: " + fanOutput + ", Heat: " + heatOutput + ", Cool: " + coolOutput
