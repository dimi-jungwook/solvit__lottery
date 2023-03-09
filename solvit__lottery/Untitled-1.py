import pygame
import button
import random
import time
year_1 = [
[12,4,32],
[21,33],
[16,18,11],
[16,5,24,15,1,29],
[9,10,3,24,17,20,15,33],
[12,13,3,5],
[2,16,8,5,15,3],
[],
[12,24,20,34,18,8,32,3,10,23,5,33,29,26,14],
[12,14,2,25,1,29]
]
year_2 = [
[10,5,2,1],
[34,12,21,7,8,5,19,27,22,18,23,36,6,13,35,11],
[34,28,7,9,20,22,37,19,12,35,21,6,15],
[18,9,15,19,2,25,6,8],
[3,14,22],

[1,17,22,29,7,26,34,21,4],
[37,35,26,5,9,30,13,16,12,21],
[11,23,24,15,31,7,14],
[26,18,12,27,4,28,24,10,29,2,34,17],
[4,27,21,37,33,7,20,10,28,9,17]
]
year_3 = [
[21,18,9,11,18,5,4,6,25,32,2],
[19, 12, 7, 33, 23, 17, 30, 29, 2, 5, 27, 32, 3, 25, 13, 12],
[32, 16, 17, 27, 10, 8, 2],
[10],
[11, 8, 2, 17, 19, 15, 33, 9, 13, 3, 29, 5],
[20, 3],
[31, 9, 28, 7, 19, 1, 22, 18, 25, 36, 4, 6],
[4, 32, 34, 18, 30, 17, 2],
[22, 6, 31, 11, 7, 33, 13],
[34, 35, 20, 31, 26, 4, 13]
]

winner_1 = []
winner_2 = []
winner_3 = []
winner_4 = []

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Solvit lottery Program.")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 20)

#define colours
TEXT_COL = (0, 0, 0)

#load button images

s_logo = pygame.image.load("stuco_logo.jpg").convert_alpha()
s_logo = pygame.transform.scale(s_logo, (150, 150))
str_but = pygame.image.load("start_button.png").convert_alpha()
drw_but = pygame.image.load("draw_button.png").convert_alpha()
home_button = pygame.image.load("home_button.png").convert_alpha()
home_button = pygame.transform.scale(home_button, (100, 100))
logo = pygame.image.load("solvit_logo.png").convert_alpha()
logo = pygame.transform.scale(logo, (500, 500))
#create button instances

start_button = button.Button(515, 300, str_but, 0.15)


draw_button1 = button.Button(500, 100, drw_but, 0.05)
draw_button2 = button.Button(500, 200, drw_but, 0.05)
draw_button3 = button.Button(500, 300, drw_but, 0.05)
result_button = button.Button(500, 400, drw_but, 0.05)

back_button = button.Button(500, 500, home_button, 0.5)
back_button2 = button.Button(200, 500, home_button, 0.5)
exit_button = button.Button(500, 550, drw_but, 0.05)

