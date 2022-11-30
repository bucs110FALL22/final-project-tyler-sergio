import math
#import os
import pygame

pygame.init()
SPEED_SCALE = 0.5
WIDTH = 400
HEIGHT = 400
XBOUND = 300
YBOUND = 300

window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill('gray')


class Sprite(pygame.sprite.Sprite):

    def __init__(self, spritefigure, width, height, x, y, speed=1):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(spritefigure),
                                            (width, height))
        #self.image = pygame.Surface((width,height))
        #self.image.fill("blue")
        # self.x = x
        # self.y = y
        self.speed = speed
        self.direction = (1, 0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # def move(self):
    #   self.forward(self.speed)
    #   if self.xcor() > 190:
    #     self.setx(190)
    #     self.right(60)

    #   if self.xcor() < -190:
    #     self.setx(-190)
    #     self.right(60)

    #   if self.ycor() > 190:
    #     self.sety(190)
    #     self.right(60)

    #   if self.ycor() < -190:
    #     self.sety(-190)
    #     self.right(60)


class Player(Sprite):

    def __init__(self, spritefigure, width, height):
        Sprite.__init__(self, spritefigure, width, height, WIDTH // 2,
                        HEIGHT // 2)
        self.lives = 3
        self.speed = 2

    def turn(self, degrees):
        rad = degrees * math.pi / 180
        x = self.direction[0]
        y = self.direction[1]
        self.direction = (x * math.cos(rad) - y * math.sin(rad),
                          x * math.sin(rad) + y * math.cos(rad))
        print(self.direction)

    def turn_left(self):
        self.turn(-15)

    def turn_right(self):
        self.turn(15)

    def accelerate(self):
        self.speed += 1

    def brake(self):
        self.speed -= 1

    def move(self):
        self.rect.x += int(self.direction[0] * self.speed * SPEED_SCALE)
        self.rect.y += int(self.direction[1] * self.speed * SPEED_SCALE)
        self.bounds()

    def bounds(self):
        xmax = XBOUND
        xmin = WIDTH - XBOUND
        ymax = YBOUND
        ymin = WIDTH - YBOUND
        if self.rect.x < xmin:
            self.rect.x = xmin
        elif self.rect.x > xmax:
            self.rect.x = xmax
        if self.rect.y < ymin:
            self.rect.y = ymin
        elif self.rect.y > ymax:
            self.rect.y = ymax

    def pos(self):
        return self.rect.topleft

    # def cyloop(self):
    #   self.pendown()

    # def non_attack(self):
    #   self.penup()
    #   self.clear()


class Game():

    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.character = Player('images/triangle CS.png', 20, 20)
        self.lives = 3

    def play(self):
        while self.state == 'playing':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.state = 'quit'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.character.turn_left()
                    if event.key == pygame.K_RIGHT:
                        self.character.turn_right()
                    if event.key == pygame.K_UP:
                        self.character.accelerate()
                    if event.key == pygame.K_DOWN:
                        self.character.brake()
            self.character.move()
            window.fill('black')
            #window.blit(border)
            window.blit(self.character.image, self.character.pos())
            #print(self.character.rect.topleft)
            pygame.display.update()
            pygame.time.wait(10000000)

    # def borders(self):
    #   self.character.speed(0)
    #   self.character.color("white")
    #   self.character.pensize(3)
    #   self.character.penup()
    #   self.character.goto(-200, 200)
    #   self.character.pendown()
    #   for side in range(4):
    #     self.character.forward(400)
    #     self.character.right(90)
    #   self.character.penup()
    #   self.character.ht()


game = Game()
game.play()
