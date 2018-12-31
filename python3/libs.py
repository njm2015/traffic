# -- coding - utf-8 -- #
#
#	@author: NATHANIEL MURPHY
#

class Map(Object):

	def __init__(self, shape=(0,0), road_list=[], intersection_list=[],
						car_list=[]):
		self.shape = shape
		self.road_list = road_list
		self.intersection_list = intersection_list
		self.car_list = car_list

	def addRoad():
		pass

	def addIntersection():
		pass

	def addCar():
		pass


class Direction(Object):

	def __init__(self, direction):
		self.direction = direction


class Destination(Object):

	def __init__(self, position):
		self.position = position


class Spawn(Object):

	def __init__(self, position, direction, speed):
		self.position = position
		self.direction = direction
		self.speed = speed


class Route(Object):

	def __init__(self, turn_list=[]):
		self.turn_list = turn_list


class Vehicle(Object):

	def __init__(self, position=None, speed=None, direction=None, 
						destination=None, route=None):
		self.position = position
		self.speed = speed
		self.direction = direction
		self.destination = destination
		self.route = route

	def canMove():
		pass

	def moveOnePosition():
		pass