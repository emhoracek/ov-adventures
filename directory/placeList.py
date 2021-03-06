from flask import g
import dbqueries

class PlaceList (object):
  def __init__(self, selected):
    
#      if (selected == []):
#        cur = dbqueries.query_db(dbqueries.full_query)
#        self.list = [dict(name=row[0], 
#	                  description=row[1],
#	                  area=row[2],
#	         	  latitude=row[3],
#	          	  longitude=row[4]) for row in cur]
#      else:
        self.list = dbqueries.superQuery(selected)
      
  def length(self):
		return len(self.list)

  def shorten_place_list(self, page, pages):
		maxPlaces = page * pages
		startPlace = maxPlaces - pages
		places = self.list[startPlace : maxPlaces]
		return places
	
  def get_average_latlong(self, listPlaces):
    total_latitude = 0
    total_longitude = 0
    average_latitude = 0
    average_longitude = 0
    placeLength = len(listPlaces)
    for place in listPlaces:
      if (place['latitude'] and place['longitude']):
      	total_latitude = place['latitude'] + total_latitude
      	total_longitude = place['longitude'] + total_longitude
    if (placeLength == 0):
      average_latitude = 0
      average_longitude = 0
    else: 
      average_latitude=total_latitude/placeLength
      average_longitude=total_longitude/placeLength
    return { 'latitude': average_latitude,
      			 'longitude': average_longitude }

def getPlaceList (selected):
    if (selected == []):
      cur = dbqueries.query_db(dbqueries.full_query)
      return PlaceList(cur)
    else:
      cur = dbqueries.superQuery(selected)
      return PlaceList(cur)
