import subprocess
import ast

""" 
Runs the C program to poll the DHT 11 sensor.
Output is then parsed into a dictionary
"""
#process = subprocess.Popen(['../Adafruit_DHT', '11', '4'], stdout=subprocess.PIPE)
#out, err = process.communicate()
temp = "'Temp' : 72, 'Hum' : 35"
out = "{" + temp + "}"

data = ast.literal_eval(out)

temperature = data['Temp']
humidity = data['Hum']

print("Temperature: " + str(temperature))
print("Humidity: " + str(humidity))
