from typing import Tuple
from enum import Enum


class Direction(Enum):
    TOP = 'top'
    LEFT = 'left'
    BOTTOM = 'bottom'
    RIGHT = 'right'


HEAD_SYMBOLS = {
    (Direction.BOTTOM,): '∞ ',
    (Direction.LEFT,): '8═',
    (Direction.RIGHT,): '8 ',
    (Direction.TOP,): '∞ '
}
SYMBOLS = {
    (Direction.BOTTOM,): '║ ',
    (Direction.BOTTOM, Direction.LEFT): '╝ ',
    (Direction.BOTTOM, Direction.RIGHT): '╚═',
    (Direction.LEFT,): '══',
    (Direction.LEFT, Direction.BOTTOM): '╔═',
    (Direction.LEFT, Direction.TOP): '╚═',
    (Direction.RIGHT,): '══',
    (Direction.RIGHT, Direction.BOTTOM): '╗ ',
    (Direction.RIGHT, Direction.TOP): '╝ ',
    (Direction.TOP,): '║ ',
    (Direction.TOP, Direction.LEFT): '╗ ',
    (Direction.TOP, Direction.RIGHT): '╔═',

}


Pos = Tuple[int, int]
