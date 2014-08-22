import SerialDraw
from Renderer import *
import random

class SubwayRenderer(Renderer):
	def __init__(self):
		super(SubwayRenderer, self).__init__()
		self.title="Subway"
		self.description="Shows when your next train is coming!"
		self.options={}

	def draw(self,keyValuePair):
		#Key is the train line
		#Value is the time till next train
		#Color is the color of the train line

		key=keyValuePair[0]
		value=keyValuePair[1]
		try:
			routecolor=keyValuePair[2]
		except:
			routecolor=[200,200,200]

		routename=key
		#percentage=self.getScalePercentageForValue(value)
		#colorForValue=self.getColorForValue(value)
		
		if value>10:
			value=10

		pixelheight=42-int(value*4.2)

		c=self.getColorMix([255,255,255],[255,0,0],1.0-float(value)/10)
		
		self.drawer.barNum=0
		self.drawer.clearDrawBuffer()
		self.drawer.drawCircle(7,55,7,routecolor)
		self.drawer.drawRectangle(0,0,16,pixelheight,c)
		self.drawer.drawTriangle(0,pixelheight,8,pixelheight+5,16,pixelheight,c)
		self.drawer.drawChar(5,51,[0,0,0],"6x10",routename)
		self.drawer.bufferswap("false")


		self.drawer.barNum=1
		self.drawer.clearDrawBuffer()
		self.drawer.bufferswap("false")
		self.drawer.barNum=2
		self.drawer.clearDrawBuffer()
		self.drawer.bufferswap("false")





		