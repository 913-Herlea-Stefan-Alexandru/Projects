from domain.activity import Activity


class Graph:
    def __init__(self):
        self._vertex_dict_out = {}
        self._vertex_dict_in = {}
        self._edge_dict = {}

    def get_vertex(self, name):
        for v in self._vertex_dict_out:
            if v.name == name:
                return v

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

    def out_degree(self, x):
        """
        Returns the out degree of a given vertex
        :param x: the given vertex (int)
        :return: the out degree of the given vertex if it exists, None otherwise
        """
        if not self.check_vertex(x):
            return None
        return len(self._vertex_dict_out[x])

    def in_degree(self, x):
        """
        Returns the in degree of a given vertex
        :param x: the given vertex (int)
        :return: the in degree of the given vertex if it exists, None otherwise
        """
        if not self.check_vertex(x):
            return None
        return len(self._vertex_dict_in[x])

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
        return len(self._vertex_dict_out)

    def get_edge_count(self):
        """
        Returns the number of edges in the graph
        :return: the number of edges in the graph (int)
        """
        return len(self._edge_dict)

    def __str__(self):
        """
        Returns a readable string version of the graph
        :return: a string version of the graph (str)
        """
        string_format = ''

        for x in self.parseX():
            if self._vertex_dict_out[x] == []:
                string_format += str(x) + '\n'
                continue
            for y in self.parseNOut(x):
                i = self.get_info(x, y)
                string_format += str(x) + ' -> ' + str(y) + ' ' + (str(i) if i != 0 else '') + '\n'
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
