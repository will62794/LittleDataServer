import SerialDraw
from Renderer import *
import random

class ColorsRenderer(Renderer):
	def __init__(self):
		super(ColorsRenderer, self).__init__()
		self.title="ColorBar"
		self.description=""
		self.colorscale=[[139,68,254],[255,10,50],[155,20,50]]
		self.options={"RandomizeColors":False}
		self.coloroptions={"Bar1_ColorA":[100,0,0],"Bar1_ColorB":[0,152,140],"Bar2_ColorA":[0,100,0],"Bar2_ColorB":[0,0,100],"Bar3_ColorA":[0,100,50],"Bar3_ColorB":[40,40,40]}

	def draw(self,keyValuePair):		
		self.drawer.clearDrawBuffer()

		self.drawer.barNum=0
		self.drawer.clearDrawBuffer()
		self.drawer.drawGradientRectangle(0,0,16,64,self.coloroptions["Bar1_ColorA"],self.coloroptions["Bar1_ColorB"])
		self.drawer.bufferswap("false")

		self.drawer.barNum=1
		self.drawer.clearDrawBuffer()
		self.drawer.drawGradientRectangle(0,0,16,64,self.coloroptions["Bar2_ColorA"],self.coloroptions["Bar2_ColorB"])
		self.drawer.bufferswap("false")

		self.drawer.barNum=2
		self.drawer.clearDrawBuffer()
		self.drawer.drawGradientRectangle(0,0,16,64,self.coloroptions["Bar3_ColorA"],self.coloroptions["Bar3_ColorB"])
		self.drawer.bufferswap("false")





		