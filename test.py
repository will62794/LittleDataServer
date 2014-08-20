import time
import threading
from threading import Thread
import random


from DataSources import Weather
from DataSources import Asana

#datacontroller=DataController.DataController()
#datacontroller.start()
#datacontroller.running=True


weather=Weather.Weather()
weather.options["Random World City"]=True
weather.options["Cities"]=["Chicago","Atlanta","Boston","New York","Milan"]

asana=Asana.AsanaAPI()
asana.options["Randomize"]=False
print asana.getKeyValue()




		#custom gradient scale
"""		g0=[0,0,0]
		g1=[174,196,221]
		g2=[168,207,56]
		g3=[168,34,34]

		grad_colors=[g0,g1,g2,g3]
		grad_pts=[0.0,49.89,73.99,100.0]"""
"""
for i in range(30):
	weatherpair=weather.getKeyValue(weather.getKeyValue(weather.chooseCity()))
	print weatherpair
	magcolorbarRender.colorscale=([[0,0,0],[174,196,221],[168,207,56],[168,34,34]],[0.0,49.89,73.99,100.0])
	magcolorbarRender.draw(weatherpair[0],weatherpair[1])
	time.sleep(0.3)
"""

