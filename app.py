from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

#from src import main
#from src import DataController

#HELLOWORLD

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
	print "DataSource: "+datasource
	app.dataUpdater.current_datasource=app.dataUpdater.datasources[datasource]
	return redirect("/")
	
@app.route('/startup')
def startup():
	return redirect("/")

@app.route('/updateDataSource',methods=['GET', 'POST'])
def updateDataSource():
	optionsDict=dict(request.form)
	print request.stream
	print optionsDict
	for option in optionsDict.keys():
		if optionsDict[option][0]=="on":
			app.dataUpdater.current_datasource.options[option]=True
		elif optionsDict[option][0]=="off":
			app.dataUpdater.current_datasource.options[option]=False
		elif isinstance(optionsDict[option],list):
			optionsDict[option]=[el for el in optionsDict[option] if el]
			app.dataUpdater.current_datasource.options[option]=optionsDict[option]
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
	return dict(convert_option=convert_option)

app.dataUpdater=DataUpdater()

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)






