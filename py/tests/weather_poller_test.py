import unittest
import sys
sys.path.append('../')
from weather_poller import WeatherPoller

class WeatherPollerTests(unittest.TestCase):

	def testTemperature(self):
		weather = WeatherPoller("Indianapolis", "IN")
		weather.updateWeather()
		data = weather.getWeatherData()

		temperature = data['current_observation']['temp_f']
		print "Temperature: " + str(temperature)
		self.failIf(temperature < 0)

	def testHumidity(self):
		weather = WeatherPoller("Indianapolis", "IN")
		weather.updateWeather()
		data = weather.getWeatherData()

		humidity = data['current_observation']['relative_humidity']
		print "Humidity: " + str(humidity)
		self.failIf(humidity < 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()