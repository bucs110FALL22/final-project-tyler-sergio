import pygame
from pygame.locals import *
#
#
class Squid:
    def __init__(self, parent_screen, length, speed, startx, starty):
        self.length = length
        self.startx = startx
        self.starty = starty
        self.x, self.y = self.startx, self.starty
        self.speed = speed
        self.parent_screen = parent_screen
        self.image = pygame.image.load("assets/picture/player_squid.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (length, length))
        self.direction = None
        self.parent_screen.blit(self.image, (self.x, self.y))
        self.imageRect = self.image.get_rect(topleft = (self.x, self.y))

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        if self.direction == 'left':
            self.x -= self.length*self.speed
        if self.direction == 'right':
            self.x += self.length*self.speed
        if self.direction == 'up':
            self.y -= self.length*self.speed
        if self.direction == 'down':
            self.y += self.length*self.speed

    def drawPlayer(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        self.imageRect = self.image.get_rect(topleft = (self.x, self.y))

    def playerReset(self):
      self.x, self.y = self.startx, self.starty
      self.direction = None

