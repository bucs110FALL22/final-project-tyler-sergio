import pygame
import random

class Enemy():
  def __init__(self, screen):
    self.screen = screen
    self.image = []
    self.size = []
    self.speed = []
    self.x = []
    self.y = []
    self.xChange = []
    self.yChange = []
    
  def move(self, index):
    self.x[index] += self.xChange[index]
    self.y[index] += self.yChange[index]

  def spawnEnemy(self, size, speed, x, y):
      self.size.append(size)
      self.image.append(pygame.transform.scale(pygame.image.load("assets/picture/enemy.png").convert_alpha(), (size, size)))
      self.speed.append(speed)
      self.x.append(x)
      self.y.append(y)
      self.xChange.append(speed*(random.randrange(5, 15)/10))
      self.yChange.append(speed*(random.randrange(5, 15)/10))
  
  
  def drawEnemy(self, index):
    try:
      self.screen.blit(self.image[index], (self.x[index], self.y[index]))
    except:
      print('fail')

  def enemyReset(self):
    self.image = []
    self.size = []
    self.speed = []
    self.x = []
    self.y = []
    self.xChange = []
    self.yChange = []
  
    
    