import SerialDraw
from Renderer import *
import random

class ColorBarRenderer(Renderer):
	def __init__(self):
		super(ColorBarRenderer, self).__init__()
		self.title="ColorBar"
		self.description="The MagnitudeColorBar Renderer renderer takes a key and a value, a Colorscale, and a max and min value for the data values and draws a bar of a certain color and height."
		self.colorscale=[[139,68,254],[255,10,50],[155,20,50]]
		self.options={"RandomizeColors":False}
		self.coloroptions={"TextColor":[0,0,0],"BackgroundColor":[0,152,140]}

	def draw(self,keyValuePair):
		key=keyValuePair[0]
		value=keyValuePair[1]
		percentage=self.getScalePercentageForValue(value)
		colorForValue=self.getColorForValue(value)
		
		self.drawer.barNum=random.choice(range(0,3))
		self.drawer.clearDrawBuffer()
		
		if self.options["RandomizeColors"]:
			textcolor=[random.randint(50,100),random.randint(200,250),random.randint(200,250)]
			backgroundcolor=[random.randint(200,250),random.randint(50,100),random.randint(50,100)]
		else:
			textcolor=self.options["TextColor"]
			backgroundColor=self.options["BackgroundColor"]

		self.drawer.drawRectangle(0,0,16,64,backgroundcolor)

		self.drawer.drawCenteredValue(str(value)[:2],50,[0,0,0],"8x13")
		
		self.drawer.drawVerticalString(2,key.strip().upper()[:6],textcolor,"6x10")
		self.drawer.transition("slide")





		