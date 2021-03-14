import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
    #Overall class to manage game assets and behavior

    def __init__(self):
        #initialize the game and create the game resources
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            #old settings code: self.screen = pygame.display.set_mode((1200,800))
            #the (1200,800) is a tuple that defines the dimensions of the game window
            #this means that the window will be 1200 pixels wide by 800 pixels high
        pygame.display.set_caption("Alien Invasion")
        #Setting the background color:
        self.bg_color = (230,230,230)
        self.ship = Ship(self)
      
    def run_game(self):
        #Start the main loop for the game
        while True:
            self._check_events()
            self._update_screen()
            
    def _check_events(self):
        #watch for kbm events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RIGHT:
                    #Move the ship right
                    self.ship.rect.x += 1
    def _update_screen(self):
        #Redraw the screen during each pass through the loop:
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()