import threading
from Sensor import Sensor
from Thermostat import Thermostat

# Time intervals for various functions in seconds
sensorPollInterval = 5

# Objects
sensor = Sensor()
tstat = Thermostat(sensor)

"""
Poll the sensor for temperature and humidity readings every five seconds, then
update the Sensor object with the most recent readings.
"""
def pollSensor():
    # Poll the sensor to grab updated readings
    sensor.pollSensor()

    # Get the sensor readings
    data = sensor.getSensorData()
    temperature = data['Temp']
    humidity = data['Hum']

    print "Temp: " + str(sensor.getTemperature()) + "\nHumidity: " + str(sensor.getHumidity())

    tstat.control()

    # call pollSensor() again in 'sensorPollInterval' seconds
    threading.Timer(sensorPollInterval, pollSensor).start()



# start calling f now and every 60 sec thereafter
pollSensor()