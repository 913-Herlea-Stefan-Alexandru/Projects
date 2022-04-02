from domain.graph import Graph
from domain.priorityQueue import PriorityQ
import random


class Service:
    def __init__(self):
        """
        Creates an empty graph and an empty copy variable
        """
        self._graph = Graph()
        self._copy_g = None

    def in_degree(self, x):
        x = int(x)
        if not self._graph.check_vertex(x):
            raise ValueError("\nVertex does not exist\n")
        return self._graph.in_degree(x)

    def out_degree(self, x):
        x = int(x)
        if not self._graph.check_vertex(x):
            raise ValueError("\nVertex does not exist\n")
        return self._graph.out_degree(x)

    def vertices_number(self):
        """
        :return: the number of vertices in the current graph
        """
        return self._graph.get_vertex_count()

    def edges_number(self):
        """
        :return: the number of edges in the current graph
        """
        return self._graph.get_edge_count()

    def parse_out(self, x):
        """
        :param x: the given vertex (str)
        :return: the outbound neighbours of the given vertex x (list of int)
        """
        x = int(x)
        return self._graph.parseNOut(x)

    def parse_in(self, x):
        """
        :param x: the given vertex (str)
        :return: the outbound neighbours of the given vertex x (list of int)
        """
        x = int(x)
        return self._graph.parseNIn(x)

    def parse_all(self):
        """
        :return: a list of all the vertexes in the graph (list of int)
        """
        return self._graph.parseX()

    def add_edge(self, x, y, val):
        """
        Adds an edge to the graph
        :param x: source vertex (str)
        :param y: destination vertex (str)
        :param val: cost/info of the edge (str)
        :return:
        :raises ValueError: if the edge already exists
        """
        if self._graph.type != 'd':
            raise ValueError("\nGraph must be directed\n")
        x = int(x)
        y = int(y)
        val = int(val)
        if not self._graph.add_edge(x, y, val):
            raise ValueError("\nEdge already created\n")

    def remove_edge(self, x, y):
        """
        Removes an edge from the graph
        :param x: source vertex (str)
        :param y: destination vertex (str)
        :return:
        :raises ValueError: if the edge does not exist
        """
        if self._graph.type != 'd':
            raise ValueError("\nGraph must be directed\n")
        x = int(x)
        y = int(y)
        if not self._graph.remove_edge(x, y):
            raise ValueError("\nEdge not found\n")

    def accessible(self, s, visited):
        """
        Finds the set of vertices of the graph that are accessible from the vertex s and returns the subgraph formed
        by them
        :return: a graph formed by the set of vertices of the graph that are accessible from the vertex s
        """
        g = Graph()
        acc = set()
        acc.add(s)
        g.add_vertex(s)
        list = [s]
        while len(list) > 0:
            x = list[0]
            list = list[1:]
            for y in self._graph.parseNOut(x):
                g.add_edge(x, y)
                g.add_edge(y, x)
                if y not in acc:
                    g.add_vertex(y)
                    acc.add(y)
                    list.append(y)
        visited += acc
        return g

    def connected(self):
        """
        Finds and returns a list of connected subgraphs of the main graph
        :return: a list of connected graphs
        """
        if self._graph.type != 'u':
            raise ValueError("\nGraph must be undirected\n")
        visited = []
        cc = []
        for v in self._graph.parseX():
            if v not in visited:
                cc.append(self.accessible(v, visited))
        return cc

    def add_edge_undirected(self, x, y):
        """
        Adds the given edge to an undirected graph
        :param x: vertex (str)
        :param y: vertex (str)
        :return:
        :raise ValueError: if the edge is already in the graph
        """
        if self._graph.get_edge_count() == 0:
            self._graph.type = 'u'
        if self._graph.type != 'u':
            raise ValueError("\nGraph must be undirected\n")
        x = int(x)
        y = int(y)
        if x == y:
            raise ValueError("\nThe source cannot be the same as the destination\n")
        if not self._graph.add_edge(x, y):
            raise ValueError("\nEdge already created\n")
        if not self._graph.add_edge(y, x):
            raise ValueError("\nEdge already created\n")

    def remove_edge_undirected(self, x, y):
        """
        Removes the given edge from an undirected graph
        :param x: vertex (str)
        :param y: vertex (str)
        :return:
        :raise ValueError: if the edge is not in the graph
        """
        if self._graph.get_edge_count() == 0:
            self._graph.type = 'u'
        if self._graph.type != 'u':
            raise ValueError("\nGraph must be undirected\n")
        x = int(x)
        y = int(y)
        if not self._graph.remove_edge(x, y):
            raise ValueError("\nEdge not found\n")
        if not self._graph.remove_edge(y, x):
            raise ValueError("\nEdge not found\n")

    def add_vertex(self, x):
        """
        Adds a vertex to the graph
        :param x: the vertex (str)
        :return:
        :raises ValueError: if the vertex is already in the graph
        """
        x = int(x)
        if not self._graph.add_vertex(x):
            raise ValueError("\nVertex already exists\n")

    def remove_vertex(self, x):
        """
        Removes a vertex from the graph
        :param x: the vertex (str)
        :return:
        :raises ValueError: if the vertex is not in the graph
        """
        x = int(x)
        if not self._graph.remove_vertex(x):
            raise ValueError("\nVertex not found\n")

    def modify_info(self, x, y, new_val):
        """
        Modifies the cost/information of a given edge
        :param x: source vertex (str)
        :param y: destination vertex (str)
        :param new_val: new cost/info of the edge (str)
        :return:
        :raises ValueError: if the edge does not exist
        """
        if self._graph.type != 'd':
            raise ValueError("\nGraph must be directed\n")
        x = int(x)
        y = int(y)
        new_val = int(new_val)

        if not self._graph.set_edge(x, y, new_val):
            raise ValueError("\nEdge does not exist\n")

    def delete_graph(self):
        """
        Deletes the current graph
        :return:
        """
        for x in self._graph.parseX():
            self._graph.remove_vertex(x)

    def copy_graph(self):
        """
        Copies the current graph into the copy variable
        :return:
        """
        self._copy_g = self._graph.copy_graph()

    def readable_undirected(self):
        """
        Returns a readable string of an undirected graph
        :return: str
        """
        if self._graph.type != 'u':
            raise ValueError("\nGraph must be undirected\n")
        return self._graph.print_undirected()

    def read_from_file_undirected(self, file_name):
        """
        Reads an undirected graph from the given file
        :param file_name: (str)
        :return:
        """
        f = open(file_name, "r")

        self.delete_graph()

        self._graph.type = 'u'

        for line in f:
            tokens = line.split(" ")

            if len(tokens) == 1:
                x = int(tokens[0])
                if not self._graph.check_vertex(x):
                    self._graph.add_vertex(x)
                continue
            if len(tokens) == 2:
                n = int(tokens[0])
                m = int(tokens[1])

                for i in range(n):
                    self._graph.add_vertex(i)
            else:
                x = int(tokens[0])
                y = int(tokens[1])

                if not self._graph.check_vertex(x):
                    self._graph.add_vertex(x)
                if not self._graph.check_vertex(y):
                    self._graph.add_vertex(y)
                self._graph.add_edge(x, y)
                self._graph.add_edge(y, x)

        f.close()

    def read_from_file(self, file_name):
        """
        Reads a graph from a file
        :param file_name: (str)
        :return:
        :raises ValueError: if the number of edges given is too high
        """
        f = open(file_name, "r")

        self.delete_graph()

        self._graph.type = 'd'

        for line in f:
            tokens = line.split(" ")

            if len(tokens) == 2:
                n = int(tokens[0])
                m = int(tokens[1])
                if m > n * n:
                    raise ValueError("\nToo many edges\n")
                for x in range(n):
                    self._graph.add_vertex(x)
                continue
            if len(tokens) == 1:
                x = int(tokens[0])
                if not self._graph.check_vertex(x):
                    self._graph.add_vertex(x)
                continue

            x = int(tokens[0])
            y = int(tokens[1])
            val = int(tokens[2])

            if not self._graph.check_vertex(x):
                self._graph.add_vertex(x)
            if not self._graph.check_vertex(y):
                self._graph.add_vertex(y)
            self._graph.add_edge(x, y, val)

        f.close()

    def write_to_file(self, file_name):
        """
        Writes the current graph into a file
        :param file_name: (str)
        :return:
        """
        if self._graph.type == 'u':
            raise ValueError("Graph must be directed")
        f = open(file_name, "w")
        f.write(str(self._graph))
        f.close()

    def write_to_file_undirected(self, file_name):
        """
        Writes the current graph into a file
        :param file_name: (str)
        :return:
        """
        if self._graph.type != 'u':
            raise ValueError("Graph must be undirected")
        f = open(file_name, "w")
        f.write(self._graph.print_undirected())
        f.close()

    def generate_random(self, n, m):
        """
        Generates a random graph with the given number of vertexes and edges
        :param n: the number of vertexes (str)
        :param m: the number of edges (str)
        :return:
        :raises ValueError: if the number of edges is too high
        """
        self.delete_graph()
        n = int(n)
        m = int(m)

        if m > n * n:
            raise ValueError("\nToo many edges\n")

        for x in range(n):
            self._graph.add_vertex(x)
        while m > 0:
            x = random.choice(self._graph.parseX())
            y = random.choice(self._graph.parseX())

            if self._graph.check_edge(x, y):
                continue

            val = random.randint(1, 1000)
            self._graph.add_edge(x, y, val)
            m -= 1

    def generate_random_undirected(self, n, m):
        """
        Generates a random undirected graph with the given number of vertexes and edges
        :param n: the number of vertexes (str)
        :param m: the number of edges (str)
        :return:
        :raises ValueError: if the number of edges is too high
        """
        self.delete_graph()
        n = int(n)
        m = int(m)

        if m > n * (n-1) / 2:
            raise ValueError("\nToo many edges\n")

        self._graph.type = 'u'

        for x in range(n):
            self._graph.add_vertex(x)
        while m > 0:
            x = random.choice(self._graph.parseX())
            y = random.choice(self._graph.parseX())
            if x == y:
                continue

            if self._graph.check_edge(x, y):
                continue

            self._graph.add_edge(x, y)
            self._graph.add_edge(y, x)
            m -= 1

    def change_to_copy(self):
        """
        Sets the copy as the current graph
        :return:
        :raises ValueError: if the copy is empty
        """
        if self._copy_g != None:
            self._graph, self._copy_g = self._copy_g, self._graph
        else:
            raise ValueError("\nThe copy is empty\n")

    def dijkstra(self, beginning):
        if self._graph.type != 'd':
            raise ValueError("\nGraph must be directed\n")
        priorityQ = PriorityQ()
        dist = {}
        prev = {}
        for v in self._graph.parseX():
            dist[v] = None
            prev[v] = None
        dist[beginning] = 0
        priorityQ.insert((beginning, dist[beginning]))
        while not priorityQ.isEmpty():
            v, d = priorityQ.delete()
            if d > dist[v]:
                print(str(v) + ' | ' + str(priorityQ) + ' | ' + str(dist) + ' | ' + str(prev))
                continue
            for x in self._graph.parseNOut(v):
                vx = self._graph.get_info(v, x)
                if dist[x] == None or dist[x] > dist[v] + vx:
                    prev[x] = v
                    dist[x] = dist[v] + vx
                    priorityQ.insert((x, dist[x]))
            print(str(v) + ' | ' + str(priorityQ) + ' | ' + str(dist) + ' | ' + str(prev))
        return prev

    def readable_graph(self):
        """
        :return: a readable format of the current graph (str)
        """
        if self._graph.type != 'd':
            raise ValueError("\nGraph must be directed\n")
        return str(self._graph)

    def get_graph(self):
        """
        :return: a readable tree version of the current graph (str)
        """
        if self._graph.type != 'd':
            raise ValueError("\nGraph must be directed\n")
        return self._graph.print_graph()

    def Floyd_Warshall(self, x, y):
        if self._graph.type != 'd':
            raise ValueError("\nGraph must be directed\n")
        x = int(x)
        y = int(y)
        if not self._graph.check_vertex(x) or not self._graph.check_vertex(y):
            raise ValueError("\nVertex not found\n")
        return self._graph.Floyd_Warshall(x, y)

    def mc_rec(self, r, p, x, res):
        """
        Determines all the cliques inside the graph
        :param r: the temporary result (list of int)
        :param p: the set of possible candidates (list of int)
        :param x: the excluded set (list of int)
        :param res: the set of results (list of list of int)
        :return:
        """
        if len(p) == 0 and len(x) == 0:
            print(r)
            res += [r]
        else:
            p1 = p.copy()
            for v in p:
                p2 = [val for val in self._graph.parseNOut(v) if val in p1]
                x2 = [val for val in self._graph.parseNOut(v) if val in x]
                self.mc_rec(r + [v], p2, x2, res)
                p1.pop(p1.index(v))
                x += [v]

    def max_clique(self):
        """
        Gets all the cliques from the graph and takes one of the the maximum ones
        :return: the maximum clique of the undirected graph
        """
        mx = 0
        res = []
        clique = []
        self.mc_rec([], self._graph.parseX(), [], res)
        for c in res:
            if len(c) > mx:
                mx = len(c)
                clique = c.copy()
        return clique
