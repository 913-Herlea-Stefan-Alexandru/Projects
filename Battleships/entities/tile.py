import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, picture, size, x, y):
        super().__init__()

        self.width = size
        self.height = size
        self.picture = picture

        self.image = pygame.image.load(self.picture).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_picture(self, new_pic = None):
        '''
        Changes the appearance of the tile
        :param new_pic: the new picture to lead (str)
        :return: -
        '''
        self.picture = new_pic

        self.image = pygame.image.load(self.picture).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
