from ...map_maker import map_maker
from ...color import Color
from ...map import Door, Exit, Key, Map, Block, Player, Spike

color1, color2 = Color.get_unique_colors(2)
PRACTICE1_1 = Map(
    map_maker(
        f"""
 XXXXXXX
 XEXXSXX
XX_XX  X
X     SX
X SXXPXX
X _   XX
XXXXXXXX
   X  _X
XXS _X_X
X      X
XX XXX X
 X XP  X
 X XS  X
 X    XX
XXXXXXXX
""",
        [Door(color1), Key(color2), Key(color1), Door(color1), Door(color2)],
    )
)
PRACTICE1 = ([PRACTICE1_1], "There are 2 players")
