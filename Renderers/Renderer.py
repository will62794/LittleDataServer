from SerialDraw import *

class Renderer(object):

	def __init__(self):
		#colorscale=[[grad_pts],[grad_colors]]
		self.colorscale=[]
		self.scaleMin=0
		self.scaleMax=100
		self.drawer=SerialDraw()
		self.drawer.WakeUpTeensy()

	
	def getScalePercentageForValue(self,value):
		offsetValue=abs(self.scaleMin-int(value))
		scaleSize=abs(self.scaleMax-self.scaleMin)
		percentageValue=float(offsetValue)/float(scaleSize)*100.0
		return percentageValue
	
	def getColorMix(self,minColor,maxColor,percentage):
		mixedColor=[]
		for i in range(3):
			difference=maxColor[i]-minColor[i]
			new_component=minColor[i]+((percentage)*difference)
			mixedColor.append(new_component)
		return mixedColor

	"""def getColorForValue(self,value):
		#custom gradient scale
		try:
			for i in range(1,len(self.colorscale[0])):
				grad_pts=self.colorscale[1]
				grad_colors=self.colorscale[0]
				percent=self.getScalePercentageForValue(value)
				if percent<grad_pts[i]:
					color1=grad_colors[i-1]
					color2=grad_colors[i]
					percentage=(float(value)-grad_pts[i-1])/(grad_pts
						[i]-grad_pts[i-1])
					return self.getColorMix(color1,color2,percentage)
 		except:
			return [255,255,255]"""

	def getColorForValue(self,value):
	#custom gradient scale
		#try:
		for i in range(1,len(self.colorscale[0])):
			grad_pts=[i*100.0/float(len(self.colorscale)-1) for i in range(len(self.colorscale))]
			grad_colors=self.colorscale
			percent=self.getScalePercentageForValue(value)
			if percent<grad_pts[i]:
				color1=grad_colors[i-1]
				color2=grad_colors[i]
				percentage=(float(value)-grad_pts[i-1])/(grad_pts[i]-grad_pts[i-1])
				return self.getColorMix(color1,color2,percentage)
		#except:
		#return [255,255,255]

			