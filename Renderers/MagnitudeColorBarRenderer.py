import SerialDraw
from Renderer import *
import random

class MagnitudeColorBarRenderer(Renderer):
	def __init__(self):
		super(MagnitudeColorBarRenderer, self).__init__()
		self.title="MagnitudeColorBar"
		self.description="The MagnitudeColorBar Renderer renderer takes a key and a value, a Colorscale, and a max and min value for the data values and draws a bar of a certain color and height."
		self.colorscale=[[139,68,254],[255,10,50],[155,20,50]]
		self.options={}

	def draw(self,key,value):
		percentage=self.getScalePercentageForValue(value)
		colorForValue=self.getColorForValue(value)
		print colorForValue
		try:
			self.drawer.barNum=random.choice(range(0,3))
			self.drawer.clearDrawBuffer()
			self.drawer.drawBarWithKeyValue(str(key),str(percentage),colorForValue)
			self.drawer.transition("slide")
			#self.drawer.bufferswap("false")
		except:
			pass




		