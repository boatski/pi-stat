import subprocess
import ast
from time import sleep

class OutputHandler(object):

	fanPin = 0
	fanOutput = False
	fanDelay = 5 # 5 seconds
	heatPin = 1
	heatOutput = False
	coolPin = 2
	coolOutput = False
	heatCoolDelay = 10 # 10 seconds

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
		self.disableHeat()
		self.disableCool()
		self.disableFan()

	"""
	The fan should be enabled before heat or cool is enabled. Ideally, there should be a small delay before
	enabling heat or cool as well.
	"""
	def enableFan(self):
		process = subprocess.Popen([self.gpioCommand, self.write, str(self.fanPin), str(self.outputOn)], stdout=subprocess.PIPE)
		# Start fan delay if enabling fan
		if self.fanOutput == False:
			sleep(self.fanDelay)
		self.fanOutput = True

	"""
	The fan should be disabled after heat or cool is disabled. Ideally, there should be a small delay after
	disabling heat or cool as well.
	"""
	def disableFan(self):
		# Start fan delay if disabling fan
		if self.fanOutput == True:
			sleep(self.fanDelay)
		process = subprocess.Popen([self.gpioCommand, self.write, str(self.fanPin), str(self.outputOff)], stdout=subprocess.PIPE)
		self.fanOutput = False

	def enableCool(self):
		self.enableFan()
		process = subprocess.Popen([self.gpioCommand, self.write, str(self.coolPin), str(self.outputOn)], stdout=subprocess.PIPE)
		if self.coolOutput == False:
			sleep(self.heatCoolDelay)
		self.coolOutput = True

	def disableCool(self):
		process = subprocess.Popen([self.gpioCommand, self.write, str(self.coolPin), str(self.outputOff)], stdout=subprocess.PIPE)
		self.disableFan()
		self.coolOutput = False

	def enableHeat(self):
		self.enableFan()
		process = subprocess.Popen([self.gpioCommand, self.write, str(self.heatPin), str(self.outputOn)], stdout=subprocess.PIPE)
		if self.heatOutput == False:
			sleep(self.heatCoolDelay)
		self.heatOutput = True

	def disableHeat(self):
		process = subprocess.Popen([self.gpioCommand, self.write, str(self.heatPin), str(self.outputOff)], stdout=subprocess.PIPE)
		self.disableFan()
		self.heatOutput = False

	"""
	Used for debugging. Prints the status of all three outputs.
	"""
	def printOutputStatus(self):
		print "Fan: " + str(self.fanOutput) + " | Heat: " + str(self.heatOutput) + " | Cool: " + str(self.coolOutput)
