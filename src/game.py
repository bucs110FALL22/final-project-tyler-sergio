import pygame
from pygame.locals import *
import time
import random
from src.player import Squid
from src.enemy import Enemy
from src.text import Text

class Game:
    def __init__(self):
        pygame.init()
        self.cap = 30/1000
        self.frame = 0
        self.surface = pygame.display.set_mode((0, 0))
        self.surfaceSize = self.surface.get_size()
        self.w = self.surfaceSize[0]
        self.h = self.surfaceSize[1]
        slength = self.surfaceSize[0]/15
        self.squid = Squid(self.surface, slength, 0.1, self.w/2 - slength/2, self.h/2 - slength/2)
        self.enemy = Enemy(self.surface, 30, 0.5, 0, 0, 180)
        self.enemyCount = 0
        
        self.background = pygame.image.load("assets/picture/space.jpg")
        self.scoretext = Text("Score: {0}".format(self.frame), 'white', 30, self.surface, 0, 0)
      
    def setBounds(self):
      xBound = self.surface.get_width()
      yBound = self.surface.get_height()
      self.area = Rect(0, 0, xBound, yBound)
      self.rectArea = self.area
      self.bounds = pygame.draw.rect(self.surface, "red", self.area, -1)
      self.areaRect = self.bounds
      squidRect = pygame.draw.rect(self.surface, "blue", self.squid.image.get_rect())
      pygame.display.flip()

    def checkCollisions(self):
      if self.squid.x < 0:
          self.squid.move_right()
      if self.squid.x + self.squid.length > self.w:
          self.squid.move_left()
      if self.squid.y < 0:
          self.squid.move_down()
      if self.squid.y + self.squid.length > self.h:
          self.squid.move_up()

      
      
      

    def render_background(self):
        self.surface.blit(background, (0,0))
      
    def play(self):
        self.render_background()

    def updateHitboxes(self):
       self.squidRect = pygame.draw.rect(self.surface, "blue", self.squid.image.get_rect(topleft = (self.squid.x, self.squid.y)))
      
    def updateScreen(self):
      self.surface.blit(self.background, (0,0))
      pygame.draw.rect(self.surface, "red", self.area, -1)
      self.squid.drawPlayer()
      #self.enemy.drawEnemy()
      self.surface.blit(self.scoretext.textSurface, (0,0))
      pygame.display.flip()

    def run(self):
        self.setBounds()
        running = True

        while running:
          self.updateHitboxes()
          self.updateScreen()
          self.checkCollisions()
          

        ## PLAYER
          self.squid.walk()
          for event in pygame.event.get():
            if event.type == KEYDOWN:
              if event.key == K_ESCAPE:
                  running = False

              if event.key == K_LEFT:
                  self.squid.move_left()

              if event.key == K_RIGHT:
                  self.squid.move_right()

              if event.key == K_UP:
                  self.squid.move_up()

              if event.key == K_DOWN:
                  self.squid.move_down()

            elif event.type == QUIT:
                  running = False

        ## ENEMIES
          if self.frame/200 == 0:
            self.enemyCount += 1
            
            self.enemy.drawEnemy(self.enemyCount)






        ## SCORE
          self.frame = self.frame + 1
          self.scoretext = Text("Score: {0}".format(self.frame), 'white', 30, self.surface, 0, 0)
          time.sleep(self.cap)          

