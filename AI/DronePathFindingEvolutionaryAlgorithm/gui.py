from utils import *
import pygame
import time

def initPyGame(dimension):
    # init the pygame
    pygame.init()
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("drone exploration with AE")

    # create a surface on screen that has the size of 800 x 480
    screen = pygame.display.set_mode(dimension)
    screen.fill(WHITE)
    return screen


def closePyGame():
    # closes the pygame
    running = True
    # loop for events
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
    pygame.quit()


def viewMap(currentMap):
    screen = initPyGame((currentMap.n * 20, currentMap.m * 20))

    screen.blit(image(currentMap), (0, 0))
    pygame.display.flip()

    closePyGame()


def movingDrone(currentMap, path, speed, energyLevels, markSeen=True):
    # animation of a drone on a path

    screen = initPyGame((currentMap.n * 20, currentMap.m * 20))

    drona = pygame.image.load("drona.png")
    seen = pygame.Surface((20, 20))
    seen.fill(GREEN)

    k = 0

    for i in range(len(path)):
        screen.blit(image(currentMap), (0, 0))

        if markSeen:
            pass

        screen.blit(drona, (path[i][1] * 20, path[i][0] * 20))
        pygame.display.flip()
        time.sleep(1 * speed)
    closePyGame()


def image(currentMap, colour=BLUE, background=WHITE):
    # creates the image of a map

    imagine = pygame.Surface((currentMap.n * 20, currentMap.m * 20))
    brick = pygame.Surface((20, 20))
    sensor = pygame.Surface((20, 20))
    sensor.fill(RED)
    brick.fill(colour)
    imagine.fill(background)
    for i in range(currentMap.n):
        for j in range(currentMap.m):
            if (currentMap.surface[i][j] == 1):
                imagine.blit(brick, (j * 20, i * 20))
            if (currentMap.surface[i][j] == 2):
                imagine.blit(sensor, (j * 20, i * 20))

    return imagine
