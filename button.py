import pygame.font

class Button:

    def __init__(self,ai_game,msg):
        #init button attrib
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #set the dimensions and prop of the bottom
        self.width, self.height = 200, 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
            #the None tells pygame to use the default font
            #the 48 specifies the font size

        #build the buttons rect object and center it
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #the buttom message needs to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        #turn msg into a rendered image and center text on the button
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #draw blank button and then draw message
        self.screen.fill(self.button_color,self.rect)
            #this is to draw the rectangle portion of the buttom
        self.screen.blit(self.msg_image,self.msg_image_rect)
            #this is to draw the text image to the screen, passing it an image and the rect object associated with it.