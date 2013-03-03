import subprocess

class OutputPoller(object):

	gpio = "gpio"
	read = "read"
	fanPin = 0
	heatPin = 1
	coolPin = 2

	def __init__(self):
		pass

	"""
	Reads the status of the three GPIO used as outputs.
	"""
	def updateOutputData(self):
		process = subprocess.Popen([self.gpio, self.read, str(self.fanPin)], stdout=subprocess.PIPE)
		fan, err = process.communicate()

		process = subprocess.Popen([self.gpio, self.read, str(self.heatPin)], stdout=subprocess.PIPE)
		heat, err = process.communicate()

		process = subprocess.Popen([self.gpio, self.read, str(self.coolPin)], stdout=subprocess.PIPE)
		cool, err = process.communicate()

		status = {'fan':fan, 'heat':heat, 'cool':cool}
		return status