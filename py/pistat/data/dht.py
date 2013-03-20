import subprocess
import ast
from .sensor import Sensor

class DHT(Sensor):

	# Default GPIO Pins
	defaultSensorPin = 4
	defaultSensorType = 11

	# GPIO Pin Bounds
	maxWiringPiPins = 16
	firstWiringPiPin = 0

	# shell commands
	sensorProgramLocation = "./../../Adafruit_DHT"
	sudo = "sudo"

	"""
	Check pin numbers or set to default pin.
	"""
	def __init__(self, sensorPin = None, sensorType = None):
		if sensorPin == None or sensorPin > self.maxWiringPiPins or sensorPin < self.firstWiringPiPin:
			self.sensorPin = self.defaultSensorPin
		else:
			self.sensorPin = sensorPin

		if sensorType == None:
			self.sensorType = self.defaultSensorType
		else:
			self.sensorType = sensorType

	"""
	Run the Adafruit_DHT driver to get the current temperature and humidity
	from the sensor. Convert the data into a dictionary.
	"""
	def pollSensor(self):
		process = subprocess.Popen([self.sudo, self.sensorProgramLocation, str(self.defaultSensorType), str(self.defaultSensorPin)], stdout=subprocess.PIPE)
		out, err = process.communicate()
		#out = "'Temp':24, 'Hum':35"
		out = "{" + out + "}"

		# Convert the string into a dictionary
		Sensor.indoorData = ast.literal_eval(out)
		
		# Convert the temperature from C to F -> C * 9/5 + 32 = F
		if Sensor.indoorData: # False if the dictionary is empty
			Sensor.indoorData['Temp'] = Sensor.indoorData['Temp'] * 9/5 + 32
			Sensor.indoorTemperature = Sensor.indoorData['Temp']
			Sensor.indoorHumidity = Sensor.indoorData['Hum']
			