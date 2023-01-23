from domain.ant import Ant

class Colony:
    def __init__(self, antParams, acoParams):
        self.__antParams = antParams
        self.__acoParams = acoParams
        self.__ants = []

    def initialize(self):
        self.__ants = []
        for _ in range(self.__acoParams["noAnts"]):
            self.__ants.append(Ant(self.__antParams))

    def initializePheromone(self):
        for i in range(self.__antParams['noSensors']):
            v = [1 for _ in range(self.__antParams['noSensors'])]
            self.__antParams['pheromone'].append(v)

    def bestAnt(self):
        best = self.__ants[0]
        for ant in self.__ants:
            if ant.distance() < best.distance():
                best = ant
        return best

    def placePheromone(self, ant):
        path = ant.path
        for i in range(len(path) - 1):
            x = path[i]
            y = path[i + 1]
            self.__antParams['pheromone'][x][y] = self.__antParams['pRate'] * self.__antParams['pheromone'][x][y] + \
                                                  self.__antParams['pRate'] * (1 / ant.distance())
            self.__antParams['pheromone'][y][x] = self.__antParams['pheromone'][x][y]

    def explore(self):
        for _ in range(self.__antParams['noSensors'] - 1):
            for ant in self.__ants:
                ant.explore()
        self.placePheromone(self.bestAnt())