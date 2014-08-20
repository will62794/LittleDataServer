import urllib
import json
import xml.etree.ElementTree as ET



class DataSource(object):
	"""Superclass for all types of data sources, which each communicate a different web API as needed. Data analysis tools are provided to those 
	subclasses by the DataSource parent class"""

	def __init__(self):
		pass
		
	def getDataFromUrl(self,url):
		data = urllib.urlopen(url).read()
		try:
			data=json.loads(data)
			return data
		except ValueError:
			pass
		try:
			return ET.fromstring(data)
			#return xmltree.getroot()
		except ValueError:
			pass

	def getKeyValue(self):
		pass
		#raise NotImplemenetedException












