import pygame
from pygame.locals import *
import time
from src.player import Squid
from src.enemy import Enemy
from src.text import Text

class Game:
    def __init__(self):
      pygame.init()
      pygame.display.set_caption('Alien Running')
      self.gameState = 'play'
      self.playing = True
      self.cap = 0.03
      self.frame = 0
      self.score = 0
      self.surface = pygame.display.set_mode((0 , 0))
      self.surfaceSize = self.surface.get_size()
      self.w = self.surfaceSize[0]
      self.h = self.surfaceSize[1]*0.95

      ## Player
      playerlength = self.surfaceSize[0]/15
      self.playerSpeed = 0.2
      self.startx = self.w/2 - playerlength/2
      self.starty = self.h/2 - playerlength/2
      self.squid = Squid(self.surface, playerlength, self.playerSpeed, self.startx, self.starty)
        
      ## Enemy
      self.enemylength = self.surfaceSize[0]/30
      self.enemy = Enemy(self.surface)
      self.enemyCount = 0

      ## Meta
      self.background =  pygame.transform.scale(pygame.image.load("assets/picture/space.jpg"), (self.w, self.h))
      self.scoretext = Text("Score: {0}".format(self.frame), 'white', 30, self.surface, 0, 0)


  
    def reset(self):
      self.score = 0
      self.squid.playerReset() 
      self.enemy.enemyReset()
      self.enemyCount = 0
      self.gameState = 'play'

  
    def setBounds(self):
      self.squidRect = self.squid.image.get_rect(topleft= (self.squid.x, self.squid.y))



  
    def checkCollisions(self):
      ## Player
      if self.squid.x < 0:
          self.squid.move_right()
      if self.squid.x + self.squid.length > self.w:
          self.squid.move_left()
      if self.squid.y < 0:
          self.squid.move_down()
      if self.squid.y + self.squid.length > self.h:
          self.squid.move_up()
      ##
      
      ## Enemies
      for i in range(self.enemyCount):
        enemyRect = self.enemy.image[i].get_rect(topleft= (self.enemy.x[i], self.enemy.y[i]))
        if enemyRect.colliderect(self.squidRect):
          self.gameState = 'gameover'
        elif self.enemy.x[i] < 0 or self.enemy.x[i] + self.enemy.size[i] > self.w:
          self.enemy.xChange[i] = self.enemy.xChange[i] * -1
        elif self.enemy.y[i] < 0 or self.enemy.y[i] + self.enemy.size[i] > self.h:
          self.enemy.yChange[i] = self.enemy.yChange[i] * -1
      ##
          
    def enemyMove(self):
      for i in range(self.enemyCount):
        if self.enemy.x[i] <= 0:
          self.enemy.move(i)

      
    def updateScreen(self):
      self.surface.blit(self.background, (0,0))
      self.squid.drawPlayer()
      
      for i in range(self.enemyCount):
        self.enemy.drawEnemy(i)
      self.surface.blit(self.scoretext.textSurface, (0,0))
      
      if self.gameState == 'gameover':
        # Game Over Text
        self.gameOverText = Text("Game Over! Score: {0}".format(self.score), 'white', 30, self.surface, self.w/2, self.h/2)
        self.gameOverTextCenter = self.gameOverText.textSurface.get_rect(center=(self.w/2, self.h/2))
        self.surface.blit(self.gameOverText.textSurface, (self.w/2 - self.gameOverTextCenter.width/2, self.h/2 - self.gameOverTextCenter.height/2))

        # Restart Text
        self.spaceRestartText = Text("Press [SPACE] to Restart or [ESC] to Quit".format(self.score), 'white', 20, self.surface, self.w/2, self.h/2)
        self.spaceRestartTextCenter = self.spaceRestartText.textSurface.get_rect(center=(self.w/2, self.h/2))
        self.surface.blit(self.spaceRestartText.textSurface, (self.w/2 - self.spaceRestartTextCenter.width/2, self.h/2 + self.gameOverTextCenter.height/2))
      pygame.display.flip()


  
    def gameOverFunction(self):
      self.gameOverText = Text("Game Over! Score: {0}".format(self.score), 'white', 30, self.surface, self.w/2, self.h/2)
      
      pygame.display.flip()


  
    def run(self):
      self.running = True
      #
      while self.running:
        time.sleep(self.cap)  
        ## Play 
        if self.gameState == 'play':
          self.setBounds()
          ### PLAYER
          self.squid.walk()
          for event in pygame.event.get():
            if event.type == KEYDOWN:
              if event.key == K_ESCAPE:
                  quit()

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
          ###
              
          ### ENEMIES
          for i in range(self.enemyCount):
            self.enemy.move(i)
          if self.score % 100 == 0:
            self.enemyCount += 1
            self.enemy.spawnEnemy(self.enemylength, 4, 0, 0)
          ###

          ### SCORE
          self.frame = self.frame + 1
          self.score += 1
          self.scoretext = Text("Score: {0}".format(self.score), 'white', 30, self.surface, 0, 0)
          self.checkCollisions()
          ###
        ##
          
        ## Game Over
        elif self.gameState == 'gameover':
          self.gameOverFunction()
          for event in pygame.event.get():
            if event.type == KEYDOWN:
              if event.key == K_ESCAPE:
                quit()
              if event.key == K_SPACE:
                self.reset()
        ##

        self.updateScreen()
      #
