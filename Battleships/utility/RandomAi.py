import random
from entities.battleship import Battleship
from entities.board import BoardError

class RandomAi:
    def __init__(self, pgame = False):
        self._carrier = Battleship(5, 'carrier', "D:\FP Python\\Battleships\\res\carrier.png", x=50,
                                   y=625, pgame=pgame)
        self._battleship = Battleship(4, 'battleship',
                                      "D:\FP Python\\Battleships\\res\\battleship.png", x=325,
                                      y=625, pgame=pgame)
        self._cruiser = Battleship(3, 'cruiser', "D:\FP Python\\Battleships\\res\cruiser.png", x=50,
                                   y=550, pgame=pgame)
        self._submarine = Battleship(3, 'submarine', "D:\FP Python\\Battleships\\res\submarine.png",
                                     x=225, y=550, pgame=pgame)
        self._destroyer = Battleship(2, 'destroyer', "D:\FP Python\\Battleships\\res\destroyer.png",
                                     x=400, y=550, pgame=pgame)
        self._ship_list = [self._carrier, self._battleship, self._cruiser, self._submarine, self._destroyer]

        self._pgame = pgame

    @property
    def ship_list(self):
        return self._ship_list

    def place_ships(self, board):
        '''
        Places all the ships into random available positions on it's board
        :param board: the computer's board (Board type)
        :return: -
        '''
        index = 0
        while index < 5:
            rot = random.choice(['v', 'h'])
            if self._ship_list[index].rotation != rot and self._pgame:
                self._ship_list[index].rotate()
            else:
                self._ship_list[index].rotation = rot
            letter = random.choice([chr(l + 65) for l in range(board.size)])
            number = random.randint(1, board.size)
            try:
                board.add_ship(letter, number, self._ship_list[index])
            except Exception:
                index -= 1
            index += 1

    def make_move(self, player_board):
        '''
        Makes a random correct move on the player's board
        :param player_board: the player's board (Board type)
        :return: -
        '''
        while True:
            letter = random.choice([chr(l + 65) for l in range(player_board.size)])
            number = random.randint(1, player_board.size)
            try:
                shot = player_board.move(letter, number)
                return shot
                break
            except BoardError:
                pass