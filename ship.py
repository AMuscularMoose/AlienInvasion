import pygame

class Ship:
    def __init__(self, ai_game):
        #initialize the ship and set its starting pos.
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        #load the ship and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #starting the ship at the bottom middle of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        #store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update the ships pos based on movement flag
        #update the ships x-value, not the rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        #update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)