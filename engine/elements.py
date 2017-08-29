## elements.py			Dana Hughes				28-Aug-2017
##
## Elements used in ZZT, such as board tiles, player, enemies, etc.

# Color Codes
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


class Empty():
	"""
	Empty Element
	"""

	def __init__(self, fg_color = None, bg_color = None):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x00
		self.name = "Empty"
		self.character = 0x20
		self.color = 0x70
		self.destructable = False
		self.pushable = True
		self.editor_floor = False
		self.floor = True
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x0010
		self.menu_number = 0
		self.key = None
		self.internal_name = "Empty"
		self.category = None
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = LIGHT_GREY
		self.fg_color = BLACK
		self.blinking = False



class BoardEdge():
	"""
	Empty Element
	"""

	def __init__(self, fg_color = None, bg_color = None):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x01
		self.name = "Board Edge"
		self.character = 0x20
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x3973
		self.menu_number = 0
		self.key = None
		self.internal_name = None
		self.category = None
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = LIGHT_GREY
		self.fg_color = WHITE
		self.blinking = True


class Messenger():
	"""
	Empty Element
	"""

	def __init__(self, fg_color = None, bg_color = None):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x02
		self.name = "Messenger"
		self.character = 0x20
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0039
		self.interact_code = 0x0010
		self.menu_number = 0
		self.key = None
		self.internal_name = None
		self.category = None
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = LIGHT_GREY
		self.fg_color = WHITE
		self.blinking = True



class Monitor():
	"""
	Empty Element
	"""

	def __init__(self, fg_color = None, bg_color = None):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x03
		self.name = "Monitor"
		self.character = 0x20
		self.color = 0x07
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = 1
		self.act_code = 0x4481
		self.interact_code = 0x0010
		self.menu_number = 0
		self.key = None
		self.internal_name = "Monitor"
		self.category = None
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = LIGHT_GREY
		self.blinking = FALSE


class Player():
	"""
	Player Element
	"""

	def __init__(self, fg_color = None, bg_color = None):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x04
		self.name = "Player"
		self.character = 0x02
		self.color = 0x1F
		self.destructable = True
		self.pushable = True
		self.editor_floor = False
		self.floor = False
		self.shown = True
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = 1
		self.act_code = 0x3E2F
		self.interact_code = 0x0010
		self.menu_number = 1
		self.key = 'Z'
		self.internal_name = "Player"
		self.category = "Items"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = DARK_BLUE
		self.fg_color = WHITE
		self.blinking = False


class Ammo():
	"""
	Ammo Element
	"""

	def __init__(self, fg_color = None, bg_color = None):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x05
		self.name = "Ammo"
		self.character = 0x84
		self.color = 0x03
		self.destructable = False
		self.pushable = True
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x3289
		self.menu_number = 1
		self.key = 'A'
		self.internal_name = "Ammo"
		self.category = "Items"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = DARK_CYAN
		self.blinking = False

class Torch():
	"""
	Torch Element
	"""

	def __init__(self, fg_color = None, bg_color = None):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x06
		self.name = "Torch"
		self.character = 0x9D
		self.color = 0x06
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = True
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = 1
		self.act_code = 0x0000
		self.interact_code = 0x37B6
		self.menu_number = 1
		self.key = 'T'
		self.internal_name = "Torch"
		self.category = "Items"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = DARK_YELLOW
		self.blinking = False


class Gem():
	"""
	Gem Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x07
		self.name = "Gem"
		self.character = 0x04
		self.color = 0xFF
		self.destructable = True
		self.pushable = True
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x3306
		self.menu_number = 1
		self.key = 'G'
		self.internal_name = "Gem"
		self.category = "Items"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class Key():
	"""
	Gem Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x08
		self.name = "Key"
		self.character = 0x0C
		self.color = 0xFF
		self.destructable = False
		self.pushable = True
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x3169
		self.menu_number = 1
		self.key = 'K'
		self.internal_name = "Key"
		self.category = "Items"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class Door():
	"""
	Gem Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x09
		self.name = "Door"
		self.character = 0x0A
		self.color = 0xFE
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x33DA
		self.menu_number = 1
		self.key = 'D'
		self.internal_name = "Door"
		self.category = "Items"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0		

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class Scroll():
	"""
	Gem Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x0A
		self.name = "Scroll"
		self.character = 0xE8
		self.color = 0x0F
		self.destructable = False
		self.pushable = True
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = 1
		self.act_code = 0x2F9F
		self.interact_code = 0x308B
		self.menu_number = 1
		self.key = 'S'
		self.internal_name = "Scroll"
		self.category = "Items"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = "Edit text of scroll"
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = WHITE
		self.blinking = False


