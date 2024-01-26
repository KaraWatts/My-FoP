import pygame
import random
from ship import Spaceship

class Powerup(pygame.sprite.Sprite, Spaceship):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/Icon29.png')
        self.rect = self.image.get_rect(center = (random.randint(10,700),random.randint(400, 700)))

    def move(self, direction):
        if direction == "a":
            if self.rect.x >= 0:
                self.rect.x -= 10
        elif direction == 'd':
            if self.rect.x <= 720:
                self.rect.x += 10    
        elif direction == 'w':
            if self.rect.y >= 400:
                self.rect.y -= 10
        elif direction == 's':
            if self.rect.y <= 720:
                self.rect.y += 10

