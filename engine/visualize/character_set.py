## character_set.py			Dana Hughes				28-Aug-2017
##
## Functions for loading in a character set

import pygame
from pygame.locals import *

import os

def load_bitmap(filename, dimensions=(8,16)):
	"""
	Load in the characters from a bitmap.

	NOTE:  Currently assumes a 2-bit (BW) bitmap.

	filename   - path to the bitmap file
	dimensions - width x height of individual character in bitmap
	"""

	# Does the file exist?
	if not os.path.exists(filename):
		print "File %s does not exist!" % filename
		return None

	with open(filename) as bitmap_file:
		bitmap = pygame.image.load(bitmap_file)

	# Extract the characters
	characters = []

	# How many characters across and down in the image?
	char_width, char_height = dimensions
	num_x = bitmap.get_width()/ char_width
	num_y = bitmap.get_height() / char_height

	# Convert the surface to a bit array for easy extraction.  Any non-zero bit
	# should be set to 1.
	bit_array = pygame.surfarray.array2d(bitmap)
	bit_array[bit_array > 0] = 1

	# Extract the characters
	for i in range(num_x):
		x = i*char_width

		for j in range(num_y):
			y = j*char_height

			char = pygame.surfarray.make_surface(bit_array[x:x+char_width,y:y+char_height])
			characters.append(char)

	return characters



