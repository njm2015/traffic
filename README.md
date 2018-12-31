# traffic
Traffic control software


Objects:

Map -
	shape tuple
	road list
	intersection list
	car list

Vehicle -
	Position
	Speed
	Direction
	Destination
	Route

Direction - 
	number (0 - 360)

Destination -
	Position

Spawn - 
	Position
	Direction
	Speed

Route -
	(Intersection * Direction) list

Intersection -
	road tuple
	# stop light
	# stop sign tuple
	Stop tuple
	
Position - 
	(x * y)

Stop - 
	stoplight flag
	Stoplight

Stoplight - 
	programming