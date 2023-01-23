from utils import *
from domain.map import Map
from domain.drone import Drone
from domain.colony import Colony
from service.service import Service
from gui import *
import pygame
import time
from random import randint

if __name__ == '__main__':
    service = Service()

    m = Map()
    m.loadMap("test1.map")

    x = randint(0, 19)
    y = randint(0, 19)

    d = Drone(x, y)

    sens = []

    noSensors = randint(4, 7)

    for i in range(noSensors):
        fX = randint(0, 19)
        fY = randint(0, 19)

        while m.isWall((fX, fY)) or not m.validatePos((fX, fY)) or m.isSensor((fX, fY)):
            fX = randint(0, 19)
            fY = randint(0, 19)

        sens.append((fX, fY))
        m.setSensor(fX, fY)

    viewMap(m)

    screen = initPyGame((m.n * 20, m.m * 20))

    sensorInfo = {}
    for i in range(len(sens)):
        sensorInfo[i] = {}

    for i in range(len(sens)):
        j = i + 1

        while j < len(sens):
            path = service.searchAStar(m, d, sens[i][0], sens[i][1], sens[j][0], sens[j][1])
            sensorInfo[i][j] = {}
            sensorInfo[i][j]['path'] = path
            sensorInfo[i][j]['distance'] = len(path)
            sensorInfo[j][i] = {}
            sensorInfo[j][i]['path'] = path[::-1]
            sensorInfo[j][i]['distance'] = len(path)

            # screen.blit(service.displayWithPath(m.image(), path), (0, 0))
            #
            # pygame.display.flip()
            # time.sleep(1)

            j += 1

    for i in range(len(sens)):
        seenCells = [0, 0, 0, 0, 0]
        for var in v:
            x = sens[i][0] + var[0]
            y = sens[i][1] + var[1]

            currentLength = 1

            while m.validatePos((x, y)) and not m.isWall((x, y)) and currentLength <= 5:
                if m.surface[x][y] != 2:
                    seenCells[currentLength - 1] += 1
                x = x + var[0]
                y = y + var[1]
                currentLength += 1
        for j in range(1, len(seenCells)):
            seenCells[j] += seenCells[j - 1]
        sensorInfo[i]['seenCells'] = seenCells
        en = 0
        mx = 0
        for e in range(len(seenCells)):
            if seenCells[e] > mx:
                mx = seenCells[e]
                en = e + 1
        sensorInfo[i]['bestRatio'] = (en, mx)
        print(sensorInfo[i]['seenCells'])
        print(sensorInfo[i]['bestRatio'])

    antParams = {'noSensors': noSensors, 'sensorInfo': sensorInfo}

    acoParams = {"noAnts": 10, "generations": 100}
    antParams['alpha'] = 5
    antParams['beta'] = 3
    antParams['pRate'] = 0.5
    antParams['pheromone'] = []
    antParams['q0'] = 0.01
    antParams['battery'] = 75

    col = Colony(antParams, acoParams)
    col.initialize()
    col.initializePheromone()

    theBestAnt = None

    for i in range(acoParams['generations']):
        col.explore()
        bestAnt = col.bestAnt()
        print("Generation " + str(i + 1) + "; best ant distance: " + str(bestAnt.distance()) + "; path: " + str(
            bestAnt.path))

        if theBestAnt == None or bestAnt.distance() < theBestAnt.distance():
            theBestAnt = bestAnt

        col.initialize()

    print("Best ant distance: " + str(theBestAnt.distance()))

    path = []

    sensorOrder = theBestAnt.path

    print("Battery left: ", theBestAnt.battery)
    print(sensorOrder)

    for i in range(1, len(sensorOrder)):
        path += sensorInfo[sensorOrder[i-1]][sensorOrder[i]]['path']
        if i < len(sensorOrder) - 1:
            path = path[:len(path) - 1]

    print(path)

    sens = theBestAnt.path
    remainingBattery = theBestAnt.battery

    energyLevels = {}
    for s in sens:
        energyLevels[s] = (0, 0)
    if remainingBattery <= 0:
        print(energyLevels)

    sens.sort(key=lambda s: sensorInfo[s]['bestRatio'][1])
    i = 0
    while i < len(sens) and remainingBattery > 0:
        currentSensorMaxEnergy = sensorInfo[sens[i]]['bestRatio'][0]
        if remainingBattery > currentSensorMaxEnergy:
            remainingBattery -= currentSensorMaxEnergy
            energyLevels[sens[i]] = (currentSensorMaxEnergy, sensorInfo[sens[i]]['seenCells'][currentSensorMaxEnergy-1])
        else:
            energyLevels[i] = (remainingBattery, sensorInfo[sens[i]]['seenCells'][remainingBattery-1])
            remainingBattery = 0
        i += 1

    print(energyLevels)

    movingDrone(m, path, 0.3, energyLevels)
