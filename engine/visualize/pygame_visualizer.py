## pygame_visualizer.py			Dana Hughes				28-Aug-2017
##
## Visualization of the ZZT game using pygame.

import pygame
from pygame.locals import *

from character_set import *
from elements import *

BLACK = 0x00
DARK_BLUE = 0x01
DARK_GREEN = 0x02
DARK_CYAN = 0x03
DARK_RED = 0x04
DARK_PURPLE = 0x05
DARK_YELLOW = 0x06
LIGHT_GREY = 0x07
DARK_GREY = 0x08
LIGHT_BLUE = 0x09
LIGHT_GREEN = 0x0A
LIGHT_CYAN = 0x0B
LIGHT_RED = 0x0C
LIGHT_PURPLE = 0x0D
LIGHT_YELLOW = 0x0E
WHITE = 0x0F

colors = { BLACK: 		(0,0,0),
			  DARK_BLUE: 	(0,0,128),
			  DARK_GREEN: 	(0,128,0),
			  DARK_CYAN: 	(0,128,128),
			  DARK_RED:		(128,0,0),
			  DARK_PURPLE:	(128,0,128),
			  DARK_YELLOW:	(128,128,0),
			  LIGHT_GREY:	(192,192,192),
			  DARK_GREY:	(128,128,128),
			  LIGHT_BLUE:	(0,0,255),
			  LIGHT_GREEN:	(0,255,0),
			  LIGHT_CYAN:	(0,255,255),
			  LIGHT_RED:	(255,0,0),
			  LIGHT_PURPLE:(255,0,255),
			  LIGHT_YELLOW:(255,255,0),
			  WHITE:			(255,255,255)	
}

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

				char_num = tile.character
				char = self.characters[char_num]

				bg_color = colors[tile.bg_color]
				fg_color = colors[tile.fg_color]

				char.set_palette([bg_color,fg_color])

				self.screen.blit(char, screen_pos)


