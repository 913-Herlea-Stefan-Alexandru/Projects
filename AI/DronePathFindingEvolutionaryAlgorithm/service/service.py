from utils import *
from domain.cell import Cell
import pygame

class Service:

    def __init__(self):
        pass

    def isValid(self, x, y):
        if x >= 0 and x < 20 and y >= 0 and y < 20:
            return True
        return False

    def isBlocked(self, mapM, x, y):
        if mapM.surface[x][y] == 1:
            return True
        return False

    def isDestination(self, x, y, dest):
        if x == dest[0] and y == dest[1]:
            return True
        return False

    def manhattenDist(self, currentX, currentY, dest):
        return abs(currentX - dest[0]) + abs(currentY - dest[1])

    def getPath(self, cellDetails, dest):
        x = dest[0]
        y = dest[1]

        path = []

        while not (cellDetails[x][y].parentX == x and cellDetails[x][y].parentY == y):
            path.append([x, y])
            tempX = cellDetails[x][y].parentX
            tempY = cellDetails[x][y].parentY
            x = tempX
            y = tempY

        path.append([x, y])
        return path[::-1]

    def searchAStar(self, mapM, droneD, initialX, initialY, finalX, finalY):
        # TO DO
        # implement the search function and put it in controller
        # returns a list of moves as a list of pairs [x,y]

        print(
            "A* path from {source} to {destination}".format(source=(initialX, initialY), destination=(finalX, finalY)))

        if not self.isValid(initialX, initialY):
            print("Invalid source")
            return []

        if not self.isValid(finalX, finalY):
            print("Invalid destination")
            return []

        if self.isBlocked(mapM, initialX, initialY):
            print("Source is blocked")
            return []

        if self.isBlocked(mapM, finalX, finalY):
            print("Destination is blocked")
            return []

        if self.isDestination(initialX, initialY, (finalX, finalY)):
            print("Already at destination")
            return []

        closedList = [[False for i in range(20)] for j in range(20)]

        cellDetails = [[None for i in range(20)] for j in range(20)]

        for i in range(20):
            for j in range(20):
                cellDetails[i][j] = Cell("inf", "inf", "inf", -1, -1)

        cellDetails[initialX][initialY].f = 0
        cellDetails[initialX][initialY].g = 0
        cellDetails[initialX][initialY].h = 0
        cellDetails[initialX][initialY].parentX = initialX
        cellDetails[initialX][initialY].parentY = initialY

        openList = []

        openList.append((0, (initialX, initialY)))

        foundDest = False

        while not len(openList) == 0:
            p = openList[0]
            openList.remove(openList[0])

            x = p[1][0]
            y = p[1][1]
            closedList[x][y] = True

            newG = newH = newF = 0

            # -------------Up successor-----------------#

            if self.isValid(x - 1, y):
                if self.isDestination(x - 1, y, (finalX, finalY)):
                    cellDetails[x - 1][y].parentX = x
                    cellDetails[x - 1][y].parentY = y
                    print("Destination found")
                    foundDest = True
                    path = self.getPath(cellDetails, (finalX, finalY))
                    return path
                elif not closedList[x - 1][y] and not self.isBlocked(mapM, x - 1, y):
                    newG = cellDetails[x][y].g + 1
                    newH = self.manhattenDist(x - 1, y, (finalX, finalY))
                    newF = newG + newH

                    if cellDetails[x - 1][y].f == "inf" or cellDetails[x - 1][y].f > newF:
                        if (newF, (x - 1, y)) not in openList:
                            openList.append((newF, (x - 1, y)))

                        cellDetails[x - 1][y].f = newF
                        cellDetails[x - 1][y].g = newG
                        cellDetails[x - 1][y].h = newH
                        cellDetails[x - 1][y].parentX = x
                        cellDetails[x - 1][y].parentY = y

            # -------------Down successor-----------------#

            if self.isValid(x + 1, y):
                if self.isDestination(x + 1, y, (finalX, finalY)):
                    cellDetails[x + 1][y].parentX = x
                    cellDetails[x + 1][y].parentY = y
                    print("Destination found")
                    foundDest = True
                    return self.getPath(cellDetails, (finalX, finalY))
                elif not closedList[x + 1][y] and not self.isBlocked(mapM, x + 1, y):
                    newG = cellDetails[x][y].g + 1
                    newH = self.manhattenDist(x + 1, y, (finalX, finalY))
                    newF = newG + newH

                    if cellDetails[x + 1][y].f == "inf" or cellDetails[x + 1][y].f > newF:
                        if (newF, (x + 1, y)) not in openList:
                            openList.append((newF, (x + 1, y)))

                        cellDetails[x + 1][y].f = newF
                        cellDetails[x + 1][y].g = newG
                        cellDetails[x + 1][y].h = newH
                        cellDetails[x + 1][y].parentX = x
                        cellDetails[x + 1][y].parentY = y

            # -------------Left successor-----------------#

            if self.isValid(x, y - 1):
                if self.isDestination(x, y - 1, (finalX, finalY)):
                    cellDetails[x][y - 1].parentX = x
                    cellDetails[x][y - 1].parentY = y
                    print("Destination found")
                    foundDest = True
                    return self.getPath(cellDetails, (finalX, finalY))
                elif not closedList[x][y - 1] and not self.isBlocked(mapM, x, y - 1):
                    newG = cellDetails[x][y].g + 1
                    newH = self.manhattenDist(x, y - 1, (finalX, finalY))
                    newF = newG + newH

                    if cellDetails[x][y - 1].f == "inf" or cellDetails[x][y - 1].f > newF:
                        if (newF, (x, y - 1)) not in openList:
                            openList.append((newF, (x, y - 1)))

                        cellDetails[x][y - 1].f = newF
                        cellDetails[x][y - 1].g = newG
                        cellDetails[x][y - 1].h = newH
                        cellDetails[x][y - 1].parentX = x
                        cellDetails[x][y - 1].parentY = y

            # -------------Right successor-----------------#

            if self.isValid(x, y + 1):
                if self.isDestination(x, y + 1, (finalX, finalY)):
                    cellDetails[x][y + 1].parentX = x
                    cellDetails[x][y + 1].parentY = y
                    print("Destination found")
                    foundDest = True
                    return self.getPath(cellDetails, (finalX, finalY))
                elif not closedList[x][y + 1] and not self.isBlocked(mapM, x, y + 1):
                    newG = cellDetails[x][y].g + 1
                    newH = self.manhattenDist(x, y + 1, (finalX, finalY))
                    newF = newG + newH

                    if cellDetails[x][y + 1].f == "inf" or cellDetails[x][y + 1].f > newF:
                        if (newF, (x, y + 1)) not in openList:
                            openList.append((newF, (x, y + 1)))

                        cellDetails[x][y + 1].f = newF
                        cellDetails[x][y + 1].g = newG
                        cellDetails[x][y + 1].h = newH
                        cellDetails[x][y + 1].parentX = x
                        cellDetails[x][y + 1].parentY = y

        if not foundDest:
            print("Failed to find destination")

        return []

    def displayWithPath(self, image, path, color=GREEN):
        mark = pygame.Surface((20, 20))
        mark.fill(color)
        for move in path:
            image.blit(mark, (move[1] * 20, move[0] * 20))
        return image
