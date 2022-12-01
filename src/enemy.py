import turtle
import pygame
import random
import math
from src.player import Squid

class Enemy():
  def __init__(self, screen, size, speed, x, y, direction):
    self.screen = screen
    self.enemSpeed = speed
    self.maxEnemies = 10
    self.image = []
    self.speed = []
    self.direction = []
    self.x = []
    self.y = []
    self.imageRect = []
    

  def move(self, index):
    print(index)
    self.x[index] += self.speed[index]
    self.y[index] += self.speed[index]
    
    #self.newX = cos(self.direction) * self.speed
    #self.newY = sin(self.direction) * self.speed
    #self.x = self.x + self.newX
    #self.y = self.y + self.newY

  def spawnEnemies(self):
    for i in range(0, self.maxEnemies):
      self.image.append(pygame.transform.scale(pygame.image.load("assets/picture/enemy.png").convert(),
        (size, size)))
      self.speed.append(self.enemSpeed)
      self.direction.append(math.radians(direction))
      self.x.append(x)
      self.y.append(y)
      self.imageRect.append(self.image.get_rect(topleft = (self.x, self.y)))

  
  def drawEnemy(self, i):
    for i in range(0, self.maxEnemies):
      self.move(i)
      
      self.screen.blit(self.image[i], (self.x[i], self.y[i]))
      self.imageRect = self.image.get_rect(topleft = (self.x, self.y))
    
    