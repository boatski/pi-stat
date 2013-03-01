import sqlite3 as lite
import sys
import datetime
from setpoint import Setpoint
from lockout import Lockout
from sensor import Sensor
from schedule import Schedule
from output_handler import OutputHandler

class Thermostat(object):
	
	con = None
	indoorTemperature = 0
	indoorHumidity = 0
	prevTemperature = 0
	prevHumidity = 0

	outdoorTemperature = 32
	offset = 1

	self.scheduleIsOn = False
	
	def __init__(self, sensor):
		self.sensor = sensor
		self.schedule = Schedule()
		self.output = OutputHandler()
		self.updateSetpoints()
		self.checkSchedule()

	"""
	Used to determine what outputs should be switched on and what outputs should be switched off.
	** Minimum on times for Heat/Cool and a Fan delay needs to be implemented. **
	"""
	def control(self):
		self.updateSetpoints()
		self.checkSchedule()

		# Get the sensor readings
		self.data = self.sensor.getSensorData()
	
		# Only update temperatures if the dictionary is not empty
		if self.data:
			self.indoorTemperature = self.data['Temp']
			self.indoorHumidity = self.data['Hum']

		if self.indoorTemperature != self.prevTemperature or self.indoorHumidity != self.prevHumidity:
			self.prevTemperature = self.indoorTemperature
			self.prevHumidity = self.indoorHumidity

			print "Temp: " + str(self.sensor.getTemperature()) + "\nHumidity: " + str(self.sensor.getHumidity())

		self.setOutput()
		self.output.printOutputStatus()

		

	def setOutput(self):
		if self.outdoorTemperature >= self.outdoorLockout.getSetpoint(): # If outdoorTemp >= outdoorLockout, do not heat
			if self.scheduleIsOn:
				if self.indoorTemperature > (self.occupiedCool.getSetpoint() + self.offset): # Turn on cool
					self.output.enableCool()
				else:
					self.output.disableCool()
			else: # Schedule is off
				if self.indoorTemperature > (self.unoccupiedCool.getSetpoint() + self.offset): # Turn on cool
					self.output.enableCool()
				else:
					self.output.disableCool()
		elif self.outdoorTemperature < self.outdoorLockout.getSetpoint(): # If outdoorTemp < outdoorLockout, do not cool
			if self.scheduleIsOn:
				if self.indoorTemperature < (self.occupiedHeat.getSetpoint() - self.offset): # Turn on heat
					self.output.enableHeat()
				else:
					self.output.disableHeat()
			else: # Schedule is off
				if self.indoorTemperature < (self.unoccupiedHeat.getSetpoint() - self.offset): # Turn on heat
					self.output.enableHeat()
				else:
					self.output.disableHeat()
		

	"""
	Grabs the current setpoints from the database.
	"""
	def updateSetpoints(self):
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

	"""
	Compares the schedule start and stop time with the current time.
	If scheduleStop <= now <= scheduleStart, then set scheduleIsOn = True, else False
	"""
 	def checkSchedule(self):
 		now = datetime.datetime.now()
 		self.todaysSchedule = self.schedule.getScheduleForToday()

 		# Split hours and minutes
 		scheduleOn = todaysSchedule.getStartTime().split(':', 1)
 		scheduleOnHour = int(scheduleOn[0])
 		scheduleOnMinute = int(scheduleOn[1])
 		scheduleStart = now.replace(hour = scheduleOnHour, minute = scheduleOnMinute, second = 0, microsecond = 0)

 		scheduleOff = todaysSchedule.getStopTime().split(':', 1)
 		scheduleOffHour = int(scheduleOff[0])
 		scheduleOffMinute = int(scheduleOff[1])
 		scheduleStop = now.replace(hour = scheduleOffHour, minute = scheduleOffMinute, second = 0, microsecond = 0)

 		if now >= scheduleStart and now <= scheduleStop:
 			self.scheduleIsOn = True
 		else:
 			self.scheduleIsOn = False





