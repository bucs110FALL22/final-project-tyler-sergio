import pygame

class Text:
  def __init__(self, text, color, size, surface, x, y):
    pygame.font.init()
    self.surface = surface
    my_font = pygame.font.SysFont('Comic Sans MS', size)
    self.textSurface = my_font.render(text, False, color)
    self.surface.blit(self.textSurface, (x,y))




  