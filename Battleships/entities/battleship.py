import pygame

class BattleshipError(Exception):
    def __init__(self, msg = ''):
        super().__init__(msg)

class Battleship(pygame.sprite.Sprite):
    def __init__(self, length, name, picture = None, x = 0, y = 0, pgame = False):
        super().__init__()
        self._name = name
        self._length = length
        self._hp = length
        self._rotation = 'h'
        self.picture = picture

        self.placed = False
        self.initial_pos = (x, y)

        self._pgame = pgame

        if self.picture != None and pgame:
            self.width = length*50
            self.height = 50

            self.image = pygame.image.load(self.picture).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            self.mask = pygame.mask.from_surface(self.image)

            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def sink(self):
        '''
        Used to change the image of the ship into the sunken one (GUI only)
        :return: -
        '''
        if self._pgame:
            self.picture = self.picture[:-4] + '_destroyed.png'

            self.image = pygame.image.load(self.picture).convert_alpha()
            if self._rotation == 'v':
                self.width, self.height = self.height, self.width
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.image = pygame.transform.rotate(self.image, 90.0)
                self.width, self.height = self.height, self.width
            else:
                self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def rotate(self):
        '''
        A function used to rotate the image of the ship (GUI only)
        :return: -
        '''
        if self._rotation == 'h':
            self.image = pygame.transform.rotate(self.image, 90.0)
            self.width, self.height = self.height, self.width
            self._rotation = 'v'
        elif self._rotation == 'v':
            self.image = pygame.transform.rotate(self.image, -90.0)
            self.width, self.height = self.height, self.width
            self._rotation = 'h'

    @property
    def name(self):
        return self._name

    @property
    def length(self):
        return self._length

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, val):
        self._hp = val

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, val):
        if val not in ['v', 'h']:
            raise BattleshipError()
        self._rotation = val