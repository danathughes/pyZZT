## board.py			Dana Hughes				25-Aug-2017
##
## Object representing an individual board in ZZT.


class Tile:
	"""
	Object to hold tile data
	"""

	def __init__(self, element, color):
		"""
		Create a tile of the provided element and color
		"""

		self.element = element
		self.color = color



class Board:
	"""
	Object representing an individual board in ZZT
	"""

	def __init__(self):
		"""
		Create a new Board
		"""

		# Name of the board
		self.name = "UNTITLED"

		# There are 60x25 tiles
		self.tiles = [None]*1500

		# Board properties
		self.exit = { 'north': 0,
		              'south': 0,
		              'west':  0,
		              'east':  0 }

		self.max_shots = 0
		self.is_dark = False		              
		self.restart_on_zap = False
		self.message = ""
		self.player_enter_x = 0
		self.player_enter_y = 0
		self.time_limit = 0

		# Objects on the board
		self.objects = []
