import pygame
from pygame.locals import *
import time
import random

SIZE = 40


class Squid:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("picture/player_squid.png").convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.direction = 'down'

        self.length = length
        self.x = [40]*length
        self.y = [40]*length

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        #
        # 
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill((110, 110, 5))

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
      
        self.squid = Squid(self.surface, 5)
        self.squid.draw()

    def render_background(self):
        background = pygame.image.load("picture/space.jgp")
        self.surface.blit(background, (0,0))
      
    def play(self):
        self.render_background()
        #self.squid.walk()

    def run(self):
        running = True

        while running:
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

            self.squid.walk()
            

            time.sleep(.2)

if __name__ == '__main__':
    game = Game()
    game.run()