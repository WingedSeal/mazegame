from ...map_maker import map_maker
from ...color import Color
from ...map import CustomMapType, Door, Key, Map, Lock


def _get_map():
    colors = Color.get_unique_colors(4)
    PRACTICE3 = Map(
        map_maker(
            f"""
XXXXXXXXX
X       X
X   X_X X
X P _E_ X
X   X_X X
X X     X
XXXXXXXXX
X S   XXX
X  S  XXX
X  _S XXX
X SP_ XXX
X  __ XXX
X   S XXX
X  S  XXX
XXXXXXXXX
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
    return ([PRACTICE3], "There are 2 players.")


PRACTICE3: CustomMapType = _get_map

# def script():
#     move(UP)
#     for i in range(3):
#         move(DOWN)
#     move(UP)
#     for i in range(3):
#         move(RIGHT)
