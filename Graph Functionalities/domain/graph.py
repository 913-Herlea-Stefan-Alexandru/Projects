import random


class Graph:
    def __init__(self, type='d', vertexes=0):
        """
        Generates a graph with the given number of vertexes
        :param vertexes: the number od vertexes
        :raises ValueError: if the number of vertexes given is < 0
        """
        if vertexes < 0:
            raise ValueError("\nNumber of vertexes should be >= 0\n")

        self._vertexes = vertexes
        self._type = type

        self._vertex_dict_out = {}
        self._vertex_dict_in = {}
        self._edge_dict = {}

        self._matrix = {}
        self._path = {}

        for x in range(vertexes):
            self._vertex_dict_out[x] = []
            self._vertex_dict_in[x] = []

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, t):
        self._type = t

    def parseX(self):
        """
        Returns a list with all the vertexes in the graph
        :return: a list with all the vertexes in the graph (list of int)
        Thetea(n)
        """
        return [x for x in self._vertex_dict_out]

    def parseNOut(self, x):
        """
        Returns all the outbound neighbours of the given vertex x as a list
        :param x: the given vertex (int)
        :return: a list of all the outbound neighbours of x (list of int)
        O(n)
        """
        if not self.check_vertex(x):
            return []
        return self._vertex_dict_out[x].copy()

    def parseNIn(self, x):
        """
        Returns all the inbound neighbours of the given vertex x as a list
        :param x: the given vertex (int)
        :return: a list of all the inbound neighbours of x (list of int)
        O(n)
        """
        if not self.check_vertex(x):
            return []
        return self._vertex_dict_in[x].copy()

    def add_edge(self, x, y, val=0):
        """
        Adds an edge to the graph between the given coordinates and with a given value
        :param x: the source vertex (int)
        :param y: the destination vertex (int)
        :param val: the cost/information of the edge (int)
        :return: True if the edge can be added, False if the edge already exists
        O(n)
        """
        if self.check_edge(x, y) or not self.check_vertex(x) or not self.check_vertex(y):
            return False
        self._vertex_dict_out[x].append(y)
        self._vertex_dict_in[y].append(x)
        self._edge_dict[(x, y)] = val
        return True

    def remove_edge(self, x, y):
        """
        Removes the edge between the given vertexes
        :param x: the source vertex (int)
        :param y: the destination vertex (int)
        :return: True if the edge can be removed, False if the edge does not exist
        O(n)
        """
        if not self.check_edge(x, y):
            return False
        self._edge_dict.pop((x, y))
        self._vertex_dict_out[x].pop(self._vertex_dict_out[x].index(y))
        self._vertex_dict_in[y].pop(self._vertex_dict_in[y].index(x))
        return True

    def add_vertex(self, x):
        """
        Adds the given vertex to the graph
        :param x: the given vertex (int)
        :return: True if the vertex has been added, False if the vertex already exists
        """
        if self.check_vertex(x):
            return False
        self._vertex_dict_out[x] = []
        self._vertex_dict_in[x] = []
        self._vertexes += 1
        return True

    def remove_vertex(self, x):
        """
        Removes a given vertex from the graph
        :param x: the given vertex (int)
        :return: True if the vertex has been removed, False if the vertex does not exist
        O(dict_out(n) + dict_in(n))1

        """
        if not self.check_vertex(x):
            return False
        for y in self._vertex_dict_out[x]:
            self._vertex_dict_in[y].pop(self._vertex_dict_in[y].index(x))
            self._edge_dict.pop((x, y))
        for y in self._vertex_dict_in[x]:
            self._vertex_dict_out[y].pop(self._vertex_dict_out[y].index(x))
            self._edge_dict.pop((y, x))
        self._vertex_dict_out.pop(x)
        self._vertex_dict_in.pop(x)
        self._vertexes -= 1
        return True

    def get_info(self, x, y):
        """
        Returns the cost/info stored on the edge given by the vertexes x and y
        :param x: the source vertex (int)
        :param y: the destination vertex (int)
        :return: The information if the edge exists, None otherwise
        """
        if not self.check_edge(x, y):
            return None
        return self._edge_dict[(x, y)]

    def set_edge(self, x, y, val):
        """
        Modifies the cost/info at the given edge
        :param x: the source vertex (int)
        :param y: the destination vertex (int)
        :param val: the new cost/information of the edge (int)
        :return: True if the cost/information has been changed, False if the edge does not exist
        """
        if not self.check_edge(x, y):
            return False
        self._edge_dict[(x, y)] = val
        return True

    def in_degree(self, x):
        """
        Returns the in degree of a given vertex
        :param x: the given vertex (int)
        :return: the in degree of the given vertex if it exists, None otherwise
        """
        if not self.check_vertex(x):
            return None
        return len(self._vertex_dict_in[x])

    def out_degree(self, x):
        """
        Returns the out degree of a given vertex
        :param x: the given vertex (int)
        :return: the out degree of the given vertex if it exists, None otherwise
        """
        if not self.check_vertex(x):
            return None
        return len(self._vertex_dict_out[x])

    def check_edge(self, x, y):
        """
        Checks if the given edge is in the graph
        :param x: the source vertex (int)
        :param y: the destination vertex (int)
        :return: True if it is in the graph, False otherwise
        """
        if (x, y) in self._edge_dict:
            return True
        return False

    def check_vertex(self, x):
        """
        Checks if the given vertex is in the graph
        :param x: the given vertex (int)
        :return: True if it is in the graph, False otherwise
        """
        if x in self._vertex_dict_out:
            return True
        return False

    def copy_graph(self):
        """
        Creates a copy of the current graph which does not modify it
        :return: a copy of the current graph
        """
        g_copy = Graph()
        for ver in self._vertex_dict_out:
            g_copy.add_vertex(ver)
        for edge in self._edge_dict:
            g_copy.add_edge(edge[0], edge[1], self._edge_dict[edge])
        return g_copy

    def get_vertex_count(self):
        """
        Returns the number of vertexes in the graph
        :return: the number of vertexes in the graph (int)
        """
        return self._vertexes

    def get_edge_count(self):
        """
        Returns the number of edges in the graph
        :return: the number of edges in the graph (int)
        """
        return len(self._edge_dict) if self._type == 'd' else int(len(self._edge_dict) / 2)

    def __str__(self):
        """
        Returns a readable string version of the graph
        :return: a string version of the graph (str)
        """
        string_format = ''

        for x in self.parseX():
            if self._vertex_dict_out[x] == [] and self._vertex_dict_in[x] == []:
                string_format += str(x) + '\n'
                continue
            for y in self.parseNOut(x):
                i = self.get_info(x, y)
                string_format += str(x) + ' ' + str(y) + ' ' + (str(i) if i != 0 else '') + '\n'
        return string_format

    def _get_children_str(self, v, visited, ident):
        """
        Returns a readable string format of the vertex with the given ident. for a tree
        :param v: the vertex (int)
        :param visited: the list of visited vertexes (list of int)
        :param ident: the ident. (str)
        :return: the readable string (str)
        """
        str_f = ident + str(v) + '\n'

        for ver in self._vertex_dict_out[v]:
            if ver not in visited:
                visited.append(ver)
                str_f += self._get_children_str(ver, visited, ident + '\t')

        return str_f

    def print_undirected(self):
        string_format = ''

        visited = []

        for x in self.parseX():
            if self._vertex_dict_out[x] == [] and self._vertex_dict_in[x] == []:
                string_format += str(x) + '\n'
                continue
            for y in self.parseNOut(x):
                if (x, y) not in visited and (y, x) not in visited:
                    visited.append((x, y))
                    i = self.get_info(x, y)
                    string_format += str(x) + ' ' + str(y) + ' ' + (str(i) if i != 0 else '') + '\n'
        return string_format

    def print_graph(self):
        """
        Returns a readable tree created from the current graph
        :return: (str)
        """
        i = 0
        while self._vertex_dict_out[i] == []:
            i += 1

        string_format = str(self.parseX()[i]) + '\n'
        visited = [i]

        for v in self._vertex_dict_out[0]:
            if v not in visited:
                visited.append(v)
                string_format += self._get_children_str(v, visited, '\t')

        return string_format

    def build_matrix(self):
        """
        Builds the graph in the form of a matrix, and also builds it's path matrix
        :return:
        """
        self._matrix = {}
        self._path = {}
        for v in self.parseX():
            self._matrix[v] = {}
            self._path[v] = {}
            for w in self.parseX():
                if v == w:
                    self._matrix[v][w] = 0
                    self._path[v][w] = -1
                elif (v, w) not in self._edge_dict:
                    self._matrix[v][w] = float('inf')
                    self._path[v][w] = -1
                else:
                    self._matrix[v][w] = self._edge_dict[(v, w)]
                    self._path[v][w] = v

    def print_matrices(self):
        """
        Prints the walk matrix and the path matrix in their current states
        :return:
        """
        line = '     '
        for v in self._matrix:
            line += str(v).rjust(3) + ' '
        line += '  ' + line
        print(line)
        print('     ' + ''.join(['-' for i in range(len(line)-5)]))
        for v in self._matrix:
            line = str(v).rjust(3) + '| '
            for w in self._matrix:
                line += str(self._matrix[v][w]).rjust(3) + ' '
            line += '   |   '
            for w in self._matrix:
                line += str(self._path[v][w]).rjust(3) + ' '
            print(line + '|' + str(v))
        print()

    def Floyd_Warshall(self, x, y):
        """
        Computes the walk matrix and the path matrix using the Floyd-Warshall algorithm and returns the minimum cost
        walk between the two given vertices
        :param x: (int) the source vertex
        :param y: (int) the destination vertex
        :return: (list of int) the minimum cost walk between the two vertices if there is a walk between them or
        None if there is no walk between them
        """
        self.build_matrix()

        self.print_matrices()

        for k in self._matrix:
            for i in self._matrix:
                for j in self._matrix[i]:
                    if j == k or i == k or self._matrix[i][k] == -1 or self._matrix[k][j] == -1:
                        continue
                    if self._matrix[i][j] > self._matrix[i][k] + self._matrix[k][j] or self._matrix[i][j] == float('inf'):
                        self._matrix[i][j] = self._matrix[i][k] + self._matrix[k][j]
                        self._path[i][j] = self._path[k][j]
            self.print_matrices()

        for v in self._matrix:
            if self._matrix[v][v] < 0:
                raise ValueError("Negative cost cycle found")

        if self._path[x][y] == -1:
            raise ValueError("No path found")
        ver = self.parseX()
        path = [0 for i in range(len(ver))]

        k = len(ver) - 1
        path[k] = y

        while path[k] != x and k > 0:
            path[k - 1] = self._path[x][path[k]]
            k -= 1

        return path[k:], self._matrix[x][y]
