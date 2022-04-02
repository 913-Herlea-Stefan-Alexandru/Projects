import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.height = 50
        self.width = 100

        self.image = pygame.Surface([100, 50])

        pygame.draw.rect(self.image, (0, 225, 102), [0, 0, 100, 50])

        self.font = pygame.font.SysFont('Arial', 30)
        self.text = self.font.render(name, True, (255, 255, 255))

        self.image.blit(self.text, (12, 5))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