class Passage():
	"""
	Passage Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x0B
		self.name = "Passage"
		self.character = 0xF0
		self.color = 0xFE
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = True
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = 0
		self.act_code = 0x0000
		self.interact_code = 0x3372
		self.menu_number = 1
		self.key = 'P'
		self.internal_name = "Passage"
		self.category = "Items"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = "Room thru passage"
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class Duplicator():
	"""
	Duplicator Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x0C
		self.name = "Duplicator"
		self.character = 0xFA
		self.color = 0x0F
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = True
		self.draw_code = 0x2A15
		self.cycle = 2
		self.act_code = 0x2BFF
		self.interact_code = 0x0010
		self.menu_number = 1
		self.key = 'U'
		self.internal_name = "Duplicator"
		self.category = "Items"
		self.P1 = None
		self.P2 = "Duplication Rate"
		self.P3 = None
		self.edit_board = None
		self.edit_step = "Source Direction"
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = WHITE
		self.blinking = False


class Bomb():
	"""
	Bomb Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x0D
		self.name = "Bomb"
		self.character = 0x0B
		self.color = 0xFF
		self.destructable = False
		self.pushable = True
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = True
		self.draw_code = 0x1872
		self.cycle = 6
		self.act_code = 0x18DA
		self.interact_code = 0x19F3
		self.menu_number = 1
		self.key = 'B'
		self.internal_name = "Bomb"
		self.category = "Items"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = WHITE
		self.blinking = False


class Energizer():
	"""
	Energizer Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x0E
		self.name = "Energizer"
		self.character = 0x7F
		self.color = 0x05
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x2034
		self.menu_number = 1
		self.key = 'E'
		self.internal_name = "Energizer"
		self.category = "Items"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = DARK_PURPLE
		self.blinking = False


class Star():
	"""
	Duplicator Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x0F
		self.name = "Star"
		self.character = 0x53
		self.color = 0x0F
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = True
		self.draw_code = 0x1D5D
		self.cycle = 1
		self.act_code = 0x1DE9
		self.interact_code = 0x00F5
		self.menu_number = 0
		self.key = None
		self.internal_name = "Star"
		self.category = "Items"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = WHITE
		self.blinking = False


class ClockwiseConveyer():
	"""
	Clockwise Conveyer Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x10
		self.name = "Clockwise"
		self.character = 0x2F
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = True
		self.draw_code = 0x171C
		self.cycle = 3
		self.act_code = 0x176C
		self.interact_code = 0x0010
		self.menu_number = 1
		self.key = '1'
		self.internal_name = "Clockwise"
		self.category = "Conveyers"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = WHITE
		self.blinking = False


class CounterclockwiseConveyer():
	"""
	Counterclockwise Conveyer Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x11
		self.name = "Counter"
		self.character = 0x5C
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = True
		self.draw_code = 0x17C7
		self.cycle = 2
		self.act_code = 0x1817
		self.interact_code = 0x0010
		self.menu_number = 1
		self.key = '2'
		self.internal_name = "Counter"
		self.category = "Conveyers"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = WHITE
		self.blinking = False


class Bullet():
	"""
	Bullet Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x12
		self.name = "Bullet"
		self.character = 0xF8
		self.color = 0x0F
		self.destructable = True
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = 1
		self.act_code = 0x0F65
		self.interact_code = 0x00F5
		self.menu_number = 0
		self.key = None
		self.internal_name = "Bullet"
		self.category = None
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = WHITE
		self.blinking = False


class Water():
	"""
	Duplicator Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x13
		self.name = "Water"
		self.character = 0xB0
		self.color = 0xF9
		self.destructable = False
		self.pushable = False
		self.editor_floor = True
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x3B03
		self.menu_number = 3
		self.key = 'W'
		self.internal_name = "Water"
		self.category = "Terrains"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = LIGHT_GREY
		self.fg_color = LIGHT_BLUE
		self.blinking = True


class Forest():
	"""
	Forest Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x14
		self.name = "Forest"
		self.character = 0xB0
		self.color = 0x20
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x38D0
		self.menu_number = 3
		self.key = 'F'
		self.internal_name = "Forest"
		self.category = "Terrains"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = DARK_GREEN
		self.fg_color = BLACK
		self.blinking = False


