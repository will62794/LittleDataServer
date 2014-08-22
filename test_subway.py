from DataSources import Subway


g=Subway.Subway()
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