import csv
from DataSource import *
import datetime
import time

class Subway(DataSource):
	def __init__(self):
		super(Subway, self).__init__()
		self.options={"Route":"Q","Direction":"Northbound","Stop":"","Station":""}
		self.title="Subway"
		self.datafolder="DataSources/mtadata/"
		self.directionCode={"Northbound":"0","Southbound":"1"}
		self.weekdays=[0,1,2,3,4]
		self.saturday=5
		self.sunday=6
		self.icon="http://ihspawprint.com/wp-content/uploads/2014/03/mta_nyc_logo_svg1.png"
		self.renderers=["Subway"]

	def getColorForRoute(self,r):
		routes = csv.DictReader(open(self.datafolder+"routes.txt"))
		for route in routes:
			if route["route_id"]==r:
				return self.getRGBFromHex(route["route_color"])

	def getRGBFromHex(self,hexstring):
		rgbstr=hexstring
		return list(tuple(ord(c) for c in rgbstr.decode('hex')))

	def getAllStations(self):
		stations = csv.DictReader(open(self.datafolder+"stops.txt"))
		return stations
	def getAllTimes(self):
		stop_times= csv.DictReader(open(self.datafolder+"stop_times.txt"))
		return stop_times

	def getStationById(self,stop_id):
		stations=self.getAllStations();
		for station in stations:
			if stop_id in station["stop_id"]:
				return station


	def getStopsForTrip(self):
		trip_ids=[trip["trip_id"] for trip in self.getTrips()]
		stop_ids=[]
		for stop_time in self.getAllTimes():
			if stop_time["trip_id"] in trip_ids :
				if stop_time["stop_id"] not in stop_ids:
					stop_ids.append(stop_time["stop_id"])
		return stop_ids
			

	"""def TimesForStation(self):
		times=[]
		station=self.getStationById(self.options["Station"])
		for time in self.getTimes():
			print time["stop_id"]
			if time["stop_id"]==station:
				times.append(time["arrival_time"])

		return times"""



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


	def getTimesForStop(self):

		alltimes= csv.DictReader(open(self.datafolder+"stop_times.txt"))
		triptimes=[]
		trips=self.getTrips()
		trip_ids=[trip["trip_id"] for trip in trips]

		for time in alltimes:
			#Get times for a route and a specific station
			if time["trip_id"] in trip_ids and self.options["Station"] in time["stop_id"]:
				triptimes.append(time)
		return triptimes
	
	def getNextTrainTime(self):
		times=sorted([t["arrival_time"] for t in self.getTimesForStop()])
		time_now=self.convertClockToSeconds(self.getLocalTime())
		for t in times:
			if time_now<self.convertClockToSeconds(t):
				return t

	def TimeUntilNextTrain(self):
		localtime=self.convertClockToSeconds(self.getLocalTime())
		nextraintime=self.convertClockToSeconds(self.getNextTrainTime())
		secs=nextraintime-localtime
		print nextraintime
		print localtime
		return secs
		return str(datetime.timedelta(seconds=secs))


	def convertClockToSeconds(self,clockstring):
		ftr = [3600,60,1]
		return sum([a*b for a,b in zip(ftr, map(int,clockstring.split(':')))])

	def getLocalTime(self):
		return time.strftime("%H:%M:%S")
	

	def getKeyValue(self):
		route=self.options["Route"]
		return [route,self.TimeUntilNextTrain(),self.getColorForRoute(route)]

	def getDayCode(self):
		datetime.datetime.today()
		day=datetime.datetime.today().weekday()
		if day in self.weekdays:
			return "WKD"
		if day==self.saturday:
			return "SAT"
		if day==self.sunday:
			return "SUN"
"""
g=Subway()
g.options["Station"]="D40"
print g.TimeUntilNextTrain()
#print "Next "+g.options["Route"]+" Train: "+g.getNextTrainTime()
for stop in g.getStopsForTrip():
	print g.getStationById(stop)["stop_name"]

#for t in g.getTimesForStop():
	#print t["departure_time"]+" " +str(g.getStationById(t["stop_id"])["stop_name"])
	#print ""
	#pass
	#print t["stop_id"]
"""

