import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #a class to represent a single alien in the fleet

    def __init__(self,ai_game):
        #initialize the alien and set its starting pos
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load alien image and set its rect attr.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the aliens exact horizontal pos
        self.x = float(self.rect.x)

    def update(self):
        #move the alien to the right
        self.x += self.settings.alien_speed
        self.rect.x = self.x