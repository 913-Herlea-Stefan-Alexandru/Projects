from ui.BigBoard import BigBoard
import time

class ConsoleUI:
    def __init__(self, player_board, computer_board, ai, player):
        self._player_board = player_board
        self._computer_board = computer_board
        self._main_board = BigBoard(self._player_board, self._computer_board, self._computer_board.size)
        self._player = player
        self._ai = ai
        self._ai.place_ships(computer_board)

    def split_position(self, pos):
        if len(pos) != 2:
            raise ValueError()
        return pos[0], int(pos[1])

    def prep_ships(self):
        ship_list = [ship.name for ship in self._player.ship_list]
        while len(ship_list) != 0:
            print(ship_list)
            ship_name = input('Choose a ship (enter it\'s name): ')
            chosen_ship = None
            for ship in ship_list:
                if ship_name.lower() == ship:
                    chosen_ship = ship
                    break
            if chosen_ship == None:
                print('Wrong ship name')
                continue
            rotation = input('Choose the rotation of the ship (vertical = \'v\', horizontal = \'h\'): ')
            if rotation.lower() not in ['v', 'h']:
                print('Wrong ship rotation')
                continue
            while True:
                position = input('Choose the position of the ship by typing the coordinates of the top-left corner: ')
                try:
                    letter, number = self.split_position(position)
                    self._player.place_ship(chosen_ship, rotation, letter, number, self._player_board)
                    ship_list.pop(ship_list.index(chosen_ship))
                    print(self._main_board)
                    break
                except Exception:
                    print('Invalid coordinates')

    def player_won(self):
        for hp in [ship.hp for ship in self._ai.ship_list]:
            if hp > 0:
                return False
        return True

    def computer_won(self):
        for hp in [ship.hp for ship in self._player.ship_list]:
            if hp > 0:
                return False
        return True

    def start(self):
        print(self._main_board)
        self.prep_ships()
        is_running = True

        while is_running:
            print('Your turn')
            position = input('Shoot: ')
            try:
                while True:
                    if self.player_won():
                        print('\nYou win!\n')
                        is_running = False
                        break
                    letter, number = self.split_position(position)
                    shot = self._computer_board.move(letter, number)
                    print(self._main_board)
                    if shot == None:
                        break
                    print('Ship hit!\n')
                    if shot.hp == 0:
                        print('Enemy ' + shot.name + ' sunk!\n')
                    print('Your turn')
                    position = input('Shoot: ')
                while True:
                    if self.computer_won():
                        print('\nYou lose!\n')
                        is_running = False
                        break
                    print('Computer\'s turn')
                    time.sleep(3)
                    shot = self._ai.make_move(self._player_board)
                    print(self._main_board)
                    if shot == None:
                        break
                    print('Ship hit!\n')
                    if shot.hp == 0:
                        print('Friendly ' + shot.name + ' sunk!\n')
            except Exception:
                print('Invalid move')