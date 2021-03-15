import pygame.font

class Scoreboard:
    """A class to report scoring info"""

    def __init__(self,ai_game):
        """Init scorekeeping attrib"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #font settings for scoring info
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #prepare the initial score image
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
            #this tells python to round the value of stats.score to the nearest 10 and store it in rounded_score
        score_str = "{:,}".format(rounded_score)
            #this string format directive tells py to insert commas into numbers when converting a num. val to string for ex: 1,000,000 instead of 1000000
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        
        #display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)