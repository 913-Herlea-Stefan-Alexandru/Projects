from random import random
import numpy as np
import pickle
import pygame
from utils import *

class Map:
    def __init__(self, n = 20, m = 20):
        self.n = n
        self.m = m
        self.surface = np.zeros((self.n, self.m))

    def validatePos(self, pos):
        return 0 <= pos[0] < self.n and 0 <= pos[1] < self.m

    def isWall(self, pos):
        return self.surface[pos[0]][pos[1]] == 1

    def isSensor(self, pos):
        return self.surface[pos[0]][pos[1]] == 2

    def randomMap(self, fill = 0.2):
        for i in range(self.n):
            for j in range(self.m):
                if random() <= fill :
                    self.surface[i][j] = 1

    def __str__(self):
        string =""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string

    def setSensor(self, x, y):
        self.surface[x][y] = 2

    def saveMap(self, numFile = "test.map"):
        with open(numFile ,'wb') as f:
            pickle.dump(self, f)
            f.close()

    def loadMap(self, numfile):
        with open(numfile, "rb") as f:
            dummy = pickle.load(f)
            self.n = dummy.n
            self.m = dummy.m
            self.surface = dummy.surface
            f.close()

    def image(self, colour = BLUE, background = WHITE):
        imagine = pygame.Surface((400 ,400))
        brick = pygame.Surface((20 ,20))
        sensor = pygame.Surface((20 ,20))
        brick.fill(BLUE)
        sensor.fill(RED)
        imagine.fill(WHITE)
        for i in range(self.n):
            for j in range(self.m):
                if (self.surface[i][j] == 1):
                    imagine.blit(brick, ( j * 20, i * 20))
                if (self.surface[i][j] == 2):
                    imagine.blit(sensor, ( j * 20, i * 20))

        return imagine
