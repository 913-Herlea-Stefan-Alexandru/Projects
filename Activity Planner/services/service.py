from domain.graph import Graph
from domain.activity import Activity

class Service:
    def __init__(self, graph):
        self._graph = graph

    def deleteGraph(self):
        for v in self._graph.parseX():
            self._graph.remove_vertex(v)

    def load(self, fn):
        f = open(fn, "r")

        self.deleteGraph()

        for line in f:
            if ':' not in line:
                tokens = line.strip().split(',')
                ver = Activity(tokens[0], int(tokens[1]))
                self._graph.add_vertex(ver)
            else:
                tokens = line.split(':')
                x = self._graph.get_vertex(tokens[0])
                prereq = tokens[1].strip().split(',')
                for p in prereq:
                    y = self._graph.get_vertex(p)
                    self._graph.add_edge(y, x)

        f.close()
        print(self._graph)

    def save(self, fn):
        pass

    def tarjans(self):
        result = []
        visited = {}
        for v in self._graph.parseX():
            visited[v] = False

        for v in visited:
            if visited[v] == False:
                err = self.visit(v, visited, result, [])
        return result

    def visit(self, vertex, visited, result, processing):
        if vertex in processing:
            raise ValueError("\nGraph is not DAG\n")
        processing.append(vertex)
        if visited[vertex] == False:
            for n in self._graph.parseNOut(vertex):
                self.visit(n, visited, result, processing)
            visited[vertex] = True
            result.insert(0, vertex)
        processing.pop(processing.index(vertex))

    def project(self):
        res = self.tarjans()
        start = Activity('Start', 0)
        end = Activity('End', 0)
        self._graph.add_vertex(start)
        self._graph.add_vertex(end)
        for ver in self._graph.parseX():
            if self._graph.in_degree(ver) == 0 and ver != start:
                self._graph.add_edge(start, ver)
            if self._graph.out_degree(ver) == 0 and ver != end:
                self._graph.add_edge(ver, end)
        res.insert(0, start)
        res.append(end)

        ms = {}
        me = {}
        ms[start] = 0
        me[start] = 0

        for i in range(1, len(res)):
            ms[res[i]] = max([me[v] for v in self._graph.parseNIn(res[i])])
            me[res[i]] = ms[res[i]] + res[i].duration

        Ms = {}
        Me = {}
        Me[end] = me[end]
        Ms[end] = Me[end] - end.duration

        for i in range(len(res)-2, 0, -1):
            Me[res[i]] = min([Ms[v] for v in self._graph.parseNOut(res[i])])
            Ms[res[i]] = Me[res[i]] - res[i].duration

        return res, ms, me, Ms, Me
