import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    #Overall class to manage game assets and behavior

    def __init__(self):
        #initialize the game and create the game resources
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #FULLSCREEN OPTION BELOW
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
            #old settings code: self.screen = pygame.display.set_mode((1200,800))
            #the (1200,800) is a tuple that defines the dimensions of the game window
            #this means that the window will be 1200 pixels wide by 800 pixels high
        pygame.display.set_caption("Alien Invasion")

        #create an instance to store game statistics
        self.stats = GameStats(self)

        #Setting the background color:
        self.bg_color = (230,230,230)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #making the play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        #Start the main loop for the game
        while True:
            self._check_events()

            #only some parts should run when game is active 
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            
    def _check_events(self):
        #watch for kbm events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)   
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        #respond to keypresses
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        #respond to keyreleases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        #create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        #update the position of bullets and get rid of old bullets
        self.bullets.update()
        #get rid of bullets that dissapeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))       --this is to check to see in terminal if bullets are actually decreasing as they hit the top of the screen
        
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        #respond to bullet-alien collisions and remove bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        
        if not self.aliens:
            #destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        #create the fleet
        #create an alien and find the number of aliens in a row
        #spacing between each alien is equal to one aliend width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        #determine the numbner of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2*alien_height)

        #create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)

    def _create_alien(self,alien_number,row_number):
        #create an alien and put it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        #respond appropr. if any aliens have reached an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _check_aliens_bottom(self):
        #check to see if any aliens have reached the bottom of the screen
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #treat this the same as if the ship got hit
                self._ship_hit()
                break

    def _change_fleet_direction(self):
        #Drop the entire fleet and change the fleet's direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        #update the pos of all aliens in the fleet after edge checking
        self._check_fleet_edges()
        self.aliens.update()

        #look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            #print("Ship hit!!!")
            self._ship_hit()
        
        #look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _ship_hit(self):
        #respond to the ship being hit by an alien
        if self.stats.ships_left > 0:
            #decrement ships_left
            self.stats.ships_left -= 1

            #get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #create new fleet and repos ship
            self._create_fleet()
            self.ship.center_ship()

            #pause
            sleep(0.5)

        else:
            self.stats.game_active = False


    def _update_screen(self):
        #Redraw the screen during each pass through the loop:
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        #make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()