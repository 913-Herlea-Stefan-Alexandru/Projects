from entities.battleship import Battleship

class Player:
    def __init__(self, pgame = False):
        self._carrier = Battleship(5, 'carrier', "res\\carrier.png", x=50, y=625, pgame=pgame)
        self._battleship = Battleship(4, 'battleship', "res\\battleship.png", x = 325, y = 625, pgame=pgame)
        self._cruiser = Battleship(3, 'cruiser', "res\\cruiser.png", x = 50, y = 550, pgame=pgame)
        self._submarine = Battleship(3, 'submarine', "res\\submarine.png", x = 225, y = 550, pgame=pgame)
        self._destroyer = Battleship(2, 'destroyer', "res\\destroyer.png", x = 400, y = 550, pgame=pgame)
        self._ship_list = [self._carrier, self._battleship, self._cruiser, self._submarine, self._destroyer]

    @property
    def ship_list(self):
        return self._ship_list

    def place_ship(self, ship_name, rotation, letter, number, board):
        '''
        Places the given ship onto the player board
        :param ship_name: the given ship name (str)
        :param rotation: the ship rotation (str)
        :param letter: the letter coordinate (str)
        :param number: the number coordinate (int)
        :param board: the player board (Board type)
        :return: -
        '''
        for ship in self._ship_list:
            if ship_name == ship.name:
                chosen_ship = ship
                break
        chosen_ship.rotation = rotation
        board.add_ship(letter, number, chosen_ship)
