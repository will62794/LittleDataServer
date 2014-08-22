import threading
from DataSources import Weather,Asana,Subway
from Renderers import MagnitudeColorBarRenderer,SubwayRenderer,ColorBarRenderer
import time


class DataUpdater(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.datasources={"Weather":Weather.Weather(),"Asana":Asana.AsanaAPI()}
		self.datasources={"Weather":Weather.Weather(),"Asana":Asana.AsanaAPI(),"Subway":Subway.Subway()}

		self.current_datasource=self.datasources.values()[0]

		self.renderers={"MagnitudeColorBar":MagnitudeColorBarRenderer.MagnitudeColorBarRenderer(),"ColorBar":ColorBarRenderer.ColorBarRenderer(),"Subway":SubwayRenderer.SubwayRenderer()}
		self.current_renderer=self.renderers.values()[0]

		self.lastChange=time.time()
		self.waittime=12

		print "CREATED"


	def run(self):
		while True:
			#print abs(time.time()-self.lastChange)
			if abs(time.time()-self.lastChange)>self.waittime:
				print "UPDATE"
				keyValuePair=self.current_datasource.getKeyValue()
				print keyValuePair
				self.current_renderer.draw(keyValuePair)
				print self.current_datasource.title
				self.lastChange=time.time()

			time.sleep(2.0)
		