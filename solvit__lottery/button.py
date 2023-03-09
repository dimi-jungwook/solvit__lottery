import pygame
import random
#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False
		'''
		self.year1 = random.randint(1,3)
        	self.class1 = random.randint(1,10)
        	self.num1 = random.randint(1,38)
        	if self.class1 < 10:
            	self.class1 = "0{}".format(self.class1)
        '''

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
'''
	def choose(self):
		h = "{}{}{}".format(self.year1, self.class1, self.num1)
        return h
'''