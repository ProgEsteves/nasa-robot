# -*- coding: utf-8 -*-

from enum import Enum
from flask import abort, json

class OutOfBoundException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr("Out of bound")

### Class enumerator to Orientation
### W to West
### N to North
### E to East
### S to South
class Orientation(Enum):
	__order__ = 'W N E S'
	W = 1
	N = 2
	E = 3
	S = 4

	### Change orientation rotation to right
	def right(self):
		v = self.value+1
		if v > 4:
			v=1
		return Orientation(v)

	### Change orientation rotation to left
	def left(self):
		v = self.value-1
		if v == 0:
			v=4
		return Orientation(v)

### Class enumerator to Command
### L to Left
### R to Right
### M to Move
class Command(Enum):
	L = 'L'
	R = 'R'
	M = 'M'

### Point class, determine a point... Can be x or y in navigation
class Point(object):
	def __init__(self, value=0):
		self.__point = value

	@property
	def get(self):
		return self.__point

	@get.setter
	def set(self, value):
		self.__point = value

	def add(self, val):
		self.__point = self.__point + val

	def sub(self, val):
		self.__point = self.__point - val

### Position class, determina axis x and y
class Position(object):
	def __init__(self):
		self.x = Point()
		self.y = Point()

### Terrain class, to determine size of ground
class Terrain(object):
	def __init__(self):
		self.x = Point(5);
		self.y = Point(5);

	### test limits of terrain
	def testLimits(self, x, y):
		if (x.get > self.x.get) or (x.get < 0):
			raise OutOfBoundException()
		if (y.get > self.y.get) or (y.get < 0):
			raise OutOfBoundException()

### Robot class, determine control to robot
class Robot(object):
	def __init__(self, path):
		self.position = Position()
		self.orientation = Orientation.N
		terrain = Terrain()
		try:
			### Get step by step in path command
			for cmd in path:
				self.move(Command(cmd))
				terrain.testLimits(self.position.x, self.position.y)
		except:
			return abort(400, 'Bad Request')

	@property
	def orientation(self):
		return self.__orientation

	@orientation.setter
	def orientation(self, value):
		self.__orientation = value

	### Function to return actual location in mars
	### x to axis x
	### y to axis y
	### d to direction
	### return text format
	def getLocationText(self):
		data = "({},{},{})".format(
			self.position.x.get,
			self.position.y.get,
			self.orientation.name
		)
		return data

	### Function to return actual location in mars
	### x to axis x
	### y to axis y
	### d to direction
	### return json format
	def getLocation(self):
		data = {
			'x' : self.position.x.get,
			'y' : self.position.y.get,
			'd' : self.orientation.name
		}
		return json.dumps(data)

	### move command using enum class to determine what to do
	def move(self, cmd):
		if(cmd in Command):
			options = {
				Command.L : self.goLeft,
				Command.R : self.goRight,
				Command.M : self.doStep
			}
			options[cmd]()
		else:
			raise Exception()

	### move on ground step by step to direction on orientation
	def doStep(self):
		options = {
			Orientation.S : self.goSouth,
			Orientation.N : self.goNorth,
			Orientation.W : self.goWest,
			Orientation.E : self.goEast
		}
		options[self.orientation]()

    ### change orientation to left
	def goLeft(self):
		self.orientation = self.orientation.left()

    ### change orientation to right
	def goRight(self):
		self.orientation = self.orientation.right()

	### do step(s) in north direction
	def goNorth(self, steps=1):
		self.position.y.add(steps);

	### do step(s) in east direction
	def goEast(self, steps=1):
		self.position.x.add(steps);

	### do step(s) in south direction
	def goSouth(self, steps=1):
		self.position.y.sub(steps);

	### do step(s) in wast direction
	def goWest(self, steps=1):
		self.position.x.sub(steps);

### Test
if __name__ == '__main__':
	r = Robot('MMRMMRMM')
	print(r.getLocation())
