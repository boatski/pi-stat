import subprocess
import ast


process = subprocess.Popen(['../Adafruit_DHT', '11', '4'], stdout=subprocess.PIPE)
out, err = process.communicate()

out = "{" + out + "}"

data = ast.literal_eval(out)

print("Temperature: " + str(data['Temp']))
