

class Ui:
    def __init__(self, service):
        self._service = service

    def _menu(self):
        print("Menu")
        print("1. Read from file")
        print("2. Generate random")
        print("3. Solve")
        print("4. Print sol")
        print("0. Exit")

    def _read(self):
        fn = input("Enter file name: ")
        print(self._service.read_board(fn))

    def _gen(self):
        n = int(input("Enter the size of the board: "))
        print(self._service.generate_random_board(n))

    def _solve(self):
        print(self._service.solve())

    def _print(self):
        v = self._service.print_graph()
        for ver in v:
            print(ver)

    def start(self):
        is_running = True

        command_dict = {'1': self._read, '2': self._gen, '3': self._solve, '4': self._print}

        while is_running:
            self._menu()
            command = input(">> ")

            if command in command_dict:
                try:
                    command_dict[command]()
                except:
                    print("Error")
            elif command == '0':
                is_running = False
            else:
                print("Invalid command\n")