import pygame
from pygame.locals import *
import time

from entities.board import Board, BoardError
from utility.RandomAi import RandomAi
from utility.SmartAi import SmartAi
from entities.player import Player
from entities.button import Button

class GUI:
    def __init__(self, ai_type):
        self._running = True
        self._background = None
        self._display_surface = None
        self._width = 1200
        self._height = 700
        self._clock = None

        self._game_state = None

        self._player_board = None
        self._computer_board = None
        self._ai = None
        self._ai_type = ai_type
        self._player = None

        self._ready_button = None

        self._drag = None
        self._ready = False

        self._player_move = True
        self._computer_move = False

        self._splash = None
        self._explosion = None

        self._end_text = ''
        self._font = None

        self._all_sprites_list = None
        self._all_player_ships = None
        self._all_enemy_ships = None

    def on_init(self):
        pygame.init()
        self._display_surface = pygame.display.set_mode((self._width, self._height))

        self._all_sprites_list = pygame.sprite.Group()
        self._all_player_ships = pygame.sprite.Group()
        self._all_enemy_ships = pygame.sprite.Group()

        self._ready_button = Button('Ready', self._width//2 - 50, self._height-100)

        self._player = Player(True)
        if self._ai_type == 'smart':
            self._ai = SmartAi(True)
        else:
            self._ai = RandomAi(True)

        self._player_board = Board(8, 125, 100, True)
        self._computer_board = Board(8, self._player_board.rect.x + self._player_board.size*50 + 150, 100, True)

        self._ai.place_ships(self._computer_board)

        self._all_sprites_list.add(self._player_board)
        self._all_sprites_list.add(self._computer_board)

        self._all_sprites_list.add(self._player.ship_list)
        self._all_player_ships.add(self._player.ship_list)

        self._game_state = 'add_ships'

        self._background = pygame.image.load("res\\background.jpg")
        self._background = pygame.transform.scale(self._background, (self._width, self._height))
        self._display_surface.blit(self._background, (0, 0))
        pygame.display.flip()

        pygame.mixer.init()
        pygame.mixer.music.load("res\\wave_sounds.mp3")
        pygame.mixer.music.play(-1, 0.0)

        self._splash = pygame.mixer.Sound("res\\splash.mp3")
        self._explosion = pygame.mixer.Sound("res\\explosion.mp3")

        self._font = pygame.font.SysFont('Arial', 50)

        self._running = True
        self._clock = pygame.time.Clock()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if self._game_state == 'add_ships':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for ship in self._all_player_ships:
                        if ship.rect.x <= event.pos[0] <= ship.rect.x + ship.width and ship.rect.y <= event.pos[1] <= ship.rect.y + ship.height:
                            if self._drag == None:
                                if ship.placed:
                                    self._player_board.remove_ship(ship)
                                    ship.placed = False
                                self._drag = ship
                    if self._ready_button in self._all_sprites_list:
                        if self._ready_button.rect.x <= event.pos[0] <= self._ready_button.rect.x + self._ready_button.width and self._ready_button.rect.y <= event.pos[1] <= self._ready_button.rect.y + self._ready_button.height:
                            self._game_state = 'play_game'
                            self._all_sprites_list.remove(self._ready_button)
                if event.button == 3:
                    if self._drag != None:
                        self._drag.rotate()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if self._drag != None:
                        try:
                            letter, number = self._player_board.get_coordinates(self._drag.rect.x, self._drag.rect.y)
                            self._player_board.add_ship(letter, number, self._drag)
                            self._drag.placed = True
                        except BoardError:
                            self._drag.rect.x = self._drag.initial_pos[0]
                            self._drag.rect.y = self._drag.initial_pos[1]
                            if self._drag.rotation == 'v':
                                self._drag.rotate()
                        self._drag = None
        if self._game_state == 'play_game':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self._player_move:
                    try:
                        letter, number = self._computer_board.get_coordinates(event.pos[0], event.pos[1])
                        ship = self._computer_board.move(letter, number)
                        if ship != None:
                            self._explosion.play()
                            if ship.hp == 0:
                                self._all_sprites_list.add(ship)
                                self._all_enemy_ships.add(ship)
                                print('Enemy ' + ship.name + ' sunk!\n')
                            self.on_render()
                            time.sleep(2)
                            self._explosion.stop()
                        else:
                            self._splash.play()
                            self.on_render()
                            time.sleep(2)
                            self._splash.stop()
                            self._player_move = False
                            self._computer_move = True
                    except BoardError:
                        pass

    def on_loop(self):
        if self._game_state == 'add_ships':
            if self._drag != None:
                mouse_pos = pygame.mouse.get_pos()
                self._drag.rect.x = mouse_pos[0] - self._drag.width / 2
                self._drag.rect.y = mouse_pos[1] - self._drag.height / 2
            self._ready = True
            for ship in self._player.ship_list:
                if ship.placed == False:
                    self._ready = False
                    break
            if self._ready:
                if self._ready_button not in self._all_sprites_list:
                    self._all_sprites_list.add(self._ready_button)
            else:
                if self._ready_button in self._all_sprites_list:
                    self._all_sprites_list.remove(self._ready_button)
        elif self._game_state == 'play_game':
            if self._computer_move:
                ship = self._ai.make_move(self._player_board)
                if ship != None:
                    self._explosion.play()
                    if ship.hp == 0:
                        print('Friendly ' + ship.name + ' sunk!\n')
                    self.on_render()
                    time.sleep(2)
                    self._explosion.stop()
                else:
                    self._splash.play()
                    self.on_render()
                    time.sleep(2)
                    self._splash.stop()
                    self._player_move = True
                    self._computer_move = False
            if len(self._all_enemy_ships) == 5:
                self._game_state = 'endgame'
                self._end_text = 'Victory!'
            ok = False
            for ship in self._all_player_ships:
                if ship.hp > 0:
                    ok = True
                    break
            if not ok:
                self._game_state = 'endgame'
                self._end_text = 'Defeat!'
        self._all_sprites_list.update()

    def on_render(self):
        self._display_surface.blit(self._background, (0, 0))
        self._all_sprites_list.draw(self._display_surface)
        if self._game_state == 'endgame':
            text = self._font.render(self._end_text, True, (0, 0, 255))
            self._display_surface.blit(text, (self._width//2-75, self._height//2-20))
            pygame.display.flip()
            while True:
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    self._running = False
                    break
        pygame.display.flip()

    def on_cleanup(self):
        pygame.mixer.music.stop()
        pygame.quit()

    def start(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()

            self.on_render()

            self._clock.tick(60)

        self.on_cleanup()
