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

import os

def load(filename):
	"""
	Load a ZZT world file or save game
	"""

	# Does the filename exist?
	if not os.path.exists(filename):
		print "File %s does not exist", filename
		return None


	# Load the contents of the file
	with open(filename) as zztFile:
		zztData = zztFile.read()

	# Start a new world
	world = World()
	

