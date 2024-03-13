# Author: 4sushi
from __future__ import annotations
import random
import threading
import time
from typing import List, Dict
from snake_game import Direction, Pos, SYMBOLS, HEAD_SYMBOLS


class GameSnake(threading.Thread):

    NB_ROW: int = 10
    NB_COL: int = 20

    MODE: Dict[int, Dict] = {
        1: {'description': 'Easy with border that can be crossed', 'can_cross_border': True, 'time_s': 0.3},
        2: {'description': 'Medium with border that can be crossed', 'can_cross_border': True, 'time_s': 0.2},
        3: {'description': 'Hard with border that can be crossed', 'can_cross_border': True, 'time_s': 0.1},
        4: {'description': 'Easy with border that cannot be crossed', 'can_cross_border': False, 'time_s': 0.3},
        5: {'description': 'Medium with border that cannot be crossed', 'can_cross_border': False, 'time_s': 0.2},
        6: {'description': 'Hard with border that cannot be crossed', 'can_cross_border': False, 'time_s': 0.1},
    }

    def __init__(self, mode: int = 1):
        self.score: int = 0
        self.direction: Direction = Direction.RIGHT
        self.next_directions: List[Direction] = []
        self.snake: List[Dict[str, Pos | Direction]] = [
            {'pos': (0, 3), 'symbol': SYMBOLS[(self.direction,)]},
            {'pos': (1, 3), 'symbol': SYMBOLS[(self.direction,)]},
            {'pos': (2, 3), 'symbol': HEAD_SYMBOLS[(self.direction,)]}
        ]
        self.food_pos = None
        self.place_food()
        self.can_cross_border: bool = self.MODE[mode]['can_cross_border']
        self.time_s: float = self.MODE[mode]['time_s']
        self.time_last_refresh: None | float = None
        self.lock: threading.Lock = threading.Lock()
        self.stop_thread: bool = False
        super().__init__()

    def move(self) -> bool:
        self.lock.acquire()
        directions = [self.direction]
        if len(self.next_directions) > 0:
            self.direction = self.next_directions.pop(0)
            directions.append(self.direction)
        self.lock.release()
        next_pos = self.get_next_pos(self.snake[-1]['pos'])
        is_border_crossed: bool = self.is_border_crossed(next_pos)
        if is_border_crossed:
            if not self.can_cross_border:
                return False
            else:
                next_pos = self.get_pos_cross_border(next_pos)

        if next_pos == self.food_pos:
            self.score += 1
            self.place_food()
        else:
            self.snake.pop(0)

        snake_positions = [part['pos'] for part in self.snake]
        if next_pos in snake_positions:
            return False

        self.snake[-1]['symbol'] = SYMBOLS.get(tuple(directions))
        self.snake.append({'pos': next_pos, 'symbol': HEAD_SYMBOLS[(self.direction,)]})
        return True

    def get_next_pos(self, actual_pos: Pos) -> Pos:
        x, y = actual_pos
        if self.direction == Direction.RIGHT:
            x += 1
        elif self.direction == Direction.LEFT:
            x -= 1
        elif self.direction == Direction.BOTTOM:
            y += 1
        elif self.direction == Direction.TOP:
            y -= 1
        return x, y

    def get_pos_cross_border(self, actual_pos: Pos) -> Pos:
        x, y = actual_pos
        if x >= self.NB_COL:
            x = 0
        elif y >= self.NB_ROW:
            y = 0
        elif x < 0:
            x = self.NB_COL - 1
        elif y < 0:
            y = self.NB_ROW - 1
        return x, y

    def is_border_crossed(self, pos: Pos) -> bool:
        x, y = pos
        return x >= self.NB_COL or y >= self.NB_ROW or x < 0 or y < 0

    def add_direction(self, direction: Direction):
        self.lock.acquire()
        if len(self.next_directions) > 0:
            last_direction: Direction = self.next_directions[-1]
        else:
            last_direction: Direction = self.direction
        if (direction == Direction.LEFT and last_direction != Direction.RIGHT) or\
           (direction == Direction.RIGHT and last_direction != Direction.LEFT) or\
           (direction == Direction.TOP and last_direction != Direction.BOTTOM) or\
           (direction == Direction.BOTTOM and last_direction != Direction.TOP):
            if direction != last_direction:
                self.next_directions.append(direction)
        self.lock.release()

    def place_food(self):
        snake_positions: List[Pos] = [part['pos'] for part in self.snake]
        all_positions: List[Pos] = []
        for i_row in range(0, self.NB_ROW):
            for i_col in range(0, self.NB_COL):
                all_positions.append((i_col, i_row))
        available_positions: List[Pos] = list(set(all_positions) - set(snake_positions))
        self.food_pos = random.choice(available_positions)

    def get_snake_str(self) -> str:
        s: str = '┏' + ('━' * (self.NB_COL * 2)) + '┓\n'
        positions = {part['pos']: part['symbol'] for part in self.snake}
        for i_row in range(0, self.NB_ROW):
            s += '┃'
            for i_col in range(0, self.NB_COL):
                pos = (i_col, i_row)
                if pos in positions.keys():
                    s += f'{positions[pos]}'
                elif pos == self.food_pos:
                    s += '$ '
                else:
                    s += '· '
            s += '┃\n'
        s += '┗' + ('━' * (self.NB_COL * 2)) + '┛\n'
        return s

    def run(self):
        is_ok: bool = True
        while not self.stop_thread and is_ok:
            is_ok = self.move()
            self.time_last_refresh = time.time()
            time.sleep(self.time_s)

    def stop(self):
        self.stop_thread = True
