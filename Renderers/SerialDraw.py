import time
import serial


class SerialDraw():
	def __init__(self):
		pass

	def WakeUpTeensy(self):
		self.ledPorts=["/dev/ttyACM0","/dev/ttyACM1","/dev/ttyACM2"]
		self.barNum=0
		try:
			led1 = serial.Serial(self.ledPorts[0], 38400, timeout=1)
			led2 = serial.Serial(self.ledPorts[1], 38400, timeout=1)
			led3 = serial.Serial(self.ledPorts[2], 38400, timeout=1)
			self.serPorts=[led1,led2,led3]


			cmd="start\n"
			time.sleep(3.0)
			self.serPorts[self.barNum].write(cmd)
			return True
		except:
			return False

	def bufferswap(self,copy):
		cmd="bufferswap "+copy+"\n"
		time.sleep(.005)
		self.serPorts[self.barNum].write(cmd)

	def transition(self,transition,fadetime=0):
		if transition=="fade":
			cmd="transition fade "+str(fadetime)+"\n"
		else:
			cmd="transition "+transition+"\n"
		time.sleep(.005)
		self.serPorts[self.barNum].write(cmd)

	def clearDrawBuffer(self):
		cmd="cleardrawbuffer \n"
		time.sleep(.005)
		#print cmd
		self.serPorts[self.barNum].write(cmd)
	
	def drawCircle(self,x,y,r,color):
		cmd="circle %s %s %s %s %s %s %s %s %s \n" % (str(x),str(y),int(r),color[0],color[1],color[2],color[0],color[1],color[2])
		time.sleep(.005)
		self.serPorts[self.barNum].write(cmd)

	def drawTriangle(self,x1,y1,x2,y2,x3,y3,color):
		cmd="triangle %s %s %s %s %s %s %s %s %s %s %s %s\n" % (str(x1),str(y1),str(x2),str(y2),str(x3),str(y3),color[0],color[1],color[2],color[0],color[1],color[2])
		time.sleep(.005)
		self.serPorts[self.barNum].write(cmd)

	def drawRectangle(self,x,y,w,h,color):
		cmd="rect %s %s %s %s %s %s %s \n" % (str(x),str(y),int(w),str(h),color[0],color[1],color[2])
		time.sleep(.005)
		self.serPorts[self.barNum].write(cmd)

	def drawGradientRectangle(self,x,y,w,h,color1,color2):
		cmd="gradrect %s %s %s %s %s %s %s %s %s %s\n" % (str(x),str(y),int(w),str(h),color1[0],color1[1],color1[2],color2[0],color2[1],color2[2])
		time.sleep(.005)
		self.serPorts[self.barNum].write(cmd)

	def drawChar(self,x,y,color,font,letter):
		cmd="char %s %s %s %s %s %s %s \n" % (str(x),str(y),color[0],color[1],color[2],font,letter)
		time.sleep(.005)
		self.serPorts[self.barNum].write(cmd)

	def drawVerticalString(self,x,text,color,font):
		i=0;
		offset=8
		for letter in text:
			self.drawChar(x,i*offset,color,font,letter)
			i+=1


	def drawCenteredValue(self,value,y,color,font):
		xoffset=0
		if font=="8x13":
			xoffset=0
		else:
			xoffset=2;
		if len(value)==1:
			self.drawChar(xoffset+4,y,color,font,value[0])
		if len(value)==2:
			self.drawChar(xoffset+0,y,color,font,value[0])
			self.drawChar(xoffset+7,y,color,font,value[1])

	##Takes Percentage Integer Value (0-100)
	def drawBarWithValue(self,color,value):
		barHeight=int(64*float(value)/100)
		self.drawRectangle(0,64-barHeight,16,64,color)
		self.drawCenteredValue(str(value),50,[0,0,0],"8x13")
	
	def drawBarWithKeyValue(self,key,value,color):
		barHeight=int(64*float(value)/100)
		self.drawRectangle(0,64-barHeight,16,64,color)
		self.drawCenteredValue(str(value)[:2],50,[0,0,0],"8x13")
		if len(key)>0:
			ypos=1
			spacing=11
			self.drawVerticalString(key[:3].upper(),[40,40,40],"8x13")

	def drawGradientBarWithValue(self,color1,color2,value,label=""):
		barHeight=int(64*float(value)/100)
		self.drawGradientRectangle(0,64-barHeight,16,64,color1,color2)
		self.drawCenteredValue(value,50,[0,0,0],"8x13")
		if len(label)>0:
			ypos=1
			spacing=11
			self.drawCenteredValue(label.upper(),ypos,[150,150,150],"5x7")







"""
while True:
	temp=Weatherman().getTemperature("New York")
	color=Weatherman().getColorForTemperature(temp)
	color=[214,100,17]
	drawBarWithValue(color,"78")
	redraw()
	time.sleep(1)
"""

	#drawRectangle(0,0,16,temp,color)

	#drawChar(0,50,[0,0,0],"8x13",temp[0])
	#drawChar(8,50,[0,0,0],"8x13",temp[1])

"""
	# see your workspaces
	myspaces = asana_api.list_workspaces()  #Result: [{u'id': 123456789, u'name': u'asanapy'}]
	workspace_id=myspaces[0]["id"]
	all_projects = asana_api.lists_projects(workspace=workspace_id,include_archived=False)  #Result: [{u'id': 123456789, u'name': u'asanapy'}]
	project_tasks=asana_api.get_project_tasks(all_projects[1]["id"],include_archived=False)
	print all_projects[1]["name"]
	print len(project_tasks)

	drawChar(0,50,[0,120,120],"8x13",str(len(project_tasks))[0])
	drawChar(8,50,[0,120,120],"8x13",str(len(project_tasks))[1])

"""

	#time.sleep(.10)





