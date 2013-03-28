#!/usr/bin/python python
import subprocess
import datetime
import sys
from datetime import date
import sqlite3 as lite

class History(object):
	indoorTemperature = 0
	indoorHumidity = 0

	def __init__(self, sensor, weather):
		self.sensor = sensor
		self.weather = weather

	def getHistoryData(self):
		# Get the sensor readings
		self.sensorData = self.sensor.getSensorData()
		self.weatherData = self.weather.getWeatherData()
	
		# Only update temperatures if the dictionary is not empty
		if self.sensorData:
			self.indoorTemperature = self.sensorData['Temp']
			self.indoorHumidity = self.sensorData['Hum']

		# Only update temperatures if the dictionary is not empty
		if self.weatherData:
			self.outdoorTemperature = self.weatherData['current_observation']['temp_f']
			self.outdoorHumidity = self.weatherData['current_observation']['relative_humidity']
			humSplit = self.outdoorHumidity.split('%')
			self.outdoorHumidity = humSplit[0]

		self.fan = subprocess.check_output(["sudo", "gpio", "read", "0"])
		self.fan = self.fan[0]

		self.heat = subprocess.check_output(["sudo", "gpio", "read", "1"])
		self.heat = self.heat[0]

		self.cool = subprocess.check_output(["sudo", "gpio", "read", "2"])
		self.cool = self.cool[0]

		#self.printData()

	def writeHistoryData(self):
		now = datetime.datetime.now()
		try:
			con = lite.connect('../../db/pi-stat.db')
			cur = con.cursor()
			#query = "INSERT INTO History(IndoorTemperature, IndoorHumidity, OutdoorTemperature, OutdoorHumidity, Fan, Heat, Cool, Date) "
			#query += "VALUES(" + str(self.indoorTemperature) + ", " + str(self.indoorHumidity) + ", " + str(self.outdoorTemperature) + ", " + str(self.outdoorHumidity) + ", "
			#query += str(self.fan) + ", " + str(self.heat) + ", " + str(self.cool) + ", '" + str(now )+ "');"
			historyData = [self.indoorTemperature, self.indoorHumidity, self.outdoorTemperature, self.outdoorHumidity, self.fan, self.heat, self.cool, now]
			cur.execute("INSERT INTO History VALUES (?, ?, ?, ?, ?, ?, ?, ?)", historyData)
			con.commit()
			#print "Complete"
		except lite.Error, e:
		    print "Error %s:" % e.args[0]
		    sys.exit(1)
		    
		finally:
		    if con:
		        con.close()

	def printData(self):
		print "*** History ***"
		print "Indoor - Temperature: " + str(self.indoorTemperature) + " | Humidity: " + str(self.indoorHumidity)
		print "Outdoor - Temperature: " + str(self.outdoorTemperature) + " | Humidity: " + str(self.outdoorHumidity)
		print "Outputs - Fan: " + str(self.fan) + " | Heat: " + str(self.heat) + " | Cool: " + str(self.cool)


