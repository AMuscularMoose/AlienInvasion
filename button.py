import pygame.font

class Botton:

    def __init__(self,ai_game,msg):
        #init button attrib
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set the dimensions and prop of the bottom
        self.width, self.height = 200, 50
        self.botton_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.Sysfont(None,48)

        #build the buttons rect object and center it
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #the buttom message needs to be prepped only once
        self._prep_msg(msg)