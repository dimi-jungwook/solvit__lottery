import pygame
import random
import time

class_101 = []
class_102 = []
class_103 = []
class_104 = []
class_105 = []
class_106 = []
class_107 = []
class_108 = []
class_109 = []
class_110 = []

class_201 = []
class_202 = []
class_203 = []
class_204 = []
class_205 = []
class_206 = []
class_207 = []
class_208 = []
class_209 = []
class_210 = []

class_301 = []
class_302 = []
class_303 = []
class_304 = []
class_305 = []
class_306 = []
class_307 = []
class_308 = []
class_309 = []
class_310 = []

pygame.init()

scr = [900, 600]
screen = pygame.display.set_mode(scr)

str_but = pygame.image.load("start_button.png").convert_alpha()
drw_but = pygame.image.load("draw_button.png").convert_alpha()
logo = pygame.image.load("solvit_logo.png").convert_alpha()
logo = pygame.transform.scale(logo, (500, 500))

s_logo = pygame.image.load("stuco_logo.jpg").convert_alpha()
s_logo = pygame.transform.scale(s_logo, (150, 150))

font  = pygame.font.SysFont("arialblack", 20)
TEXT_COL = (0, 0, 0)

game_paused = False

def draw_text(text,font, text_col, x, y):
    img = font.render(text, True, text_col)

    screen.blit(img, (x, y))
    
menu = "main"
 
run = True

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()       
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        
    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
        
start_button = Button(515, 300, str_but, 0.15)

quit_button = Button(150, 300, drw_but, 0.5)
draw_button1 = Button(150, 200, drw_but, 0.5)
draw_button2 = Button(150, 100, drw_but, 0.5)
draw_button3 = Button(150, 400, drw_but, 0.5)
result_button = Button(150, 500, drw_but, 0.5)
  
exit_button = Button(150, 300, drw_but, 0.5)
color = (255 ,239, 222)
prize_1 = False
prize_2 = False
prize_3 = False
result = False
is_right = False

while run == True:

    
    screen.fill((color))
              
    if game_paused == True:
        
        if menu == "main":   
            screen.blit(s_logo, (515, 60))
            
            if quit_button.draw(screen):
                run = False
                break
                    
                        
            if draw_button1.draw(screen):
                menu = "draw_1"
                    
            
            if result_button.draw(screen):
                result = True
            
                        
            if draw_button2.draw(screen): #가장 위에 버튼
                prize_2 = True
                    
            if draw_button3.draw(screen):
                prize_3 = True
            
        if menu == "draw_1":
            year1 = random.randint(1,3)
            class1 = random.randint(1,10)
            num1 = random.randint(1,38)
        
            if class1 < 10:
                class1 = "0{}".format(class1)
                h = "{}{}{}".format(year1, class1, num1)
                draw_text(f"{h}".format(h), font, (255,255,255), 515, 250)

            if exit_button.draw(screen):
                is_right = True
                prize_1 = False
    else:
        screen.blit(logo, (0, 0))
        draw_text("PRESS TO START", font, TEXT_COL, 515, 250)
        draw_text("Powered by.", font, TEXT_COL, 515, 400)
        draw_text("Solvit student council", font, TEXT_COL, 515, 425)
        
        
        if start_button.draw(screen):
            game_paused = True
            
        

        
    if result:
        if quit_button.draw(screen):
            run = False
                
    
    for event in pygame.event.get():
                
        if event.type == pygame.QUIT:
            run = False        
            
    
    
    
    pygame.display.flip()


pygame.quit()