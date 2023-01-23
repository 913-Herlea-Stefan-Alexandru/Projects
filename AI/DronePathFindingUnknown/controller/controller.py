from model.DMap import DMap
from model.Drone import Drone
from model.Environment import Environment
import pygame
from pygame.locals import *
from random import random, randint, seed
import numpy as np
import time

class Controller:
    def __init__(self, e):
        # we create the environment
        self.e = e
        #self.e.loadEnvironment("test2.map")
        self.e.randomMap()
        # print(str(e))

        # we create the map
        self.m = DMap()

        # we position the drone somewhere in the area
        x = randint(0, 19)
        y = randint(0, 19)

        while e.isWall(x, y):
            x = randint(0, 19)
            y = randint(0, 19)

        print(x, y)

        # cream drona
        self.d = Drone(x, y)

    def getEnvironment(self):
        return self.e

    def run(self, screen):
        running = True
        tm = time.time()

        # main loop
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
                if event.type == KEYDOWN:
                    # use this function instead of move
                    #self.d.moveDSF(self.m)
                    self.d.move(self.m)
            self.m.markDetectedWalls(self.e, self.d.x, self.d.y)
            screen.blit(self.m.image(self.d.x, self.d.y), (400, 0))
            pygame.display.flip()
            r = self.d.moveDSF(self.m)
            time.sleep(0.05)
            if r == 1:
                running = False

        rm = time.time() - tm
        print(rm)
