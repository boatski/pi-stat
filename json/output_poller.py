import RPi.GPIO as GPIO

class OutputPoller(object):

	def __init__(self):
		GPIO.setmode(GPIO.BCM) # BCM pin numbering
		GPIO.setwarnings(False) # Disable warnings for GPIO already being setup
		GPIO.setup(17, GPIO.OUT)
		GPIO.setup(18, GPIO.OUT)
		GPIO.setup(27, GPIO.OUT)
		self.updateOutputData()

	"""
	Reads the status of the three GPIO used as outputs.
	"""
	def updateOutputData(self):
		fan = GPIO.input(17)
		cool = GPIO.input(27)
		heat = GPIO.input(18)

		status = {'fan':fan, 'heat':heat, 'cool', cool}
		return status