from DataSource import *
import random
import time

class Weather(DataSource):
	"""Connects to Open Weather Map Web API (http://openweathermap.org/current) and retrieves weather data for cities; 
	also does semantic, sentiment analysis, etc."""

	def __init__(self):
		super(Weather, self).__init__()
		#Set one default key
		self.options={"Locations":["New York","Los Angeles","19075","10001"],"Randomize":False}
		self.title="Weather"
		self.icon="https://cdn3.iconfinder.com/data/icons/weather-and-forecast/51/Weather_icons_grey-03-512.png"
		self.renderers=["MagnitudeColorBar"]
		self.defaultColorscale=[[255,255,255],[174,196,221],[168,207,56],[168,34,34]]
		self.defaultMin=0
		self.defaultMax=100


	def CityWeatherData(self,city):
		#if zipcode
		cityString=city
		if len(city)==5 and city.isdigit():
			cityString=self.getCityForZipCode(city)
		url="http://api.openweathermap.org/data/2.5/weather?q="+cityString
		return self.getDataFromUrl(url)
	
	def getCityForZipCode(self,zipcode):
		url="http://ziptasticapi.com/"+zipcode
		return self.getDataFromUrl(url)["city"]


	def getRandomWorldCity(self):
		url="http://filltext.com/?rows=1&city={city}"
		return self.getDataFromUrl(url)[0]["city"]

	def chooseCity(self):
		random.seed(time.time())
		return random.choice(self.options["Locations"])

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
		if self.options["Randomize"]:
			city=self.getRandomWorldCity()
		else:
			city=random.choice(self.options["Locations"])
		temp=self.getTemperature(city)
		return [city,str(int(float(temp)))]

	def kelvinToCelsius(self,C):
		return (C - 273.15)* 1.8000

	def kelvinToFahrenheit(self,K):
		return 32+(K - 273.15)*1.8000




		


		
		