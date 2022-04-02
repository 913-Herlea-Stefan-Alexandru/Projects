
class Snake:
    def __init__(self, head, body1, body2):
        self._body = [head, body1, body2]
        self._direction = 'up'

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    @property
    def body(self):
        return self._body

    @property
    def head(self):
        return self._body[0].copy()

    def expand(self, head):
        self._body.append(0)
        i = len(self._body)-1
        while i > 0:
            self._body[i] = self._body[i-1]
            i -= 1
        self._body[0] = head

    def move(self, head):
        i = len(self._body) - 1
        while i > 0:
            self._body[i] = self._body[i - 1]
            i -= 1
        self._body[0] = head

    def __len__(self):
        return len(self._body)