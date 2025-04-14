from ...map_maker import map_maker
from ...color import Color
from ...map import Door, Key, Map, Lock

colors = Color.get_unique_colors(4)
PRACTICE2_1 = Map(
    map_maker(
        f"""
XXXXXXXX
X   _  X
XP _E_ X
X   _  X
XXXXXXXX
XS  S  X
X_ _ _ X
XPS S _X
X   SX X
XXXXXXXX
""",
        [
            *(Door(color, open=True) for color in colors),
            Lock(colors[3]),
            Lock(colors[1]),
            Lock(colors[0]),
            Lock(colors[2]),
        ],
    )
)
PRACTICE2 = ([PRACTICE2_1], "It's ok to lock some doors, as long as you can get in.")

# Solution 1 (12 moves)
# def script():
#     move(DOWN)
#     move(RIGHT)
#     move(RIGHT)
#     move(UP)
#     move(UP)
#     move(UP)
#     move(DOWN)
#     move(RIGHT)
#     move(RIGHT)
#     move(UP)
#     move(DOWN)
#     move(LEFT)

# Solution 2 (13 moves)
# def script():
#     move(DOWN)
#     move(RIGHT)
#     move(RIGHT)
#     move(UP)
#     move(UP)
#     move(RIGHT)
#     move(RIGHT)
#     move(RIGHT)
#     move(DOWN)
#     move(DOWN)
#     move(LEFT)
#     move(LEFT)
#     move(UP)
