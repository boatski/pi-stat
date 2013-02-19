import subprocess
import ast

class SensorPoller(object):
	_instance = None
	defaultSensorPin = 4
	defaultSensorType = 11

	maxWiringPiPins = 16
	firstWiringPiPin = 0
	sensorProgramLocatoin = "../Adafruit_DHT"

	def __init__(self, sensorPin = None, sensorType = None):
		if sensorPin == None or sensorPin > self.maxWiringPiPins or sensorPin < firstWiringPiPin:
			self.sensorPin = self.defaultSensorPin
		else:
			self.sensorPin = sensorPin

		if sensorType == None:
			self.sensorType = self.defaultSensorType
		else:
			self.sensorType = sensorType

		self.updateSensorData()

	""" 
	Runs the C program to poll the DHT 11 sensor. Output is then parsed into a dictionary. The C
	program is provided by Adafruit.com
	A temporary dictionary is used to test on other platforms where the sensor can't be polled.
	"""
	def updateSensorData(self):
		#process = subprocess.Popen([sensorProgramLocatoin, defaultSensorType, defaultSensorPin], stdout=subprocess.PIPE)
		#out, err = process.communicate()
		temp = "'Temp' : 24, 'Hum' : 35"
		out = "{" + temp + "}"

		# Convert the string into a dictionary
		self.data = ast.literal_eval(out)

		# Convert the temperature from C to F -> C * 9/5 + 32 = F
		self.data['Temp'] = self.data['Temp'] * 9/5 + 32

	def getSensorData(self):
		return self.data