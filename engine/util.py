## util.py			Dana Hughes				25-Aug-2017
##
## Utility functions for pyZZT.  Includes the following functions:
##
## load - Load a ZZT (world) file (or save game)
## save - Save a ZZT (world) file (or save game)
## loadBoard - Load a BRD (board) file
## saveBoard - Save a BRD (board) file

from world import *
from board import *
from elements import *

import os

def readByte(data, index):
	"""
	Read a byte and convert to integer
	"""

	return ord(data[index])


def readWord(data, index):
	"""
	Read two bytes from the data and return an integer.
	"""

	# Note that the data is little-endian (Intel style), so the first byte
	# is the least significant

	return 256*ord(data[index+1]) + ord(data[index])


def readLong(data, index):
	"""
	Read four bytes from the data and return an integer.
	"""

	# Note that the data is little-endian (Intel style), so the first byte
	# is the least significant

	return 16777216*ord(data[index+3]) + 65536*ord(data[index+2]) + 256*ord(data[index+1]) + ord(data[index])


def extractBoard(data):
	"""
	Extract a board from the data
	"""

	# Create a board object to load the data into
	board = Board()

	# Name of the board
	name_length = readByte(data, 0x02)
	board.name = data[0x03:0x03+name_length]

	# Extract the tile data.  This is run-length encoded, so need to keep track
	# of tile numbers and properly create stuff
	cur_tile_idx = 0
	cur_rle_idx = 0x35		# Start of the RLE tile data

	# There's a total of 60x25 (1500) tiles
	while cur_tile_idx < 1500:
		# Get the RLE data
		num_tiles = readByte(data, cur_rle_idx)
		element = readByte(data, cur_rle_idx+1)
		color = readByte(data, cur_rle_idx+2)

		# odd quirk:  if num_tiles is 0, then it's actually 256 tiles
		if num_tiles == 0:
			num_tiles = 256

		# Determine the foreground and background colors
		bg_color = int(color / 16) % 8
		fg_color = color % 16


		# Create the appropriate number of tiles
		for i in range(cur_tile_idx, cur_tile_idx+num_tiles):
			#board.tiles[i] = Tile(element, color)
			board.tiles[i] = zztElementList[element](fg_color, bg_color)

		cur_tile_idx += num_tiles
		cur_rle_idx += 3


	# Board properties follow the RLE data
	data = data[cur_rle_idx:]		# Start the current data from the end of the RLE data

	board.max_shots = readByte(data, 0x00)
	board.is_dark = readByte(data, 0x01) != 0
	board.restart_on_zap = readByte(data, 0x06) != 0
	
	board.exit['north'] = readByte(data, 0x02)
	board.exit['south'] = readByte(data, 0x03)
	board.exit['west']  = readByte(data, 0x04)
	board.exit['east']  = readByte(data, 0x05)

	message_length = readByte(data, 0x07)
	board.message = data[0x08:0x08+message_length]

	board.player_enter_x = readByte(data, 0x42)
	board.player_enter_y = readByte(data, 0x43)
	board.time_limit = readWord(data, 0x44)

	num_objects = readWord(data, 0x56)

	print "Number of objects", objects

	# Load the player
	player, next_addr = extractObject(data[0x58:])

	return board


def extractObject(data):
	"""
	Extract the object from the data, starting at the provided address
	"""

	# Store all the relevant information in a dictionary
	object_info = {}

	# Get x, y and velocity info
	object_info['x'] = readByte(data, 0x00)
	object_info['y'] = readByte(data, 0x01)
	object_info['step_x'] = readWord(data, 0x02)
	object_info['step_y'] = readWord(data, 0x04)
	object_info['cycle'] = readWord(data, 0x06)

	# Object parameters
	object_info['P1'] = readByte(data, 0x08)
	object_info['P2'] = readByte(data, 0x09)
	object_info['P3'] = readByte(data, 0x0A)

	# For linking centipedes, etc
	object_info['follower'] = readWord(data, 0x0B)
	object_info['leader'] = readWord(data, 0x0D)

	# What is under the object?
	object_info['under_id'] = readByte(data, 0x0F)
	object_info['under_color'] = readByte(data, 0x10)

	# Object code
	object_info['pointer'] = readLong(data, 0x11)
	object_info['current_instruction'] = readWord(data, 0x15)

	# Length of the information, or what object to copy this from
	object_info['length'] = readWord(data, 0x17)

	# Is there code?
	




def load(filename):
	"""
	Load a ZZT world file or save game
	"""

	# Does the filename exist?
	if not os.path.exists(filename):
		print "File %s does not exist", filename
		return None


	# Load the contents of the file
	with open(filename, 'rb') as zztFile:
		zztData = zztFile.read()

	# Is this a valid world file?  The first two bytes should be 0xFFFF
	if readWord(zztData, 0x00) != 0xFFFF:
		print "Not a valid ZZT world file"
		return None


	# Start a new world
	world = World()


	# Process the world header
	world.num_boards = readWord(zztData, 0x02)
	world.boards = [None]*world.num_boards

	world.ammo = readWord(zztData, 0x04)
	world.gems = readWord(zztData, 0x06)
	world.health = readWord(zztData, 0x0F)
	world.torches = readWord(zztData, 0x13)
	world.score = readWord(zztData, 0x1B)

	world.keys['blue']   = readByte(zztData, 0x08) != 0
	world.keys['green']  = readByte(zztData, 0x09) != 0
	world.keys['cyan']   = readByte(zztData, 0x0A) != 0
	world.keys['red']    = readByte(zztData, 0x0B) != 0
	world.keys['purple'] = readByte(zztData, 0x0C) != 0
	world.keys['yellow'] = readByte(zztData, 0x0D) != 0
	world.keys['white']  = readByte(zztData, 0x0E) != 0

	world.current_board = readWord(zztData, 0x13)
	world.torch_cycles = readWord(zztData, 0x15)
	world.energizer_cycles = readWord(zztData, 0x17)
	world.time_seconds = readWord(zztData, 0x104)
	world.time_ticks = readWord(zztData, 0x106)

	title_length = readByte(zztData, 0x1D)
	world.title = zztData[0x1E:0X1E+title_length]

	# Read the flags, if present
	for i in range(10):
		addr = 0x32 + i*0x15
		flag_length = readByte(zztData, addr)
		if flag_length > 0:
			world.flags[i] = zztData[addr+1:addr+1+flag_length]


	# Read in all the boards, and store in the world
	# Boards start at index 200
	board_idx = 0x200

	for i in range(world.num_boards):
		# The board size doesn't include the two bytes for the size
		board_size = readWord(zztData, board_idx) + 2
		world.boards[i] = extractBoard(zztData[board_idx:board_idx + board_size])
		board_idx += board_size


	return world


	