choose_1 = button.Button(300, 300, drw_but, 0.05)
choose_2 = button.Button(300, 300, drw_but, 0.05)
choose_3 = button.Button(300, 300, drw_but, 0.05)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
'''
def choose(x, y):
    choose_button = button.Button(x, y, drw_but, 0.05)
    if choose_button.draw(screen):
        year1 = random.randint(1,3)
        class1 = random.randint(1,10)
        num1 = random.randint(1,38)
    
        if class1 < 10:
            class1 = "0{}".format(class1)
        h = "{}{}{}".format(year1, class1, num1)
        return h
'''
#game loop
h = "XXXXX"
h2 = "XXXXX"
h3 = "XXXXX"
show1 = "XXXXX"
run = True
while run:

  screen.fill((255, 239, 222))

  #check if game is paused
  if game_paused == True:
    #check menu state
    if menu_state == "main":
        screen.blit(s_logo, (35, 100))
        draw_text("1st prize", font, TEXT_COL, 200, 100)
        draw_text("2nd prize", font, TEXT_COL, 200, 200)
        draw_text("3rd prize", font, TEXT_COL, 200, 300)
        draw_text("result", font, TEXT_COL, 200, 400)
        draw_text("Exit", font, TEXT_COL, 200, 550)
        
        
        if draw_button1.draw(screen):
            menu_state = "draw_1"
    
        if draw_button2.draw(screen):
            menu_state = "draw_2"
        if draw_button3.draw(screen):
            menu_state = "draw_3"
        if result_button.draw(screen):
            menu_state = "result"
        if exit_button.draw(screen):
            run = False
    #check if the options menu is open
    
    
    if menu_state == "draw_1":
        
        draw_text("1st prize", font, TEXT_COL, 100, 100)
        if choose_1.draw(screen):
        
            year1 = random.randint(1,3)
            class1 = random.randint(1,10)
            while class1 == 8:
                class1 = random.randint(1,10)
                if class1 != 8:
                    break
            
            
            if year1 == 1:
                for i in range(1,11):
                    if class1 == i:
                        num1 = random.choice(year_1[i-1])
                        
    
            if year1 == 2:
                for i in range(1,11):
                    if class1 == i:
                        num1 = random.choice(year_2[i-1])
                        
    
            if year1 == 3:
                for i in range(1,11):
                    if class1 == i:
                        num1 = random.choice(year_3[i-1])
                        
    
            if class1 < 10:
                class1 = "0{}".format(class1)
                
            if num1 < 10:
                num1 = "0{}".format(num1)
            h = "{}{}{}".format(year1, class1, num1)
            winner_1.append(h)
            
        
        draw_text("{}".format(h), font, TEXT_COL, 200, 500)
        
        if back_button.draw(screen):
            menu_state = "main"
        #menu_state = "main"
    if menu_state == "draw_2":
        
        draw_text("2nd prize", font, TEXT_COL, 200, 100)
        
        if choose_2.draw(screen):
            
            year2 = random.randint(1,3)
            class2 = random.randint(1,10)
            while class2 == 8:
                class2 = random.randint(1,10)
                if class2 != 8:
                    break
            
            if year2 == 1:
                for i in range(1,11):
                    if class2 == i:
                        num2 = random.choice(year_1[i-1])
                        
            if year2 == 2:
                for i in range(1,11):
                    if class2 == i:
                        num2 = random.choice(year_2[i-1])
                        
            if year2 == 3:
                for i in range(1,11):
                    if class2 == i:
                        num2 = random.choice(year_3[i-1])
                        
    
            if class2 < 10:
                class2 = "0{}".format(class2)
                
            if num2 < 10:
                num2 = "0{}".format(num2)
            h2 = "{}{}{}".format(year2, class2, num2)
            winner_2.append(h2)
            
        draw_text("{}".format(h2), font, TEXT_COL, 200, 500)
        if back_button.draw(screen):
            menu_state = "main"
    if menu_state == "draw_3":
        
        draw_text("3rd prize", font, TEXT_COL, 200, 100)
        if choose_3.draw(screen):
            
            year3 = random.randint(1,3)
            class3 = random.randint(1,10)
            if class3 == 8:
                class3 = random.randint(1,10)
            if class3 == 8:
                class3 = random.randint(1,10)
            if class3 == 8:
                class3 = random.randint(1,10)
            if class3 == 8:
                class3 = random.randint(1,10)
            if class3 == 8:
                class3 = random.randint(1,10)
            if class3 == 8:
                class3 = random.randint(1,10)
            if class3 == 8:
                class3 = random.randint(1,10)
            if class3 == 8:
                class3 = random.randint(1,10)
            if class3 == 8:
                class3 = random.randint(1,10)
            
            if year3 == 1:
                for i in range(1,11):
                    if class3 == i:
                        num3 = random.choice(year_1[i-1])
                        
            if year3 == 2:
                for i in range(1,11):
                    if class3 == i:
                        num3 = random.choice(year_2[i-1])
                        
            if year3 == 3:
                for i in range(1,11):
                    if class3 == i:
                        num3 = random.choice(year_3[i-1])
                        
    
            if class3 < 10:
                class3 = "0{}".format(class3)
                
            if num3 < 10:
                num3 = "0{}".format(num3)
            h3 = "{}{}{}".format(year3, class3, num3)
            winner_3.append(h3)
        draw_text("{}".format(h3), font, TEXT_COL, 200, 500)
        if back_button.draw(screen):
            menu_state = "main"
            
    

    if menu_state == "result":
        draw_text("Result", font, TEXT_COL, 100, 70)
        show1 = winner_1[0]
        
        show2 = winner_2[0]
        show3 = winner_2[1]
        show4 = winner_2[2]
        show5 = winner_2[3]
        
        show6 = winner_3[0]
        show7 = winner_3[1]
        show8 = winner_3[2]
        show9 = winner_3[3]
        show10 = winner_3[4]
        show11 = winner_3[5]
        show12 = winner_3[6]
        show13 = winner_3[7]
        show14 = winner_3[8]
        show15 = winner_3[9]
        show16 = winner_3[10]
        show17 = winner_3[11]
        show18 = winner_3[12]
        show19 = winner_3[13]
        show20 = winner_3[14]
        show21 = winner_3[15]
        
        draw_text("1st prize: {}".format(show1), font, TEXT_COL, 100, 150)
        
        draw_text("2nd prize: {}".format(show2), font, TEXT_COL, 100, 200)
        draw_text("2nd prize: {}".format(show3), font, TEXT_COL, 100, 250)
        draw_text("2nd prize: {}".format(show4), font, TEXT_COL, 100, 300)
        draw_text("2nd prize: {}".format(show5), font, TEXT_COL, 100, 350)
        
        draw_text("3rd prize: {}".format(show6), font, TEXT_COL, 300, 150)
        draw_text("3rd prize: {}".format(show7), font, TEXT_COL, 300, 200)
        draw_text("3rd prize: {}".format(show8), font, TEXT_COL, 300, 250)
        draw_text("3rd prize: {}".format(show9), font, TEXT_COL, 300, 300)
        draw_text("3rd prize: {}".format(show10), font, TEXT_COL, 300, 350)
        draw_text("3rd prize: {}".format(show11), font, TEXT_COL, 300, 400)
        draw_text("3rd prize: {}".format(show12), font, TEXT_COL, 300, 450)
        draw_text("3rd prize: {}".format(show13), font, TEXT_COL, 500, 150)
        draw_text("3rd prize: {}".format(show14), font, TEXT_COL, 500, 200)
        draw_text("3rd prize: {}".format(show15), font, TEXT_COL, 500, 250)
        
        draw_text("3rd prize: {}".format(show16), font, TEXT_COL, 500, 300)
        draw_text("3rd prize: {}".format(show17), font, TEXT_COL, 500, 350)
        draw_text("3rd prize: {}".format(show18), font, TEXT_COL, 500, 400)
        draw_text("3rd prize: {}".format(show19), font, TEXT_COL, 500, 450)
        draw_text("3rd prize: {}".format(show20), font, TEXT_COL, 500, 500)
        draw_text("3rd prize: {}".format(show21), font, TEXT_COL, 500, 550)
        if back_button2.draw(screen):
            menu_state = "main"
    

  else:
    screen.blit(logo, (0, 0))
    draw_text("PRESS TO START", font, TEXT_COL, 515, 250)
    draw_text("Powered by.", font, TEXT_COL, 515, 400)
    draw_text("Solvit student council", font, TEXT_COL, 515, 425)
    if start_button.draw(screen):
        game_start = True

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()