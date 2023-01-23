from controller.controller import Controller
import pickle,pygame,sys
from pygame.locals import *
from random import random, randint, seed
import numpy as np
import time
from model.constants import *

class UI:
    def __init__(self, controller):
        self._controller = controller

        # initialize the pygame module
        pygame.init()
        # load and set the logo
        logo = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("drone exploration")

        self.screen = pygame.display.set_mode((800, 400))
        self.screen.fill(WHITE)
        self.screen.blit(self._controller.getEnvironment().image(), (0, 0))

    def start(self):
        self._controller.run(self.screen)
        pygame.quit()
