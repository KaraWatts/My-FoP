import pygame
import random

class Alien(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.green_alien = pygame.image.load("assets/GreenAlien.png")
        self.red_alien = pygame.image.load("assets/RedAlien.png")
        self.yellow_alien = pygame.image.load("assets/YellowAlien.png")

        self.spawnable_aliens = [self.yellow_alien, self.red_alien, self.green_alien]

        self.image = self.spawnable_aliens[random.randint(0,2)]
        self.rect = self.image.get_rect(center = (20,20))
        self.going_right = True

    def update(self):
        if self.going_right == True:
            self.rect.x += 5
            if self.rect.x == 760:
                self.rect.y += 50
                self.going_right = False
        else:
            self.rect.x -= 5
            if self.rect.x == 0:
                self.going_right = True
                self.rect.y += 50