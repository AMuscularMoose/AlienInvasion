import sys
import pygame

class AlienInvasion:
    #Overall class to manage game assets and behavior

    def __init__(self):
        #initialize the game and create the game resources
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
            #the (1200,800) is a tuple that defines the dimensions of the game window
            #this means that the window will be 1200 pixels wide by 800 pixels high
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        #Start the main loop for the game
        while True:
            #watch for kbm events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit
            #make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()