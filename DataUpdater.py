import threading
from DataSources import Weather,Asana
from Renderers import MagnitudeColorBarRenderer
import time


class DataUpdater(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.datasources={"Weather":Weather.Weather(),"Asana":Asana.AsanaAPI()}
		self.current_datasource=self.datasources.values()[0]

		self.renderers={"MagnitudeColorBar":MagnitudeColorBarRenderer.MagnitudeColorBarRenderer()}
		self.current_renderer=self.renderers.values()[0]

		self.lastChange=time.time()
		self.waittime=12

		print "CREATED"


	def run(self):
		while True:
			#print abs(time.time()-self.lastChange)
			if abs(time.time()-self.lastChange)>self.waittime:
				keyValuePair=self.current_datasource.getKeyValue()
				self.current_renderer.draw(keyValuePair[0],keyValuePair[1])
				print self.current_datasource.title
				print keyValuePair
				self.lastChange=time.time()

			time.sleep(2.0)
		