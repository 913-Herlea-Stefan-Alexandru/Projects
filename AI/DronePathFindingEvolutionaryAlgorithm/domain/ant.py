from random import randint, uniform
import random

class Ant:
    def __init__(self, antParams):
        self.__antParams = antParams
        startSensor = randint(0, self.__antParams['noSensors'] - 1)
        self.__antPath = [startSensor]
        self.__visited = [0 for _ in range(antParams['noSensors'])]
        self.__visited[self.__antPath[0]] = 1
        self.__battery = self.__antParams['battery']
        self.__inexistentPath = False

    @property
    def battery(self):
        return self.__battery

    @property
    def path(self):
        return self.__antPath

    def next(self):
        q = uniform(0, 1)
        currentSensor = self.__antPath[len(self.__antPath) - 1]

        if q < self.__antParams["q0"]:
            sum = 0
            nextSensorChoices = []
            for i in range(self.__antParams['noSensors']):
                if self.__visited[i] == 0 and i != currentSensor and self.__antParams['sensorInfo'][currentSensor][i]['distance'] != 0 and (self.__antParams['sensorInfo'][currentSensor][i]['distance'] <= self.__battery):
                    sum += pow(self.__antParams['pheromone'][currentSensor][i], self.__antParams["alpha"]) * pow(
                        1 / self.__antParams['sensorInfo'][currentSensor][i]['distance'], self.__antParams["beta"])
            # (pheromone[i][j]^alpha * 1/dist[i][j]^beta) / sum(pheromone[i][z]^alpha * 1/dist[i][z]^beta)
            for i in range(0, self.__antParams['noSensors']):
                if self.__visited[i] == 0 and i != currentSensor and self.__antParams['sensorInfo'][currentSensor][i]['distance'] != 0 and (self.__antParams['sensorInfo'][currentSensor][i]['distance'] <= self.__battery):
                    p = pow(self.__antParams['pheromone'][currentSensor][i], self.__antParams["alpha"]) * pow(
                        1 / self.__antParams['sensorInfo'][currentSensor][i]['distance'], self.__antParams["beta"])
                    nextSensorChoices.append((p / sum, i))

            if len(nextSensorChoices) == 0:
                raise Exception("No valid neighbour city")

            return random.choices([c[1] for c in nextSensorChoices], weights=[c[0] for c in nextSensorChoices], k=1)[0]
        else:
            nextSensorChoices = []
            for i in range(len(self.__antParams['pheromone'][currentSensor])):
                if i != currentSensor and self.__visited[i] == 0 and self.__antParams['sensorInfo'][currentSensor][i]['distance'] != 0 and (self.__antParams['sensorInfo'][currentSensor][i]['distance'] <= self.__battery):
                    p = pow(self.__antParams['pheromone'][currentSensor][i], self.__antParams["alpha"]) * pow(
                        1 / self.__antParams['sensorInfo'][currentSensor][i]['distance'], self.__antParams["beta"])
                    nextSensorChoices.append((p, i))

            if len(nextSensorChoices) == 0:
                raise Exception("No valid neighbour city")

            nextSensorChoices.sort()

            return nextSensorChoices[0][1]

    def explore(self):
        try:
            nextSensor = self.next()
        except:
            self.__inexistentPath = True
            return

        currentSensor = self.__antPath[len(self.__antPath) - 1]
        self.__visited[nextSensor] = 1
        self.__antPath.append(nextSensor)
        self.__battery -= self.__antParams['sensorInfo'][currentSensor][nextSensor]['distance']

        self.__antParams['pheromone'][currentSensor][nextSensor] = (1 - self.__antParams["pRate"]) * \
                                                                 self.__antParams["pheromone"][currentSensor][nextSensor] + \
                                                                 self.__antParams["pRate"] * \
                                                                 self.__antParams['sensorInfo'][currentSensor][nextSensor]['distance']
        self.__antParams['pheromone'][nextSensor][currentSensor] = self.__antParams['pheromone'][currentSensor][nextSensor]

    def distance(self):
        if self.__inexistentPath:
            return 999999
        dist = 0
        for i in range(len(self.__antPath) - 1):
            dist += self.__antParams['sensorInfo'][self.__antPath[i]][self.__antPath[i + 1]]['distance']
        #dist += self.__antParams['sensorInfo'][self.__antPath[len(self.__antPath) - 1]][self.__antPath[0]]['distance']
        return dist