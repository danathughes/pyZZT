## pygame_visualizer.py			Dana Hughes				28-Aug-2017
##
## Visualization of the ZZT game using pygame.

import pygame
from pygame.locals import *

from character_set import *
from elements import *



class PygameVisualizer:
	"""
	Visualization class using pygame
	"""

	def __init__(self):
		"""
		Create a new screen, etc
		"""

		pygame.init()

		self.screen = pygame.display.set_mode((480,400))
		self.characters = load_bitmap('engine/visualize/sans_8x16.bmp')


	def draw_board(self, board):
		"""
		Draw all the tiles in the board
		"""

		for i in range(25):
			for j in range(60):

				tile = board.tiles[i*60+j]
				screen_pos = (j*8, i*16)

				char_num = character_map[tile.element]
				char = self.characters[char_num]
				char.set_palette([(0,0,0),(255,255,255)])

				self.screen.blit(char, screen_pos)


