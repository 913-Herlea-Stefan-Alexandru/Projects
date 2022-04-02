import pygame
from entities.tile import Tile

class BoardError(Exception):
    def __init__(self, msg = ''):
        super().__init__(msg)


class Board(pygame.sprite.Sprite):
    def __init__(self, size = 8, x = 0, y = 0, pgame = False):
        super().__init__()
        self._size = size
        self._grid = [[0 for col in range(size)] for row in range(size)]

        self._pgame = pgame

        if pgame:

            self.width = size*50
            self.height = size*50
            self.tile_list = []

            self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA, 32)
            self.image.convert_alpha()

            for i in range(self._size):
                for j in range(self._size):
                    m = i + j
                    if m % 2 == 0:
                        self.tile_list.append(Tile("res\\light_tile.png", 50, x + j * 50, y + i * 50))
                    else:
                        self.tile_list.append(Tile("res\\dark_tile.png", 50, x + j * 50, y + i * 50))
                    self.image.blit(self.tile_list[-1].image, (50 * j, 50 * i))

            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def get_coordinates(self, x, y):
        '''
        Gives the actual coordinates (letter and number) of the point given (GUI only)
        :param x: the x coordinate on the screen (int)
        :param y: the y coordinate on the screen (int)
        :return: the corresponding letter and number of the given coordinates on the board
        :raises BoardError: if the given coordinates are not on the board
        '''
        if self.rect.x <= x <= self.rect.x + self._size * 50 and self.rect.y <= y <= self.rect.y + self._size * 50:
            chosen_tile = None
            for tile in self.tile_list:
                if tile.rect.x <= x <= tile.rect.x + tile.width and tile.rect.y <= y <= tile.rect.y + tile.width:
                    chosen_tile = tile
                    break
            if chosen_tile == None:
                raise BoardError()
            j = (chosen_tile.rect.x - self.rect.x) // 50
            i = (chosen_tile.rect.y - self.rect.y) // 50
            letter = chr(j + 65)
            number = i + 1
            return letter, number
        else:
            raise BoardError()

    def remove_ship(self, ship):
        '''
        Removes a ship from the board (GUI only)
        :param ship: the ship to remove (Battleship type)
        :return: -
        '''
        j = (ship.rect.x - self.rect.x) // 50
        i = (ship.rect.y - self.rect.y) // 50
        if ship.rotation == 'v':
            k = 0
            while k < ship.length:
                self._grid[i][j] = 0
                k += 1
                i += 1
        elif ship.rotation == 'h':
            k = 0
            while k < ship.length:
                self._grid[i][j] = 0
                k += 1
                j += 1

    @property
    def size(self):
        return self._size

    def _check_if_in_bounds(self, letter, number):
        '''
        Checks if the given coordinates are in the bounds of the board
        :param letter: the letter of the coordinate (str)
        :param number: the number of the coordinate (int)
        :return: -
        :raises BoardError: if the move is not in bounds
        '''
        if number < 1 or number > self._size:
            raise BoardError()
        if letter.upper() not in [chr(65 + i) for i in range(self._size)]:
            raise BoardError()

    def add_ship(self, letter, number, ship):
        '''
        Adds a given ship at the given coordinates
        :param letter: the letter of the coordinate (str)
        :param number: the number of the coordinate (int)
        :param ship: the given ship (Battleship type)
        :return: -
        :raises BoardError: if the ship goes out of bounds
        '''
        self._check_if_in_bounds(letter, number)
        x = ord(letter.upper()) - 65
        y = number - 1
        if ship.rotation == 'h':
            if x + ship.length > self._size:
                raise BoardError()
            for col in range(x, x + ship.length):
                if self._grid[y][col] != 0:
                    raise BoardError()
            for col in range(x, x + ship.length):
                self._grid[y][col] = [ship, 's']
        elif ship.rotation == 'v':
            if y + ship.length > self._size:
                raise BoardError()
            for row in range(y, y + ship.length):
                if self._grid[row][x] != 0:
                    raise BoardError()
            for row in range(y, y + ship.length):
                self._grid[row][x] = [ship, 's']

        if self._pgame:
            ship.rect.x = self.rect.x + x * 50
            ship.rect.y = self.rect.y + y * 50

    def _sink(self, x, y, ship):
        '''
        Sinks the given ship by looking for it's parts starting at the given coordinate
        :param x: x coordinate (int)
        :param y: y coordinate (int)
        :param ship: the given ship (Battleship type)
        :return: -
        '''
        self._grid[y][x][1] = 1
        if ship.rotation == 'h':
            x2 = x + 1
            while x2 < self._size and type(self._grid[y][x2]) == type([]) and self._grid[y][x2][0] == ship:
                self._grid[y][x2][1] = 1
                x2 += 1

            x2 = x - 1
            while x2 < self._size and type(self._grid[y][x2]) == type([]) and self._grid[y][x2][0] == ship:
                self._grid[y][x2][1] = 1
                x2 -= 1
        else:
            y2 = y + 1
            while y2 < self._size and type(self._grid[y2][x]) == type([]) and self._grid[y2][x][0] == ship:
                self._grid[y2][x][1] = 1
                y2 += 1

            y2 = y - 1
            while y2 < self._size and type(self._grid[y2][x]) == type([]) and self._grid[y2][x][0] == ship:
                self._grid[y2][x][1] = 1
                y2 -= 1

        ship.sink()

    def move(self, letter, number):
        '''
        Makes a move at the given coordinates
        :param letter: the letter of the coordinate (str)
        :param number: the number of the coordinate (int)
        :return: the ship if it hit one, None if no ship was hit
        '''
        self._check_if_in_bounds(letter, number)
        x = ord(letter.upper()) - 65
        y = number - 1
        if self._grid[y][x] == 0:
            self._grid[y][x] = 'm'
            if self._pgame:
                for tile in self.tile_list:
                    if tile.rect.x == self.rect.x + x * 50 and tile.rect.y == self.rect.y + y * 50:
                        tile.change_picture("res\\light_tile_miss.png")
                        self.image.blit(tile.image, (50 * x, 50 * y))
                        break
        elif type(self._grid[y][x]) == type([]) and self._grid[y][x][1] == 's':
            self._grid[y][x][1] = 'd'
            self._grid[y][x][0].hp -= 1
            if self._grid[y][x][0].hp == 0:
                self._sink(x, y, self._grid[y][x][0])
            if self._pgame:
                for tile in self.tile_list:
                    if tile.rect.x == self.rect.x + x * 50 and tile.rect.y == self.rect.y + y * 50:
                        tile.change_picture("res\\damaged_tile.png")
                        self.image.blit(tile.image, (50 * x, 50 * y))
                        break
            return self._grid[y][x][0]
        else:
            raise BoardError()
        return None

    def get_grid(self):
        '''
        :return: a copy of the grid of the board
        '''
        grid_copy = []
        for row in range(self._size):
            grid_row = []
            for col in range(self._size):
                grid_row.append(self._grid[row][col])
            grid_copy.append(grid_row)
        return grid_copy