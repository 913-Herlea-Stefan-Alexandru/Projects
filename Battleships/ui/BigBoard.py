from texttable import Texttable

class BigBoard:
    def __init__(self, player_board, computer_board, size):
        self._size = size
        self._player_board = player_board
        self._computer_board = computer_board

    def __str__(self):
        '''
        Used to print both player and computer boards as a table
        :return: -
        '''
        t = Texttable()

        header = [' ']
        for h in range(self._size):
            header.append(chr(65 + h))
        header.append('        ')

        for h in range(self._size):
            header.append(chr(65 + h))
        header.append(' ')

        t.header(header)

        player_grid = self._player_board.get_grid()
        computer_grid = self._computer_board.get_grid()

        for row in range(1, self._size + 1):
            data = [row]

            for val in player_grid[row - 1]:
                if val == 0:
                    data.append(' ')
                elif type(val) == type([]) and val[1] == 's':
                    data.append(chr(0x2588))
                elif type(val) == type([]) and val[1] == 'd':
                    data.append(chr(130))
                elif type(val) == type([]) and val[1] == 1:
                    data.append('X')
                else:
                    data.append('O')

            data.append('        ')

            for val in computer_grid[row - 1]:
                if val == 0:
                    data.append(' ')
                elif type(val) == type([]) and val[1] == 's':
                    data.append(' ')
                elif type(val) == type([]) and val[1] == 'd':
                    data.append(chr(130))
                elif type(val) == type([]) and val[1] == 1:
                    data.append('X')
                else:
                    data.append('O')

            data.append(row)

            t.add_row(data)

        return t.draw()
