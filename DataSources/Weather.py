from DataSource import *
import random
import time

class Weather(DataSource):
	"""Connects to Open Weather Map Web API (http://openweathermap.org/current) and retrieves weather data for cities; 
	also does semantic, sentiment analysis, etc."""

	def __init__(self):
		super(Weather, self).__init__()
		#Set one default key
		self.options={"Cities":["New York","Los Angeles"],"ZipCodes":["19075"],"RandomCities":False}
		self.title="Weather"

	def CityWeatherData(self,city):
		url="http://api.openweathermap.org/data/2.5/weather?q="+city
		return self.getDataFromUrl(url)
	
	def getRandomWorldCity(self):
		url="http://filltext.com/?rows=1&city={city}"
		return self.getDataFromUrl(url)[0]["city"]

	def chooseCity(self):
		random.seed(time.time())
		return random.choice(self.options["Cities"])

	def getTemperature(self,city):
		return str(self.kelvinToFahrenheit(float(self.CityWeatherData(city)["main"]["temp"])))

	def getWeatherDescriptors(self,city):
		descriptors=self.CityWeatherData(city)["weather"][0]
		return [descriptors["main"],descriptors["description"]]

	def getLetterCode(self,city):
		url="http://airportcode.riobard.com/search?q="+city.lower()+"&fmt=JSON"
		return self.getDataFromUrl(url)[0]["code"]

	def getKeyValue(self):
		random.seed(time.time())
		if self.options["RandomCities"]:
			city=self.getRandomWorldCity()
		else:
			city=random.choice(self.options["Cities"])
		temp=self.getTemperature(city)
		return [city,str(int(float(temp)))]

	def kelvinToCelsius(self,C):
		return (C - 273.15)* 1.8000

	def kelvinToFahrenheit(self,K):
		return 32+(K - 273.15)*1.8000




		


		
		