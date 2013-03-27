import sqlite3 as lite
import datetime
from day import Day

class Schedule(object):

	scheduleDays = {}
	days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

	def __init__(self):
		self.updateSchedule()

	def updateSchedule(self):
		try:
			con = lite.connect('../../db/pi-stat.db')
			cur = con.cursor()
			cur.execute("SELECT * FROM Schedule ;")
			data = cur.fetchall()

			for row in data:
				# Day, StartTime, StopTime
				self.createNewDay(row[0], row[1], row[2])

		except lite.Error, e:
		    print "Error %s:" % e.args[0]
		    sys.exit(1)
		    
		finally:
		    if con:
		        con.close()

	def updateScheduleForToday(self, cur):
		pass

	def createNewDay(self, day, startTime, stopTime):
		schedule = Day(day, startTime, stopTime)
		self.scheduleDays[day] = schedule

	def getScheduleForToday(self):
		self.updateSchedule()
		now = datetime.datetime.now()
		weekday = now.weekday() # returns an int 0-6
		today = self.days[weekday]

		return self.scheduleDays[today]