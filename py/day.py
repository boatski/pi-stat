

class Day(object):

	def __init__(self, day, startTime, stopTime):
		self.day = day
		self.startTime = startTime
		self.stopTime = stopTime

	def getDay(self):
		return self.day

	def getStartTime(self):
		return self.startTime

	def getStopTime(self):
		return self.stopTime

	def setDay(self, day):
		self.day = day

	def setStartTime(self, startTime):
		self.startTime = startTime

	def setStopTime(self, stopTime):
		self.stopTime = stopTime