## world.py			Dana Hughes				25-Aug-2017
##
## Object representing a World in ZZT

from board import *

class World:
	"""
	Object representing a world in ZZT
	"""

	def __init__(self):
		"""
		Create a new World
		"""

		# Name of the world
		self.title = "UNTITLED"

		# Information on boards in the world
		self.num_boards = 0
		self.current_board = 0
		self.boards = []

		# Stuff the player has
		self.ammo = 0
		self.gems = 0
		self.health = 0
		self.torches = 0
		self.score = 0

		# Dictionary of keys the player has
		self.keys = { 'blue': 	False,
						  'green': 	False,
						  'cyan':	False,
						  'red':		False,
						  'purple':	False,
						  'yellow':	False,
						  'white':	False }

		# How much time remaining on torches and energizer
		# These will be relevant for saving a game
		self.torch_cycles = 0
		self.energizer_cycles = 0
		self.time_seconds = 0		# Seconds left on board
		self.time_ticks = 0			# Subseconds left on board

		# Currently existing flags
		self.flags = [None]*10



