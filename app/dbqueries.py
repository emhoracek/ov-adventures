from flask import g

# This module contains the functions for querying the database

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

query_activities = ('select places.name, places.description, areas.name ' +
		   'FROM places JOIN ? as "a" ' +
		   'ON places.id = a.placeId ' +
		   'order by places.name')

def get_activities_list():
	cur = query_db('select name from activities order by name')
	return [dict(name=row[0]) for row in cur]

full_query = ('select places.name, places.description, ' +
	      'areas.name, places.latitude, places.longitude ' +
	      'FROM places JOIN areas ' +
	      'ON places.areaId = areas.id '
	      'order by places.name')


query_join = (' select places.name, places.description, areas.name, '+
	      ' places.latitude, places.longitude ' +
	      ' FROM places, areas JOIN joinActPlace, activities ' +
	      ' ON places.id = joinActPlace.placeId AND ' +
	      ' activities.id = joinActPlace.activityId ' +  
	      ' where activities.name = ? AND areas.id = places.areaId')