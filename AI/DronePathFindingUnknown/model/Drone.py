import pygame
from pygame.locals import *
import numpy as np
from collections import deque

class Drone():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sourceX = x
        self.sourceY = y
        self.currentPath = deque()
        n = 20
        m = 20
        self.visited = np.zeros((n, m))
        self.step = 1

    def move(self, detectedMap):
        pressed_keys = pygame.key.get_pressed()
        if self.x > 0:
            if pressed_keys[K_UP] and detectedMap.surface[self.x - 1][self.y] == 0:
                self.x = self.x - 1
        if self.x < 19:
            if pressed_keys[K_DOWN] and detectedMap.surface[self.x + 1][self.y] == 0:
                self.x = self.x + 1

        if self.y > 0:
            if pressed_keys[K_LEFT] and detectedMap.surface[self.x][self.y - 1] == 0:
                self.y = self.y - 1
        if self.y < 19:
            if pressed_keys[K_RIGHT] and detectedMap.surface[self.x][self.y + 1] == 0:
                self.y = self.y + 1

    def shortestPath(self, detectedMap, x, y):
        parent = {}
        detectedMap.bfs((self.x, self.y), parent)
        self.currentPath.appendleft((x, y))
        dest = parent[(x, y)]
        while dest != (self.x, self.y):
            self.currentPath.appendleft(dest)
            dest = parent[dest]


    def moveDSF(self, detectedMap):
        self.visited[self.x][self.y] = self.step

        if not self.currentPath:
            destX, destY = detectedMap.closestReachable(self.x, self.y)
            if destX == None and destY == None:
                return 1
            self.shortestPath(detectedMap, destX, destY)

        self.x = self.currentPath[0][0]
        self.y = self.currentPath[0][1]

        self.currentPath.popleft()

        '''
        if self.x > 0 and detectedMap.surface[self.x - 1][self.y] == 0 and self.visited[self.x - 1][self.y] == 0:
            self.x = self.x - 1
        elif self.x < 19 and detectedMap.surface[self.x + 1][self.y] == 0 and self.visited[self.x + 1][self.y] == 0:
            self.x = self.x + 1
        elif self.y > 0 and detectedMap.surface[self.x][self.y - 1] == 0 and self.visited[self.x][self.y - 1] == 0:
            self.y = self.y - 1
        elif self.y < 19 and detectedMap.surface[self.x][self.y + 1] == 0 and self.visited[self.x][self.y + 1] == 0:
            self.y = self.y + 1
        else:
            for i in range(20):
                for j in range(20):
                    if self.visited[i][j] == self.step - 1:
                        self.visited[self.x][self.y] = -10
                        self.x = i
                        self.y = j
                        if self.step > 2:
                            self.step -= 1
                        return
            return
        self.step += 1'''

        return 0
