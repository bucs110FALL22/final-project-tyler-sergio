import turtle
import pygame 


pygame.init()
#
#
window = turtle.Screen() 
window.bgcolor('purple')
character = turtle.Turtle() 
character.color('orange')
character.shape('turtle')
character.penup()

def draw_line():
  character.pendown()
#
#
def up_motion():
  character.forward(120)
#
def left_direction():
  character.left(60)
#
def right_direction():
  character.right(60)

#
turtle.listen()
turtle.onkey(up_motion, "Up")
turtle.onkey(left_direction, "Left")
turtle.onkey(right_direction, "Right")





turtle.done()
pygame.quit()
window.exitonclick()