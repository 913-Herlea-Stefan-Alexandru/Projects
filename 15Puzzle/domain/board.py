

class Board:
    def __init__(self, n):
        self._n = n
        self._board = [[-1 for j in range(n)] for i in range(n)]

    @property
    def n(self):
        return self._n

    def search(self, val):
        for i in range(self._n):
            for j in range(self._n):
                if self._board[i][j] == val:
                    return i, j
        return None

    def change_value(self, x, y, val=0):
        if x < 0 or x >= self._n or y < 0 or y >= self._n:
            return False
        if val not in list(range(self._n*self._n)):
            return False
        for i in range(self._n):
            for j in range(self._n):
                if self._board[i][j] == val:
                    self._board[i][j] = 0
        self._board[x][y] = val
        return True

    def copy(self):
        b = Board(self._n)
        for i in range(self._n):
            for j in range(self._n):
                b.change_value(i, j, self._board[i][j])
        return b

    def get_manhattan_dist(self):
        h = 0
        for i in range(self._n):
            for j in range(self._n):
                e = self._board[i][j]
                if e == 0:
                    continue
                if e != i * self._n + j + 1:
                    c = (e % self._n - 1 if e % self._n != 0 else self._n - 1)
                    l = int((e - c - 1) / self._n)
                    h += abs(i - l) + abs(j - c)
        return h

    def get_linear_conflict(self):
        con = 0
        for i in range(self._n):
            for j in range(self._n):
                e = self._board[i][j]
                c = (e % self._n - 1 if e % self._n != 0 else self._n - 1)
                l = int((e - c - 1) / self._n)
                if c == j:
                    if i - 1 >= 0:
                        e2 = self._board[i-1][j]
                        c2 = (e2 % self._n - 1 if e % self._n != 0 else self._n - 1)
                        l2 = int((e2 - c - 1) / self._n)
                        if c == c2:
                            if (i == l and j == c) or (i - 1 == l2 and j == c2):
                                con += 1
                    if i + 1 < self._n:
                        e2 = self._board[i+1][j]
                        c2 = (e2 % self._n - 1 if e % self._n != 0 else self._n - 1)
                        l2 = int((e2 - c - 1) / self._n)
                        if c == c2:
                            if (i == l and j == c) or (i + 1 == l2 and j == c2):
                                con += 1
                if l == i:
                    if j - 1 >= 0:
                        e2 = self._board[i][j-1]
                        c2 = (e2 % self._n - 1 if e % self._n != 0 else self._n - 1)
                        l2 = int((e2 - c - 1) / self._n)
                        if c == c2:
                            if (i == l and j == c) or (i == l2 and j-1 == c2):
                                con += 1
                    if j + 1 < self._n:
                        e2 = self._board[i][j+1]
                        c2 = (e2 % self._n - 1 if e % self._n != 0 else self._n - 1)
                        l2 = int((e2 - c - 1) / self._n)
                        if c == c2:
                            if (i == l and j == c) or (i == l2 and j+1 == c2):
                                con += 1
        return con


    def move(self):
        i, j = self.search(0)
        b1 = self.copy()
        b2 = self.copy()
        b3 = self.copy()
        b4 = self.copy()

        if i - 1 >= 0:
            b1.change_value(i, j, self._board[i-1][j])
        else:
            b1 = None
        if i + 1 < self._n:
            b2.change_value(i, j, self._board[i+1][j])
        else:
            b2 = None
        if j - 1 >= 0:
            b3.change_value(i, j, self._board[i][j-1])
        else:
            b3 = None
        if j + 1 < self._n:
            b4.change_value(i, j, self._board[i][j+1])
        else:
            b4 = None

        return [b1, b2, b3, b4]

    def check(self, other):
        for i in range(self._n):
            for j in range(self._n):
                if self._board[i][j] != other.get_elem(i, j):
                    return False
        return True

    def get_array(self):
        arr = []
        for i in range(self._n):
            for j in range(self._n):
                arr.append(self._board[i][j])
        return arr

    def get_elem(self, x, y):
        if x < 0 or x >= self._n or y < 0 or y >= self._n:
            return None
        return self._board[x][y]

    def __str__(self):
        string_format = ''

        for i in range(self._n):
            for j in range(self._n):
                string_format += str(self._board[i][j]) + ('  ' if self._board[i][j] < 10 else ' ')
            string_format += '\n'

        return string_format
