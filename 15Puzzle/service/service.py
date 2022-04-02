from domain.board import Board
from domain.graph import Graph
from domain.priorityQueue import PriorityQ
import random

class Service:
    def __init__(self):
        self._n = 4
        self._b = Board(self._n)
        self._result = Board(self._n)

        self._graph = Graph()

        for i in range(self._n):
            for j in range(self._n):
                if i == self._n-1 and j == self._n-1:
                    self._result.change_value(i, j, 0)
                    break
                self._result.change_value(i, j, i * self._n + j + 1)

        self._graph.add_vertex(self._b)

    def read_board(self, file_name):
        f = open(file_name, "r")
        l = 0
        for line in f:
            tokens = line.split(" ")

            if len(tokens) == 1:
                self._n = int(tokens[0])

                self._b = Board(self._n)
                self._result = Board(self._n)

                self._graph = Graph()

                for i in range(self._n):
                    for j in range(self._n):
                        if i == self._n - 1 and j == self._n - 1:
                            self._result.change_value(i, j, 0)
                            break
                        self._result.change_value(i, j, i * self._n + j + 1)

                self._graph.add_vertex(self._b)

                continue
            elif len(tokens) != self._n:
                raise ValueError("Wrong file format")
            elif l >= self._n:
                raise ValueError("Wrong file format")
            else:
                for c in range(self._n):
                    self._b.change_value(l, c, int(tokens[c]))
                l += 1
        f.close()
        return self._b

    def generate_random_board(self, n):
        self._n = n

        self._b = Board(self._n)
        self._result = Board(self._n)

        self._graph = Graph()

        for i in range(self._n):
            for j in range(self._n):
                if i == self._n - 1 and j == self._n - 1:
                    self._result.change_value(i, j, 0)
                    break
                self._result.change_value(i, j, i * self._n + j + 1)

        self._graph.add_vertex(self._b)

        i = 0
        j = 0

        while i < self._n:
            while j < self._n:
                x = random.choice(list(range(self._n*self._n)))
                if self._b.search(x) != None:
                    continue
                if not self._b.change_value(i, j, x):
                    continue
                j += 1
            i += 1
            j = 0

        return self._b

    def solve(self):
        arr = self._b.get_array()
        count = 0
        for i in range(len(arr) - 1):
            if arr[i] == 0:
                continue
            for j in range(i + 1, len(arr)):
                if arr[j] == 0:
                    continue
                if arr[i] > arr[j]:
                    count += 1
        if self._b.n % 2 == 1:
            if count % 2 == 1:
                return "Unsolvable"
        else:
            x, y = self._b.search(0)
            if x % 2 == 0:
                if count % 2 == 0:
                    return "Unsolvable"
            else:
                if count % 2 == 1:
                    return "Unsolvable"
        pq = PriorityQ()
        priority = {}
        prev = {}
        priority[self._b] = self._b.get_manhattan_dist()
        prev[self._b] = None
        pq.insert((self._b, priority[self._b], 0))
        end = None
        while not pq.isEmpty():
            b, h, g = pq.delete()
            if b.check(self._result):
                end = b
                break
            g += 1
            boards = b.move()
            for board in boards:
                if board != None:
                    hb = board.get_manhattan_dist()
                    hb += g
                    ok = None
                    for br in priority:
                        if board.check(br):
                            ok = br
                            break
                    if ok == None or priority[ok] > hb:
                        prev[board if ok == None else ok] = b
                        priority[board if ok == None else ok] = hb
                        pq.insert((board if ok == None else ok, hb, g))
        p = end
        b_arr = []
        while p != None:
            b_arr.append(p)
            p = prev[p]
        b_arr.reverse()
        self._graph = Graph()
        self._graph.add_vertex(self._b)
        for i in range(1, len(b_arr)):
            self._graph.add_vertex(b_arr[i])
            self._graph.add_edge(b_arr[i-1], b_arr[i])
        return "Solved"

    def print_graph(self):
        return self._graph.parseX()
