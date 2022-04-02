

class PriorityQ:
    def __init__(self):
        self._queue = []

    def isEmpty(self):
        return len(self._queue) == 0

    def func(self, elem):
        return elem[1]

    def insert(self, data):
        self._queue.append(data)
        self._queue.sort(key=self.func)

    def delete(self):
        if not self.isEmpty():
            return self._queue.pop(0)
        else:
            return None

    def __str__(self):
        return str(self._queue)
