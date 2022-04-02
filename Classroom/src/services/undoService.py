

class UndoService:
    def __init__(self):
        self._history = []
        self._index = -1

    def record(self, operation):
        '''
        Records the given Operation/CascadeOperations objects into the history of the service
        :param operation: (Operation/CascadeOperations) which contain the undo/redo operations for a given function
        :return: -
        '''
        self._history = self._history[:self._index+1]
        self._history.append(operation)
        self._index += 1

    def undo(self):
        '''
        Calls the undo functions for the given operations on the last position of the history list
        :return: False if there is no operation to undo or True if there is
        '''
        if self._index == -1:
            return False

        self._history[self._index].undo()
        self._index -= 1
        return True

    def redo(self):
        '''
        Calls the redo functions for the given operations on the next position of the history list
        :return: False if there is no operation to redo or True if there is
        '''
        if self._index == len(self._history) - 1:
            return False

        self._index += 1
        self._history[self._index].redo()
        return True


class CascadeOperations:
    '''
    Objects created from this class have a list of Operation type objects which for each we call the
    undo or redo functions
    '''
    def __init__(self, *operations):
        self._operations = operations

    def undo(self):
        for operation in self._operations:
            operation.undo()

    def redo(self):
        for operation in self._operations:
            operation.redo()


class Operation:
    '''
    Objects created from this class have FunctionCall type attributes which can be called to undo or redo an operation
    '''
    def __init__(self, undo_function, redo_function):
        self._undo_function = undo_function
        self._redo_function = redo_function

    def undo(self):
        self._undo_function()

    def redo(self):
        self._redo_function()


class FunctionCall:
    '''
    Objects created from this class have function attributes which can be called using the given parameters
    '''
    def __init__(self, function_name, *parameters):
        self._function_name = function_name
        self._parameters = parameters

    def __call__(self):
        self._function_name(*self._parameters)