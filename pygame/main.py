import pygame
import sys #allows you to control your interface for your system
from ship import Spaceship
from bullet import Bullet
from alien import Alien
from powerup import Powerup

#Main game components
class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption('Space Invaders')
        self.clock = pygame.time.Clock()

        #Space Background
        self.space_surface = pygame.Surface((800,800))

        #HERO
        self.space_ship = Spaceship('assets/DurrrSpaceShip.png', 400, 800)

        # Bullet
        self.all_bullets = pygame.sprite.Group() #creates an empty object {}

        #Aliens
        self.all_aliens = pygame.sprite.Group() #creates an empty object {}


        self.enemy_spawn_timer = pygame.USEREVENT + 1 #creates a custom event 
        pygame.time.set_timer(self.enemy_spawn_timer, 500) #runs the enemy spawn timer event every 500 milisecs

        #Powerup
        self.powerup = pygame.sprite.Group()
        self.powerup_spawn_timer = pygame.USEREVENT + 2 #creates a custom event 
        pygame.time.set_timer(self.powerup_spawn_timer, 10000)

        self.powerup_end_timer = pygame.USEREVENT + 3

        

    def run(self):
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    current_ship_position = self.space_ship.get_position()
                    bullet_object = Bullet(current_ship_position[0] + 40, current_ship_position[1] + 10)
                    self.all_bullets.add(bullet_object)


                if event.type == self.enemy_spawn_timer:
                    alien_object = Alien()
                    self.all_aliens.add(alien_object)

                if event.type == self.powerup_spawn_timer:
                    powerup_object = Powerup()
                    self.powerup.add(powerup_object)

                if event.type == self.powerup_end_timer:
                    self.space_ship.speed_boost(5)
                    

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.space_ship.move('a')
            if keys[pygame.K_d]:
                self.space_ship.move('d')
            if keys[pygame.K_s]:
                self.space_ship.move('s')
            if keys[pygame.K_w]:
                self.space_ship.move('w')

            self.screen.blit(self.space_surface, ((0,0)))
            self.space_surface.blit(pygame.image.load("assets/OuterSpace.png"), (0,0)) #destination is where the top left corner of the image is to be placed
            self.space_ship.draw(self.space_surface)
            self.all_bullets.draw(self.space_surface)
            self.all_bullets.update(self.all_aliens)
            self.all_aliens.draw(self.space_surface)
            self.all_aliens.update()
            self.powerup.draw(self.space_surface)
            
       
            if pygame.sprite.spritecollide(self.space_ship, self.all_aliens, True):
                 self.space_ship.livesCounter(-1)

            if pygame.sprite.spritecollide(self.space_ship, self.powerup, True):
                self.space_ship.speed_boost(10)
                pygame.time.set_timer(self.powerup_end_timer, 5000)
                
                
            if self.space_ship.lives == 0:
                pygame.quit()
                sys.exit()



            pygame.display.update()
            self.clock.tick(60) #lets the game know that we want it to run at 60 fps


my_game = Game()
my_game.run()

