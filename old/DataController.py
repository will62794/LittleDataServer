import time
import random
import threading
from threading import Thread

import SerialDraw

from DataSources import WeatherMan
from DataSources import Asana
from DataSources import StockBroker


class DataController(Thread):
	"""docstring for DataController"""
	def __init__(self):	
		Thread.__init__(self)
		self.drawer=SerialDraw.SerialDraw()
		self.drawer.WakeUpTeensy()
		
		self.weather=WeatherMan.WeatherMan()
		self.asana = Asana.AsanaAPI('3D31plGb.tYIr08vhXQI3GEE8XgGm3AG', debug=True)

		self.lastChangeTime=time.time()-10.1

		self.modes=["weather","asana","color"]

		self.current_mode="weather"
		self.running=False


	def run(self):
		while not self.running:
			pass
		while True:
			decision=self.newDecision()
			print "New Decision: "+str(decision)
			time.sleep(1.0)

	def newDecision(self):
		current_time=time.time()
		delayTime=12
		if(abs(self.lastChangeTime-current_time)>delayTime):
			#choice=random.choice(self.open_modes)
			#if choice!=self.current_mode:
			self.showMode(self.current_mode)
			#self.current_mode=choice
			self.lastChangeTime=time.time()
			return self.current_mode
		return "no change"


	def showMode(self,mode):
		if self.current_mode=="weather":
			self.drawNewWeather()
		if mode=="asana":
			self.drawNewAsana()
		if mode=="color":
			self.drawNewColor()



	def drawNewWeather(self):
		city=self.weather.getRandomCity()
		temp=self.weather.getTemperature(city)
		color1=self.weather.getColorForTemperature(temp)
		color2=self.weather.getColorForTemperature(str(float(temp)-3.0))
		value=str(int(100*self.weather.getPercentageForTemperature(temp)))
		lettercode=(city[:2]).upper()

		#SerialDraw.clearScreen()
		self.drawer.clearDrawBuffer()
		self.drawer.drawGradientBarWithValue(color1,color2,value,lettercode)
		self.drawer.transition("slide")
		return (temp)

	def drawNewAsana(self):
		# see your workspaces
		myspaces = self.asana.list_workspaces()  #Result: [{u'id': 123456789, u'name': u'asanapy'}]
		workspace_id=myspaces[0]["id"]
		all_projects = self.asana.list_projects(workspace=workspace_id,include_archived=False)  #Result: [{u'id': 123456789, u'name': u'asanapy'}]


		project=random.choice(all_projects)
		tasks=self.asana.get_project_tasks(project["id"])
		projectName=str(project["name"]).upper()
		print projectName
		num_tasks=len(tasks)*4

		self.drawer.clearDrawBuffer()
		self.drawer.drawRectangle(0,0,16,64,[180,180,num_tasks])
		self.drawer.drawVerticalString(projectName[:9],[0,0,0])
		self.drawer.transition("slide")
	
	def drawNewColor(self,color):
		pass



