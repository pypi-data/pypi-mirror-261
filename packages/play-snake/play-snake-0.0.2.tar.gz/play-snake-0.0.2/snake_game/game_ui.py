# Author: 4sushi
from __future__ import annotations
import curses
from multiprocessing import Process, Manager
import time
from snake_game.game import GameSnake
from snake_game import Direction
import sys


class GameUI:

    def __init__(self):
        self.stdscr = None
        self.game: None | GameSnake = None
        self.height: None | int = None
        self.width: None | int = None
        self.KEY_QUIT: int = ord('!')
        self.KEY_RESTART: int = ord('?')
        self.color_red: int | None = None
        self.game_mode: int = 2
        self.time_last_refresh: float = 0.
        self.keyboard_handler: None | GameUIKeyboardHandler = None
        curses.wrapper(self.init_screen)

    def init_screen(self, stdscr):
        self.stdscr = stdscr
        curses.curs_set(0)
        self.stdscr.keypad(True)
        # Init colors
        curses.use_default_colors()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, -1)
        self.color_red = curses.color_pair(1)
        # Init game
        self.init_game()
        self.keyboard_handler = GameUIKeyboardHandler(self.stdscr)
        self.loop()

    def init_game(self, mode: int = 2):
        self.game_mode = mode
        self.game = GameSnake(self.game_mode)
        self.game.start()

    def loop(self):
        k = None
        while k != self.KEY_QUIT:
            try:
                k = self.keyboard_handler.get_key()
                if k:
                    self.controller(k)
                if not self.game.stop_thread and self.game.time_last_refresh != self.time_last_refresh:
                    self.refresh_screen()
                    self.time_last_refresh = self.game.time_last_refresh
            except KeyboardInterrupt:
                self.quit()
            except curses.error as e:
                if str(e) == 'addwstr() returned ERR':
                    self.popup_error()
                    time.sleep(0.2)
                else:
                    raise e

    def quit(self):
        self.game.stop()
        self.keyboard_handler.stop()
        sys.exit(0)

    def controller(self, k):
        if k in (curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP):
            self.controller_direction_keys(k)
        elif k == self.KEY_RESTART:
            self.popup_new_game()
        elif k == self.KEY_QUIT:
            self.quit()

    def controller_direction_keys(self, k: int):
        if k == curses.KEY_RIGHT:
            self.game.add_direction(Direction.RIGHT)
        elif k == curses.KEY_LEFT:
            self.game.add_direction(Direction.LEFT)
        elif k == curses.KEY_UP:
            self.game.add_direction(Direction.TOP)
        elif k == curses.KEY_DOWN:
            self.game.add_direction(Direction.BOTTOM)

    def popup_new_game(self):
        self.game.stop()
        self.stdscr.clear()
        self.height, self.width = self.stdscr.getmaxyx()
        message = f'New game - Choose the mode (enter the corresponding number):\n\n'
        for i, mode in self.game.MODE.items():
            message += f'{i}- {mode["description"]}\n'
        self.stdscr.addstr(0, 0, message)

        info_menu: str = f'[1][2][3][4][5][6]select mode [!]quit'
        self.stdscr.addstr(self.height - 1, 0, info_menu + ' ' * (self.width - len(info_menu) - 1), curses.A_STANDOUT)
        self.stdscr.refresh()
        while True:
            k = self.keyboard_handler.get_key()
            if k and ord('1') <= k <= ord('6'):
                c = chr(k)
                self.init_game(mode=int(c))
                break
            if k == self.KEY_QUIT:
                self.quit()

    def popup_error(self):
        self.stdscr.clear()
        self.height, self.width = self.stdscr.getmaxyx()
        x_center = int(self.width / 2)
        y_center = int(self.height / 2)
        error_message: str = 'Screen is to small, enlarge the window and restart the game.\n'
        self.stdscr.addstr(y_center - 1, x_center - int(len(error_message) / 2), error_message, self.color_red)
        self.stdscr.refresh()

    def refresh_screen(self):
        self.stdscr.clear()
        self.height, self.width = self.stdscr.getmaxyx()

        # Draw snake
        lines = self.game.get_snake_str().split('\n')
        for i, line in enumerate(lines):
            self.stdscr.addstr(1+i, 1, line)

        info_menu: str = f'(Score {self.game.score}) Mode {self.game_mode} [←][→][↑][↓]move [?]new game [!]quit'
        self.stdscr.addstr(self.height-1, 0, info_menu + ' '*(self.width-len(info_menu)-1), curses.A_STANDOUT)
        self.stdscr.refresh()


class GameUIKeyboardHandler:

    def __init__(self, stdscr):
        self.stdscr = stdscr
        manager = Manager()
        self.keys = manager.list()
        self.p = Process(target=GameUIKeyboardHandler.start, args=(stdscr, self.keys))
        self.p.start()

    @staticmethod
    def start(stdscr, keys):
        while True:
            k: int = stdscr.getch()
            keys.append(k)

    def stop(self):
        self.p.kill()

    def get_key(self) -> int | None:
        k: int | None = None
        if len(self.keys) > 0:
            k = self.keys.pop(0)
        return k
