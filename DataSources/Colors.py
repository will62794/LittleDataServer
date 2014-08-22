from DataSource import *
import random
import time

class Colors(DataSource):
	"""Connects to Open Weather Map Web API (http://openweathermap.org/current) and retrieves weather data for cities; 
	also does semantic, sentiment analysis, etc."""

	def __init__(self):
		super(Colors, self).__init__()
		#Set one default key
		self.options={}
		self.title="Colors"
		self.icon="http://270c81.medialib.glogster.com/aidallanos/media/7d/7da3f80f5680169c6520d8bccfa781b9d452325c/ks-color.png"
		self.defaultColorscale=[[255,255,255],[174,196,221],[168,207,56],[168,34,34]]
		self.defaultMin=0
		self.defaultMax=100
		self.renderers=["Colors"]

	def getKeyValue():
		return ["",""]



		


		
		