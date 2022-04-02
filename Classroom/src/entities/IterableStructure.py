
class Iterable:
    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def index(self, item):
        return self._list.index(item)

    def __getitem__(self, index):
        if index < len(self):
            return self._list[index]

    def __setitem__(self, key, value):
        if value != None:
            self._list[key] = value

    def __add__(self, other):
        self._list.append(other)

    def __delitem__(self, key = None):
        if key == None:
            self._list.pop()
        else:
            self._list.pop(key)

    def __iter__(self):
        self._index = -1
        return self

    def __next__(self):
        if self._index+1 < len(self):
            self._index += 1
            return self._list[self._index]
        else:
            raise StopIteration

def gnome_sort(array, function, upperBound):
    '''
    It moves the element at the position given by the upperBound in the array to the left until the condition of the
    sort is not met anymore or it gets into the first position of the array, then the function exits.
    :param array: the array to sort (list)
    :param function: the function giving the sorting conditions
    :param upperBound: the initial position of the element that has to be moved (integer)
    :return: -
    '''
    while upperBound > 0 and function(array[upperBound-1]) < function(array[upperBound]):
        array[upperBound-1], array[upperBound] = array[upperBound], array[upperBound-1]
        upperBound -= 1

def sort(array, function):
    '''
    The function takes each element except for the first one of the array and moves it to the left if the given
    conditions are met.
    :param array: the array to sort (list)
    :param function: the function giving the sorting conditions
    :return: -
    '''
    for i in range(len(array)):
        gnome_sort(array, function, i)

def filter(array, function):
    good_list = []
    for item in array:
        if function(item):
            good_list.append(item)
    return good_list