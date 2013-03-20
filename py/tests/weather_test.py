import unittest

class WeatherTests(unittest.TestCase):

	def testTemperature(self):
		weather = WeatherPoller("Indianapolis", "IN")
		weather.updateWeather()
		data = weather.getWeatherData()

		temperature = data['current_observation']['temp_f']
		print "Temperature: " + str(temperature)
		self.failIf(temperature < 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()