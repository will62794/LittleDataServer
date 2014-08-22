from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

#from src import main
#from src import DataController

#HELLOWORLD

##GIT TESTING ON

from DataUpdater import *

app = Flask(__name__)



@app.route('/')
def index():
	try:
		app.dataUpdater.start()
	except:
		pass
	return render_template('home.html',dataSources=app.dataUpdater.datasources,current_datasource=app.dataUpdater.current_datasource,renderers=app.dataUpdater.renderers,current_renderer=app.dataUpdater.current_renderer)
	

@app.route('/datasource/<datasource>')
def set_data_source(datasource):
# show the user profile for that user
	if datasource=="Colors":
		app.dataUpdater.waittime=1
	else:
		app.dataUpdater.waittime=9

	app.dataUpdater.current_datasource=app.dataUpdater.datasources[datasource]
	renderer=app.dataUpdater.current_datasource.renderers[0]
	app.dataUpdater.current_renderer=app.dataUpdater.renderers[renderer]
	#Use default data source color scale if there is one
	
	try:
		app.dataUpdater.current_renderer.colorscale=app.dataUpdater.current_datasource.defaultColorscale
	except:
		pass
	try:
		if app.dataUpdater.current_datasource.defaultMin:
			app.dataUpdater.current_renderer.scaleMin=app.dataUpdater.current_datasource.defaultMin
		if app.dataUpdater.current_datasource.defaultMax:
			app.dataUpdater.current_renderer.scaleMax=app.dataUpdater.current_datasource.defaultMax
	except:
		pass


	print "DataSource: "+app.dataUpdater.current_datasource.title
	print "Renderer: "+app.dataUpdater.current_renderer.title

	return redirect("/")
	
@app.route('/startup')
def startup():
	return redirect("/")

@app.route('/test')
def test():
	return render_template("test.html")

@app.route('/updateDataSource',methods=['GET', 'POST'])
def updateDataSource():
	app.dataUpdater.current_renderer.drawer.glowMode("off")
	optionsDict=dict(request.form)
	print optionsDict
	for option in optionsDict.keys():
		print optionsDict[option][0]
		if optionsDict[option][0].lower().strip()=="on":
			app.dataUpdater.current_datasource.options[option]=True
		elif optionsDict[option][0].lower().strip()=="off":
			app.dataUpdater.current_datasource.options[option]=False
			print app.dataUpdater.current_datasource.options
		elif isinstance(optionsDict[option],list):
			optionsDict[option]=[el for el in optionsDict[option] if el]
			app.dataUpdater.current_datasource.options[option]=optionsDict[option]

	return redirect("/")

@app.route('/brightness',methods=['GET', 'POST'])
def setBrightness():
	optionsDict=dict(request.form)
	b=optionsDict["brightnessValue"]
	app.dataUpdater.current_renderer.brightness=b[0]
	app.dataUpdater.current_renderer.setBrightness()
	return redirect("/")

@app.route('/updateColorOptions',methods=['GET', 'POST'])
def updateColorOptions():
	optionsDict=dict(request.form)
	print optionsDict
	for option in optionsDict.keys():
		try:
			app.dataUpdater.current_renderer.coloroptions[option]=optionsDict[option]
		except:
			pass

	return redirect("/")


@app.route('/addColorscalePoint')
def addColorscalePoint():
	#add new neutral(gray) gradient point
	app.dataUpdater.current_renderer.colorscale.append([128,128,128])
	return redirect("/")

@app.route('/deleteColorscalePoint')
def deleteColorscalePoint():
	app.dataUpdater.current_renderer.colorscale.pop()
	return redirect("/")

@app.route('/updateRenderer',methods=['GET', 'POST'])
def updateRenderer():
	values=dict(request.form)
	app.dataUpdater.current_renderer.scaleMin=int(values["scaleMin"][0])
	app.dataUpdater.current_renderer.scaleMax=int(values["scaleMax"][0])

	for i in range(len(app.dataUpdater.current_renderer.colorscale)):
		app.dataUpdater.current_renderer.colorscale[i]=[int(comp) for comp in values["color"+str(i)]]
	return redirect("/")


@app.context_processor
def utility_processor():
	def convert_option(value):
		if isinstance(value, list):
			return "list"
		if isinstance(value, bool):
			return "bool"
		if isinstance(value, str):
			return "str"
	return dict(convert_option=convert_option)

app.dataUpdater=DataUpdater()

if __name__ == '__main__':
	set_data_source("Weather")
	app.run(host='0.0.0.0',debug=True)







