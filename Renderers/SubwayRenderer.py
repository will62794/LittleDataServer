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
		color=keyValuePair[2]

		#percentage=self.getScalePercentageForValue(value)
		#colorForValue=self.getColorForValue(value)
		
		
		self.drawer.barNum=0
		self.drawer.clearDrawBuffer()
		self.drawer.drawCircle(7,54,7,[255,255,0])
		self.drawer.drawRectangle(0,0,16,10,[200,200,200])
		self.drawer.drawTriangle(0,10,8,15,16,10,[200,200,200])

		self.drawer.drawChar(5,54,[0,0,0],"6x10","Q")
		self.drawer.bufferswap("false")
		#self.drawer.clearDrawBuffer()
		#self.drawer.drawBarWithValue(colorForValue,str(percentage))
		#self.drawer.drawVerticalString(2,value,[0,0,0],"6x10")
		#self.drawer.transition("slide")
		#self.drawer.bufferswap("false")
		#except:
		#	pass




		