from entities.board import BoardError


class CommandError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Ui:
    def __init__(self, board):
        self._board = board

    def _split_command(self, command):
        tokens = command.split(' ')
        return tokens[0].strip().lower(), (tokens[1].strip().lower() if len(tokens) >= 2 else None)

    def _change_direction(self, params):
        return self._board.change_direction(params)

    def _move(self, params):
        if params == None:
            return self._board.move(1)
        try:
            n = int(params)
        except ValueError:
            raise CommandError('\nInvalid parameters\n')
        return self._board.move(n)

    def start(self):
        is_running = True
        command_list = ['up', 'down', 'right', 'left']
        while is_running:
            print(self._board)
            cmd_in = input()
            cmd, params = self._split_command(cmd_in)
            try:
                if cmd == 'move':
                    is_running = self._move(params)
                elif cmd in command_list and params == None:
                    is_running = self._change_direction(cmd)
                elif cmd == 'exit':
                    is_running = False
                else:
                    print('\nInvalid command\n')
            except (CommandError, BoardError) as e:
                print(str(e))
        print('\nGame over\n')
