import pygame

class Text:
  def __init__(self, text, color, size, surface, x, y):
    pygame.font.init()
    self.surface = surface
    self.my_font = pygame.font.SysFont('Comic Sans MS', size)
    self.textSurface = self.my_font.render(text, True, color)




  