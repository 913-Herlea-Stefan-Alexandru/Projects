from texttable import Texttable
import random
from entities.snake import Snake

class BoardError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Board:
    def __init__(self, size, apple_number):
        self._grid = [[0 for i in range(size)] for j in range(size)]
        self._size = size
        self._grid[self._size//2-1][self._size//2] = 2
        self._grid[self._size//2][self._size//2] = 3
        self._grid[self._size//2+1][self._size//2] = 3
        self._snake = Snake([self._size//2-1, self._size//2], [self._size//2, self._size//2],
                            [self._size//2+1, self._size//2])
        self._apple_number = apple_number
        self._current_aplle_number = 0
        self.generate_apples()

    def _can_generate_apple(self):
        for i in range(self._size):
            for j in range(self._size):
                if self._grid[i][j] != 0:
                    continue
                if j != self._size - 1 and self._grid[i][j + 1] == 1:
                    continue
                if j != 0 and self._grid[i][j - 1] == 1:
                    continue
                if i != self._size - 1 and self._grid[i + 1][j] == 1:
                    continue
                if i != 0 and self._grid[i - 1][j] == 1:
                    continue
                return True
        return False

    def _random_generator(self):
        ok = False
        i = j = None
        while not ok:
            i = random.randint(0, self._size-1)
            j = random.randint(0, self._size-1)
            if self._grid[i][j] != 0:
                continue
            if j != self._size-1 and self._grid[i][j+1] == 1:
                continue
            if j != 0 and self._grid[i][j-1] == 1:
                continue
            if i != self._size-1 and self._grid[i+1][j] == 1:
                continue
            if i != 0 and self._grid[i-1][j] == 1:
                continue
            ok = True
        return i, j

    def generate_apples(self):
        while self._current_aplle_number < self._apple_number:
            if not self._can_generate_apple():
                break
            i, j = self._random_generator()
            self._grid[i][j] = 1
            self._current_aplle_number += 1

    def change_direction(self, new_direction):
        if self._snake.direction == new_direction:
            return True
        if self._snake.direction == 'up' and new_direction == 'down':
            raise BoardError('\nBad move\n')
        if self._snake.direction == 'down' and new_direction == 'up':
            raise BoardError('\nBad move\n')
        if self._snake.direction == 'left' and new_direction == 'right':
            raise BoardError('\nBad move\n')
        if self._snake.direction == 'right' and new_direction == 'left':
            raise BoardError('\nBad move\n')

        self._snake.direction = new_direction
        return self.move(1)

    def _out_of_bounds(self, x, y):
        if x < 0 or x > self._size-1 or y < 0 or y > self._size-1:
            return True
        return False

    def _hit_body(self, x, y):
        if self._grid[x][y] == 3:
            return True
        return False

    def _redraw_snake(self, head):
        body = self._snake.body

        for component in body:
            self._grid[component[0]][component[1]] = 3

        self._grid[head[0]][head[1]] = 2

    def move(self, n):
        what_to_add = [0, 0]
        if self._snake.direction == 'up':
            what_to_add = [-1, 0]
        elif self._snake.direction == 'down':
            what_to_add = [1, 0]
        elif self._snake.direction == 'left':
            what_to_add = [0, -1]
        elif self._snake.direction == 'right':
            what_to_add = [0, 1]

        for i in range(n):
            head = self._snake.head

            head[0] += what_to_add[0]
            head[1] += what_to_add[1]

            tail_end = self._snake.body[-1]

            if self._out_of_bounds(head[0], head[1]):
                return False
            if self._hit_body(head[0], head[1]) and head != tail_end:
                return False

            if self._grid[head[0]][head[1]] == 1:
                self._current_aplle_number -= 1
                self._snake.expand(head)
                self._redraw_snake(head)
                self.generate_apples()
            else:
                body = self._snake.body
                self._grid[body[-1][0]][body[-1][1]] = 0
                self._snake.move(head)
                self._redraw_snake(head)

        return True

    def __str__(self):
        t = Texttable()

        for row in range(self._size):
            data = []
            for value in self._grid[row]:
                if value == 0:
                    data.append(' ')
                elif value == 1:
                    data.append('.')
                elif value == 2:
                    data.append('*')
                elif value == 3:
                    data.append('+')
            t.add_row(data)

        return t.draw()
