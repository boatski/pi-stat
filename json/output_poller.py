#!/usr/bin/python python
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
	Reads the status of the three GPIO used as outputs. Web server user (www-data) needs
	to be able to run sudo on the gpio command without requiring a password.
	"""
	def updateOutputData(self):
		try:
			fan = subprocess.check_output(["sudo", "gpio", "read", "0"])

			heat = subprocess.check_output(["sudo", "gpio", "read", "1"])

			cool = subprocess.check_output(["sudo", "gpio", "read", "2"])

			status = {'fan':self.removeEscapeChar(fan), 'heat':self.removeEscapeChar(heat), 'cool':self.removeEscapeChar(cool)}
		except Exception:
			status = {'fan':"FAIL", 'heat':"FAIL", 'cool':"FAIL"}

		return status

	def removeEscapeChar(self, out):
		return out[0]