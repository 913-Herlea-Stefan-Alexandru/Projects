import unittest
from entities.battleship import Battleship, BattleshipError
from entities.board import Board, BoardError
from entities.player import Player
from utility.RandomAi import RandomAi
from utility.SmartAi import SmartAi

class MyTestCase(unittest.TestCase):
    def test_battleship(self):
        carrier = Battleship(5, 'carrier')
        self.assertEqual(carrier.name, 'carrier')
        self.assertEqual(carrier.length, 5)
        self.assertEqual(carrier.hp, 5)
        carrier.hp -= 1
        self.assertEqual(carrier.hp, 4)
        carrier.rotation = 'v'
        self.assertEqual(carrier.rotation, 'v')
        try:
            carrier.rotation = 0
            self.assertEqual(True, False)
        except BattleshipError:
            self.assertEqual(True, True)

    def test_board(self):
        carrier = Battleship(5, 'carrier')
        carrier2 = Battleship(5, 'carrier')
        carrier.rotation = 'v'
        board = Board(8)
        self.assertEqual(board.size, 8)
        board.add_ship('A', 1, carrier)
        try:
            board.add_ship('H', 8, carrier)
            self.assertEqual(True, False)
        except BoardError:
            self.assertEqual(True, True)
        try:
            board.add_ship('A', 3, carrier)
            self.assertEqual(True, False)
        except BoardError:
            self.assertEqual(True, True)
        carrier2.rotation = 'h'
        board.add_ship('B', 1, carrier2)
        try:
            board.add_ship('A', 2, carrier2)
            self.assertEqual(True, False)
        except BoardError:
            self.assertEqual(True, True)
        try:
            board.add_ship('A', 10, carrier2)
            self.assertEqual(True, False)
        except BoardError:
            self.assertEqual(True, True)
        try:
            board.add_ship('Z', 2, carrier2)
            self.assertEqual(True, False)
        except BoardError:
            self.assertEqual(True, True)
        try:
            board.add_ship('H', 5, carrier2)
            self.assertEqual(True, False)
        except BoardError:
            self.assertEqual(True, True)

        board.move('H', 8)

        board.move('A', 1)
        board.move('A', 2)
        board.move('A', 4)
        board.move('A', 5)
        board.move('A', 3)
        try:
            board.move('A', 1)
            self.assertEqual(True, False)
        except BoardError:
            self.assertEqual(True, True)

        board.move('B', 1)
        board.move('C', 1)
        board.move('F', 1)
        board.move('E', 1)
        board.move('D', 1)

        grid = board.get_grid()
        self.assertEqual(grid[0][0][0], carrier)
        self.assertEqual(grid[0][0][1], 1)
        self.assertEqual(grid[7][7], 'm')
        self.assertEqual(grid[7][6], 0)

    def test_player(self):
        board = Board(8)
        player = Player()
        ship_list = player.ship_list
        self.assertEqual([ship.name for ship in ship_list],
                         ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer'])

        player.place_ship('carrier', 'v', 'A', 1, board)

    def test_random_ai(self):
        board = Board(8)
        ai = RandomAi()
        ship_list = ai.ship_list
        self.assertEqual([ship.name for ship in ship_list],
                         ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer'])

        ai.place_ships(board)
        ai.make_move(board)

    def test_smart_ai(self):
        board = Board(8)
        ai = SmartAi()
        ship_list = ai.ship_list
        self.assertEqual([ship.name for ship in ship_list],
                         ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer'])

        ai.place_ships(board)
        shot = None
        while not shot:
            shot = ai.make_move(board)
        while shot.hp != 0:
            ai.make_move(board)


if __name__ == '__main__':
    unittest.main()
