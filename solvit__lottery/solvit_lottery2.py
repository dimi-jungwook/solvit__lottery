import pygame
#import random


pygame.init()

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

scr = [900, 600]
screen = pygame.display.set_mode(scr)

str_but = pygame.image.load("start_button.png").convert_alpha()
drw_but = pygame.image.load("draw_button.png").convert_alpha()
logo = pygame.image.load("solvit_logo.png").convert_alpha()
logo = pygame.transform.scale(logo, (500, 500))


    
    
    for event in pygame.event.get():
                
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
        
pygame.quit()