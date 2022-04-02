from ui.consoleUI import ConsoleUI
from entities.board import Board
from utility.RandomAi import RandomAi
from utility.SmartAi import SmartAi
from entities.player import Player
from ui.GUI import GUI


if __name__ == '__main__':
    print('\nChoose difficulty:\n')
    print('1. Easy')
    print('2. Hard')
    ai_type = ''
    while True:
        command = input('>> ')
        if command == '1':
            ai_type = 'random'
            break
        elif command == '2':
            ai_type = 'smart'
            break
        else:
            print('Invalid command\n')
    print('Choose option:\n')
    print('1. Console based')
    print('2. GUI')
    while True:
        command = input('>> ')
        if command == '1':
            player_board = Board(8)
            computer_board = Board(8)
            player = Player()
            if ai_type == 'smart':
                ai = SmartAi()
            else:
                ai = RandomAi()
            ui = ConsoleUI(player_board, computer_board, ai, player)
            break
        elif command == '2':
            ui = GUI(ai_type)
            break
        else:
            print('Invalid command\n')
    ui.start()
