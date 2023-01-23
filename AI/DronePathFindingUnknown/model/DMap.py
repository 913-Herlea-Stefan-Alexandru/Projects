import pygame
import numpy as np
from model.constants import *
from math import sqrt
from collections import deque

class DMap():
    def __init__(self):
        self.__n = 20
        self.__m = 20
        self.surface = np.zeros((self.__n, self.__m))
        for i in range(self.__n):
            for j in range(self.__m):
                self.surface[i][j] = -1

    def markDetectedWalls(self, e, x, y):
        #   To DO
        # mark on this map the wals that you detect
        wals = e.readUDMSensors(x, y)
        self.surface[x][y] = 0
        i = x - 1
        if wals[UP] > 0:
            while ((i >= 0) and (i >= x - wals[UP])):
                self.surface[i][y] = 0
                i = i - 1
        if (i >= 0):
            self.surface[i][y] = 1

        i = x + 1
        if wals[DOWN] > 0:
            while ((i < self.__n) and (i <= x + wals[DOWN])):
                self.surface[i][y] = 0
                i = i + 1
        if (i < self.__n):
            self.surface[i][y] = 1

        j = y + 1
        if wals[LEFT] > 0:
            while ((j < self.__m) and (j <= y + wals[LEFT])):
                self.surface[x][j] = 0
                j = j + 1
        if (j < self.__m):
            self.surface[x][j] = 1

        j = y - 1
        if wals[RIGHT] > 0:
            while ((j >= 0) and (j >= y - wals[RIGHT])):
                self.surface[x][j] = 0
                j = j - 1
        if (j >= 0):
            self.surface[x][j] = 1

        return None

    def bfs(self, start, parent):
        dist = {}
        q = deque()

        q.append(start)
        parent[start] = (-1, -1)
        dist[start] = 0

        while q:
            u = q[0]
            q.popleft()

            v1 = (u[0]+1, u[1])
            v2 = (u[0]-1, u[1])
            v3 = (u[0], u[1]+1)
            v4 = (u[0], u[1]-1)

            if v1[0] < 20 and self.surface[v1[0]][v1[1]] == 0:
                if v1 not in dist or dist[v1] > dist[u] + 1:
                    dist[v1] = dist[u] + 1
                    q.append(v1)
                    parent[v1] = u
                elif dist[v1] == dist[u] + 1:
                    parent[v1] = u
            if v2[0] >= 0 and self.surface[v2[0]][v2[1]] == 0:
                if v2 not in dist or dist[v2] > dist[u] + 1:
                    dist[v2] = dist[u] + 1
                    q.append(v2)
                    parent[v2] = u
                elif dist[v2] == dist[u] + 1:
                    parent[v2] = u
            if v3[1] < 20 and self.surface[v3[0]][v3[1]] == 0:
                if v3 not in dist or dist[v3] > dist[u] + 1:
                    dist[v3] = dist[u] + 1
                    q.append(v3)
                    parent[v3] = u
                elif dist[v3] == dist[u] + 1:
                    parent[v3] = u
            if v4[1] >= 0 and self.surface[v4[0]][v4[1]] == 0:
                if v4 not in dist or dist[v4] > dist[u] + 1:
                    dist[v4] = dist[u] + 1
                    q.append(v4)
                    parent[v4] = u
                elif dist[v4] == dist[u] + 1:
                    parent[v4] = u

    def closestReachable(self, dx, dy):
        searchArea = 1

        while searchArea < self.__n:
            mx = dx + searchArea
            lx = dx - searchArea
            for y in range(dy-searchArea, dy+searchArea+1):
                if y < 0 or y > 19:
                    continue
                if mx <= 19 and self.surface[mx][y] == 0:
                    if self.canGetTo(mx, y):
                        return mx, y
                if lx >= 0 and self.surface[lx][y] == 0:
                    if self.canGetTo(lx, y):
                        return lx, y

            my = dy + searchArea
            ly = dy - searchArea
            for x in range(dx-searchArea, dx+searchArea+1):
                if x < 0 or x > 19:
                    continue
                if my <= 19 and self.surface[x][my] == 0:
                    if self.canGetTo(x, my):
                        return x, my
                if ly >= 0 and self.surface[x][ly] == 0:
                    if self.canGetTo(x, ly):
                        return x, ly

            searchArea += 1
        return None, None

    def shortestDist(self, fx, fy, l):
        dist = []
        for point in l:
            dist.append(sqrt((fx-point[0])**2 + (fy-point[1])**2))
        return dist.index(min(dist))


    def canGetTo(self, x, y):
        xf = x - 1
        while ((xf >= 0) and (self.surface[xf][y] == 0)):
            xf = xf - 1
        if xf >= 0 and self.surface[xf][y] == -1:
            return True
        # DOWN
        xf = x + 1
        while ((xf < self.__n) and (self.surface[xf][y] == 0)):
            xf = xf + 1
        if xf < self.__n and self.surface[xf][y] == -1:
            return True
        # LEFT
        yf = y + 1
        while ((yf < self.__m) and (self.surface[x][yf] == 0)):
            yf = yf + 1
        if yf < self.__m and self.surface[x][yf] == -1:
            return True
        # RIGHT
        yf = y - 1
        while ((yf >= 0) and (self.surface[x][yf] == 0)):
            yf = yf - 1
        if yf >= 0 and self.surface[x][yf] == -1:
            return True

        return False

    def image(self, x, y):

        imagine = pygame.Surface((420, 420))
        brick = pygame.Surface((20, 20))
        empty = pygame.Surface((20, 20))
        empty.fill(WHITE)
        brick.fill(BLACK)
        imagine.fill(GRAYBLUE)

        for i in range(self.__n):
            for j in range(self.__m):
                if (self.surface[i][j] == 1):
                    imagine.blit(brick, (j * 20, i * 20))
                elif (self.surface[i][j] == 0):
                    imagine.blit(empty, (j * 20, i * 20))

        drona = pygame.image.load("drona.png")
        imagine.blit(drona, (y * 20, x * 20))
        return imagine