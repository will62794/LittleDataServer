import csv
from DataSource import *
import datetime

class Subway(DataSource):
	def __init__(self):
		super(Subway, self).__init__()
		self.options={"Route":"B","Direction":"Northbound","Stop":""}
		self.title="Subway"
		self.datafolder="mtadata/"
		self.directionCode={"Northbound":"0","Southbound":"1"}
		self.weekdays=[0,1,2,3,4]
		self.saturday=5
		self.sunday=6



	def getAllTrips(self):
		trips = csv.DictReader(open(self.datafolder+"trips.txt"))
		return trips

	def getTrips(self):
		route_trips=[]
		day=self.getDayCode()
		for trip in self.getAllTrips():
			if trip["route_id"]==self.options["Route"] and trip["direction_id"]==self.directionCode[self.options["Direction"]] and day in trip["service_id"]:
				route_trips.append(trip)	
		return route_trips


	def getTimes(self):

		alltimes= csv.DictReader(open(self.datafolder+"stop_times.txt"))
		triptimes=[]
		trips=self.getTrips()
		trip_ids=[trip["trip_id"] for trip in trips]

		for time in alltimes:
			if time["trip_id"] in trip_ids and "D17" in time["stop_id"]:
				triptimes.append(time)

		return triptimes
	
	def getKeyValue(self):
		pass

	def getDayCode(self):
		datetime.datetime.today()
		day=datetime.datetime.today().weekday()
		if day in self.weekdays:
			return "WKD"
		if day==self.saturday:
			return "SAT"
		if day==self.sunday:
			return "SUN"

g=Subway()

for t in g.getTrips():
	pass
	#print t	
for time in g.getTimes():
	#print time
	print time["arrival_time"]


