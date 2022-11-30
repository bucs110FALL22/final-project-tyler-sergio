import turtle
import pygame
import random
import math
from player import Player

class Enemy():
  def __init__(self, sprite, color, target):
    self.turt = turtle.Turtle
    self.target = target
    self.turt.color(color)
    self.turt.shape('circle')
    self.turt.penup()
    self.turt.speed = 1
    self.hp = 1

  def facePlayer():
    tarX = self.target.xcor()
    tarY = self.target.ycor()
    dir = atan(





  
  def testFacePlayer():
    if self.turt.xcor() > target.xcor() and self.turt.ycor() > target.ycor():
      self.turt.setheading(135)
    if self.turt.xcor() > target.xcor() and self.turt.ycor() < target.ycor():
      self.turt.setheading(225)
    if self.turt.xcor() < target.xcor() and self.turt.ycor() > target.ycor():
      self.turt.setheading(45)
    if self.turt.xcor() < target.xcor() and self.turt.ycor() < target.ycor():
      self.turt.setheading(315)
    
    