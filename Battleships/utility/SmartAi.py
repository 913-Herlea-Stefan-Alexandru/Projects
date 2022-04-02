from entities.battleship import Battleship
from entities.board import BoardError
import random

class SmartAi:
    def __init__(self, pgame = False):
        self._carrier = Battleship(5, 'carrier', "res\\carrier.png", x=50,
                                   y=625, pgame=pgame)
        self._battleship = Battleship(4, 'battleship',
                                      "res\\battleship.png", x=325,
                                      y=625, pgame=pgame)
        self._cruiser = Battleship(3, 'cruiser', "res\\cruiser.png", x=50,
                                   y=550, pgame=pgame)
        self._submarine = Battleship(3, 'submarine', "res\\submarine.png",
                                     x=225, y=550, pgame=pgame)
        self._destroyer = Battleship(2, 'destroyer', "res\\destroyer.png",
                                     x=400, y=550, pgame=pgame)
        self._ship_list = [self._carrier, self._battleship, self._cruiser, self._submarine, self._destroyer]

        self._pgame = pgame

        self._last_hit = None
        self._first_point_hit = None
        self._direction = None

    @property
    def ship_list(self):
        return self._ship_list

    def _place_border_ship(self, border_ship, board):
        '''
        A function to place the given ship at one border of the board
        :param border_ship: the given ship (Battleship type)
        :param board: the given board (Board type)
        :return: -
        '''
        rotation = random.choice(['v', 'h'])
        if self._pgame and border_ship.rotation != rotation:
            border_ship.rotate()
        else:
            border_ship.rotation = rotation
        if border_ship.rotation == 'v':
            letter = random.choice(['A', 'H'])
            number = random.randint(1, board.size - border_ship.length + 1)
        else:
            letter = random.choice([chr(l + 65) for l in range(0, board.size - border_ship.length + 1)])
            number = random.choice([1, 8])
        board.add_ship(letter, number, border_ship)

    def place_ships(self, board):
        '''
        Places the ships randomly so that at least one is at the border of the grid and there are no ships side by side
        :param board: the given board (Board type)
        :return: -
        '''
        border_ship = random.choice(self._ship_list)
        self._place_border_ship(border_ship, board)

        ignore = self._ship_list.index(border_ship)

        index = 0
        rot = None
        while index < 5:
            if index == ignore:
                index += 1
                continue
            grid = board.get_grid()
            if rot == None:
                rot = random.choice(['v', 'h'])
                if self._ship_list[index].rotation != rot and self._pgame:
                    self._ship_list[index].rotate()
                else:
                    self._ship_list[index].rotation = rot
            letter = random.choice([chr(l + 65) for l in range(board.size)])
            number = random.randint(1, board.size)
            i = number - 1
            j = ord(letter) - 65
            if rot == 'v':
                if i + self._ship_list[index].length > board.size:
                    continue
                ok = 1
                for line in range(self._ship_list[index].length):
                    if j != 0 and grid[i+line][j-1] != 0:
                        ok = 0
                        break
                    elif j != board.size-1 and grid[i+line][j+1] != 0:
                        ok = 0
                        break
                if ok == 0:
                    continue
            elif rot == 'h':
                if j + self._ship_list[index].length > board.size:
                    continue
                ok = 1
                for col in range(self._ship_list[index].length):
                    if i != 0 and grid[i-1][j + col] != 0:
                        ok = 0
                        break
                    elif i != board.size-1 and grid[i+1][j + col] != 0:
                        ok = 0
                        break
                if ok == 0:
                    continue
            try:
                board.add_ship(letter, number, self._ship_list[index])
                rot = None
            except Exception:
                continue
            index += 1

    def check_for_ships(self, grid):
        '''
        Checks on the given grid if there are ships previously hit but not destroyed
        :param grid: the player grid (list of list)
        :return: -
        '''
        for line in range(len(grid)):
            for col in range(len(grid[line])):
                if type(grid[line][col]) == type([]) and grid[line][col][1] == 'd':
                    self._first_point_hit = (chr(col + 65), line + 1)
                    self._last_hit = (chr(col + 65), line + 1)
                    return

    def check_too_crowded(self, i, j, g, player_board):
        '''
        Checks if the given position has 3 or more already hit spots around
        :param i: i coordinate for the grid (lines) (int)
        :param j: j coordinate for the grid (columns)(int)
        :param g: the grid (list of list)
        :param player_board: the player board (Board type)
        :return: True if there are too many surrounding hits, False otherwise
        '''
        k = 0
        if i - 1 < 0 or (g[i - 1][j] == 'm' if type(g[i - 1][j]) != type([]) else g[i - 1][j][1] in ['d', 1]):
            k += 1
        if i + 1 >= player_board.size or (
        g[i + 1][j] == 'm' if type(g[i + 1][j]) != type([]) else g[i + 1][j][1] in ['d', 1]):
            k += 1
        if j - 1 < 0 or (g[i][j - 1] == 'm' if type(g[i][j - 1]) != type([]) else g[i][j - 1][1] in ['d', 1]):
            k += 1
        if j + 1 >= player_board.size or (
        g[i][j + 1] == 'm' if type(g[i][j + 1]) != type([]) else g[i][j + 1][1] in ['d', 1]):
            k += 1
        if k > 2:
            return True
        return False

    def make_move(self, player_board):
        '''
        Makes a correct calculated move on the player's board
        :param player_board: the player's board (Board type)
        :return: -
        '''
        g = player_board.get_grid()
        while True:
            if self._first_point_hit == None:
                letter = random.choice([chr(l + 65) for l in range(player_board.size)])
                number = random.randint(1, player_board.size)
                i = number - 1
                j = ord(letter) - 65
                m = i + j
                if m % 2 == 0:
                    continue
                if self.check_too_crowded(i, j, g, player_board):
                    continue
            else:
                letter = self._last_hit[0]
                number = self._last_hit[1]
                i = number - 1
                j = ord(letter) - 65
                if self._direction == None:
                    if j+1 < player_board.size and (g[i][j+1] != 'm' if type(g[i][j+1]) != type([]) else g[i][j+1][1] not in ['d', 1]):
                        self._direction = 'h+'
                    elif i-1 >= 0 and (g[i-1][j] != 'm' if type(g[i-1][j]) != type([]) else g[i-1][j][1] not in ['d', 1]):
                        self._direction = 'v-'
                    elif j-1 >= 0 and (g[i][j-1] != 'm' if type(g[i][j-1]) != type([]) else g[i][j-1][1] not in ['d', 1]):
                        self._direction = 'h-'
                    elif i+1 < player_board.size and (g[i+1][j] != 'm' if type(g[i+1][j]) != type([]) else g[i+1][j][1] not in ['d', 1]):
                        self._direction = 'v+'
                if self._direction == 'h+':
                    letter = chr(j + 65 + 1)
                elif self._direction == 'v-':
                    number -= 1
                elif self._direction == 'h-':
                    letter = chr(j + 65 - 1)
                else:
                    number += 1
            try:
                shot = player_board.move(letter, number)
                if shot != None:
                    if self._last_hit == None:
                        self._first_point_hit = (letter, number)
                    self._last_hit = (letter, number)
                    if shot.hp == 0:
                        self._first_point_hit = None
                        self._last_hit = None
                        self._direction = None
                        self.check_for_ships(g)
                    else:
                        letter = self._last_hit[0]
                        number = self._last_hit[1]
                        i = number - 1
                        j = ord(letter) - 65
                        if self._last_hit != self._first_point_hit:
                            if self._direction == 'h+' and (j+1 >= player_board.size or (g[i][j+1] == 'm' if type(g[i][j+1]) != type([]) else g[i][j+1][1] in ['d', 1])):
                                self._last_hit = self._first_point_hit
                                self._direction = 'h-'
                            elif self._direction == 'v-' and (i-1 < 0 or (g[i-1][j] == 'm' if type(g[i-1][j]) != type([]) else g[i-1][j][1] in ['d', 1])):
                                self._last_hit = self._first_point_hit
                                self._direction = 'v+'
                            elif self._direction == 'h-' and (j-1 < 0 or (g[i][j-1] == 'm' if type(g[i][j-1]) != type([]) else g[i][j-1][1] in ['d', 1])):
                                self._last_hit = self._first_point_hit
                                self._direction = None
                            elif self._direction == 'v+' and (i+1 >= player_board.size or (g[i+1][j] == 'm' if type(g[i+1][j]) != type([]) else g[i+1][j][1] in ['d', 1])):
                                self._last_hit = self._first_point_hit
                                self._direction = None
                elif self._first_point_hit != None and self._last_hit != None:
                    letter = self._first_point_hit[0]
                    number = self._first_point_hit[1]
                    i = number - 1
                    j = ord(letter) - 65
                    if self._last_hit == self._first_point_hit and self._first_point_hit != None:
                        if self._direction == 'h+' and i-1 >= 0 and (g[i-1][j] != 'm' if type(g[i-1][j]) != type([]) else g[i-1][j][1] not in ['d', 1]):
                            self._direction = 'v-'
                        elif self._direction == 'v-' and j-1 >= 0 and (g[i][j-1] != 'm' if type(g[i][j-1]) != type([]) else g[i][j-1][1] not in ['d', 1]):
                            self._direction = 'h-'
                        elif self._direction == 'h-' and i+1 < player_board.size and (g[i+1][j] != 'm' if type(g[i+1][j]) != type([]) else g[i+1][j][1] not in ['d', 1]):
                            self._direction = 'v+'
                        else:
                            self._direction = None
                    else:
                        if self._direction == 'h+' and j-1 >= 0 and (g[i][j-1] != 'm' if type(g[i][j-1]) != type([]) else g[i][j-1][1] not in ['d', 1]):
                            self._last_hit = self._first_point_hit
                            self._direction = 'h-'
                        elif self._direction == 'v-' and i+1 < player_board.size and (g[i+1][j] != 'm' if type(g[i+1][j]) != type([]) else g[i+1][j][1] not in ['d', 1]):
                            self._last_hit = self._first_point_hit
                            self._direction = 'v+'
                        else:
                            self._direction = None
                else:
                    self.check_for_ships(g)
                return shot
                break
            except BoardError:
                self._first_point_hit = None
                self._last_hit = None
                self._direction = None
                self.check_for_ships(g)
                pass
