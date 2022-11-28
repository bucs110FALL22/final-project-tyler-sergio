import turtle
import math
import os

window = turtle.Screen() 
window.bgcolor('gray20')
turtle.fd(0)
turtle.speed(0)
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)


class Sprite(turtle.Turtle):
  def __init__(self, spritefigure, color, x, y):
    turtle.Turtle.__init__(self, shape = spritefigure)
    self.penup()
    self.color(color)
    self.forward(0)
    self.goto(x, y)
    self.speed = 0


  def move(self):
    self.forward(self.speed)
    if self.xcor() > 190:
      self.setx(190)
      self.right(60)

    if self.xcor() < -190:
      self.setx(-190)
      self.right(60)

    if self.ycor() > 190:
      self.sety(190)
      self.right(60)

    if self.ycor() < -190:
      self.sety(-190)
      self.right(60)
 
class Player(Sprite):
  def __init__(self, spritefigure, color, x, y):
    Sprite.__init__(self, spritefigure, color, x, y)
    self.lives = 3 
    self.speed = 2

  def turn_left(self):
    self.left(45)

  def turn_right(self):
    self.right(45)


  def speed(self):
    self.speed += 1

  def brake(self):
    self.speed -= 1

  def cyloop(self):
    self.pendown()
    

  def non_attack(self):
    self.penup()
    self.clear()


class Game():
  def __init__(self):
    self.level = 1 
    self.score = 0
    self.state = "playing"
    self.character = turtle.Turtle()
    self.lives = 3 

  def borders(self):
    self.character.speed(0)
    self.character.color("white")
    self.character.pensize(3)
    self.character.penup()
    self.character.goto(-200, 200)
    self.character.pendown()
    for side in range(4):
      self.character.forward(400)
      self.character.right(90)
    self.character.penup()
    self.character.ht()
    
    
game = Game()
game.borders()


player = Player("triangle", "blue", 0, 0)


turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")


turtle.onkey(player.speed, "Up")
turtle.onkey(player.brake, "Down")
turtle.onkeypress(player.cyloop, "space")
turtle.onkeyrelease(player.non_attack, "space")
turtle.listen()
while True:
  player.move()

window.exitonclick()
