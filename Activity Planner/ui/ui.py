from services.service import Service

class Ui:
    def __init__(self, service):
        self._service = service

    def _printMenu(self):
        print('\tMenu')
        print('1. Topological sort')
        print('2. Create project')
        print('3. Load from file')
        print('0. Exit')

    def _toposort(self):
        try:
            res = self._service.tarjans()
            for v in res:
                print(str(v))
        except ValueError as err:
            print(str(err))

    def _project(self):
        res, ms, me, Ms, Me = self._service.project()

        print("Activity | Duration | Earliest | Latest | Is Critical")
        print("---------+----------+----------+--------+------------")
        for v in res:
            if v.name == 'Start' or v.name == 'End':
                continue
            print(str(v).ljust(8) + ' | ' + str(v.duration).ljust(8) + ' | ' + (str(ms[v]) + '-' + str(me[v])).ljust(8)
                  + ' | ' + (str(Ms[v]) + '-' + str(Me[v])).ljust(6) + ' | ' + str(ms[v] == Ms[v]))

    def _load(self):
        fn = input("\nEnter file name: ")
        print()
        self._service.load(fn)

    def start(self):
        commandDict = {'1': self._toposort, '2': self._project, '3': self._load}
        isRunning = True

        while isRunning:
            self._printMenu()
            command = input('>> ')

            if command in commandDict:
                commandDict[command]()
            elif command == '0':
                isRunning = False
            else:
                print('\nInvalid command\n')