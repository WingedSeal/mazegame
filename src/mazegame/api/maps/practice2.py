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
XS     X
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

# def script():
#     move(RIGHT)
#     move(DOWN)
#     move(DOWN)
#     for _ in range(4):
#         move(LEFT)
#     for _ in range(4):
#         move(UP)
#     for _ in range(4):
#         move(RIGHT)
#     move(UP)
#     move(RIGHT)
#     move(UP)
#     move(LEFT)
#     move(DOWN)
#     for _ in range(3):
#         move(LEFT)
#     move(UP)
#     move(UP)