class Solid():
	"""
	Solid Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x15
		self.name = "Solid"
		self.character = 0xDB
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x0010
		self.menu_number = 3
		self.key = 'S'
		self.internal_name = "Solid"
		self.category = "Walls"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class Normal():
	"""
	Normal Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x16
		self.name = "Normal"
		self.character = 0xB2
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x0010
		self.menu_number = 3
		self.key = 'N'
		self.internal_name = "Normal"
		self.category = "Walls"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class Breakable():
	"""
	Breakable Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x17
		self.name = "Breakable"
		self.character = 0xB1
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x0010
		self.menu_number = 3
		self.key = 'B'
		self.internal_name = "Breakable"
		self.category = "Walls"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = WHITE
		self.blinking = False


class Boulder():
	"""
	Boulder Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x18
		self.name = "Boulder"
		self.character = 0xFE
		self.color = 0xFF
		self.destructable = False
		self.pushable = True
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x34E3
		self.menu_number = 3
		self.key = 'O'
		self.internal_name = "Boulder"
		self.category = "Walls"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class SliderNS():
	"""
	Duplicator Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x19
		self.name = "Slider (NS)"
		self.character = 0x12
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x34E3
		self.menu_number = 3
		self.key = '1'
		self.internal_name = "Slider (NS)"
		self.category = "Walls"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class SliderEW():
	"""
	Duplicator Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x1A
		self.name = "Slider (EW)"
		self.character = 0x1D
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x34E3
		self.menu_number = 3
		self.key = '2'
		self.internal_name = "Slider (EW)"
		self.category = "Walls"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class Fake():
	"""
	Fake Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x1B
		self.name = "Fake"
		self.character = 0xB2
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = True
		self.floor = True
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x3949
		self.menu_number = 3
		self.key = 'A'
		self.internal_name = "Fake"
		self.category = "Walls"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class Invisible():
	"""
	Invisible Wall Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x1C
		self.name = "Invisible"
		self.character = 0xB0
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x3848
		self.menu_number = 3
		self.key = 'I'
		self.internal_name = "Invisible"
		self.category = "Walls"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class BlinkWall():
	"""
	Blink Wall Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x1D
		self.name = "Blink Wall"
		self.character = 0xCE
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = True
		self.draw_code = 0x242E
		self.cycle = 1
		self.act_code = 0x2445
		self.interact_code = 0x0010
		self.menu_number = 3
		self.key = 'L'
		self.internal_name = "Blink Wall"
		self.category = "Walls"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class Transporter():
	"""
	Transporter Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x1E
		self.name = "Transporter"
		self.character = 0xC5
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = True
		self.draw_code = 0x242E
		self.cycle = 2
		self.act_code = 0x1C85
		self.interact_code = 0x1C41
		self.menu_number = 3
		self.key = 'T'
		self.internal_name = "Transporter"
		self.category = "Walls"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class Line():
	"""
	Line Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x1F
		self.name = "Line"
		self.character = 0xCE
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = True
		self.draw_code = 0x122A
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x0010
		self.menu_number = 0
		self.key = None
		self.internal_name = "Line"
		self.category = "Walls"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


class Ricochet():
	"""
	Invisible Wall Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x20
		self.name = "Ricochet"
		self.character = 0x2A
		self.color = 0x0A
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x0010
		self.menu_number = 3
		self.key = 'R'
		self.internal_name = "Ricochet"
		self.category = "Walls"
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = BLACK
		self.fg_color = LIGHT_GREEN
		self.blinking = False


class BlinkRayHorizontal():
	"""
	Blink Ray Element
	"""

	def __init__(self, fg_color = WHITE, bg_color = BLACK):
		"""
		"""

		# These element properties are from www.shikadi.net/moddingwiki/ZZT_Format and
		# the ZZT format document
		self.id = 0x21
		self.name = "Blink Ray (Horizontal)"
		self.character = 0xCD
		self.color = 0xFF
		self.destructable = False
		self.pushable = False
		self.editor_floor = False
		self.floor = False
		self.shown = False
		self.special_draw = False
		self.draw_code = 0x0020
		self.cycle = -1
		self.act_code = 0x0000
		self.interact_code = 0x10
		self.menu_number = 0
		self.key = None
		self.internal_name = None
		self.category = None
		self.P1 = None
		self.P2 = None
		self.P3 = None
		self.edit_board = None
		self.edit_step = None
		self.edit_code = None
		self.points = 0

		# Color and blinking information
		self.bg_color = bg_color
		self.fg_color = fg_color
		self.blinking = False


