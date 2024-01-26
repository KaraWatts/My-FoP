import pygame


class Spaceship:

    def __init__(self, image, x, y):
        self.space_ship_surface = pygame.image.load(image)
        self.rect = self.space_ship_surface.get_rect(midbottom = (x,y))
        self.speed = 5
        self.lives = 3

    def get_position(self):
        return (self.rect.x, self.rect.y)
    
    def draw(self, screen):
        screen.blit(self.space_ship_surface, self.rect)

    def speed_boost(self, speed):
        self.speed = speed

    def livesCounter(self, lives):
        self.lives += lives

    def move(self, direction):
        if direction == "a":
            if self.rect.x >= 0:
                self.rect.x -= self.speed
        elif direction == 'd':
            if self.rect.x <= 720:
                self.rect.x += self.speed   
        elif direction == 'w':
            if self.rect.y >= 400:
                self.rect.y -= self.speed
        elif direction == 's':
            if self.rect.y <= 720:
                self.rect.y += self.speed
