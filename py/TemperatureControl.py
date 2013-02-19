import sqlite3 as lite
import sys
from Setpoint import Setpoint
from Lockout import Lockout
from Sensor import Sensor

class TemperatureControl(object):
	
	con = None
	indoorTemperature = 76
	outdoorTemperature = 82
	offset = 1

	fanIsOn = False
	heatIsOn = False
	coolIsOn = False
	scheduleIsOn = True

	def __init__(self, sensor):
		self.sensor = sensor
		self.updateSetpoints()

	"""
	Used to determine what outputs should be switched on and what outputs should be switched off.
	** Minimum on times for Heat/Cool and a Fan delay needs to be implemented. **
	"""
	def control(self):
		self.updateSetpoints()
		self.indoorTemperature = self.sensor.getTemperature()

		if self.outdoorTemperature >= self.outdoorLockout.getSetpoint(): # If outdoorTemp >= outdoorLockout, do not heat
			if self.scheduleIsOn:
				if self.indoorTemperature >= (self.occupiedCool.getSetpoint() + self.offset): # Turn on cool
					self.fanIsOn = True
					self.heatIsOn = False
					self.coolIsOn = True
				else:
					self.fanIsOn = False
					self.heatIsOn = False
					self.coolIsOn = False
			else: # Schedule is off
				if self.indoorTemperature >= (self.unoccupiedCool.getSetpoint() + self.offset): # Turn on cool
					self.fanIsOn = True
					self.heatIsOn = False
					self.coolIsOn = True
				else:
					self.fanIsOn = False
					self.heatIsOn = False
					self.coolIsOn = False
		elif self.outdoorTemperature < self.outdoorLockout.getSetpoint(): # If outdoorTemp < outdoorLockout, do not cool
			if self.scheduleIsOn:
				if self.indoorTemperature <= (self.occupiedHeat.getSetpoint() - self.offset): # Turn on heat
					self.fanIsOn = True
					self.heatIsOn = True
					self.coolIsOn = False
				else:
					self.fanIsOn = False
					self.heatIsOn = False
					self.coolIsOn = False
			else: # Schedule is off
				if self.indoorTemperature <= (self.unoccupiedHeat.getSetpoint() - self.offset): # Turn on heat
					self.fanIsOn = True
					self.heatIsOn = True
					self.coolIsOn = False
				else:
					self.fanIsOn = False
					self.heatIsOn = False
					self.coolIsOn = False

	def updateSetpoints(self):
		self.__getSetpoints()

	"""
	Grabs the current setpoints from the database.
	"""
	def __getSetpoints(self):
		# Grab setpoint data from the sqlite database
		try:
			con = lite.connect('../db/pi-stat.db')
			cur = con.cursor()
			cur.execute("SELECT * FROM Thermostat;")

			data = cur.fetchone()

			# Setpoints
			self.occupiedCool = Setpoint(data[0])
			self.unoccupiedCool = Setpoint(data[1])
			self.occupiedHeat = Setpoint(data[2])
			self.unoccupiedHeat = Setpoint(data[3])
			self.outdoorLockout = Lockout(data[4])

		except lite.Error, e:
		    print "Error %s:" % e.args[0]
		    sys.exit(1)
		    
		finally:
		    if con:
		        con.close()