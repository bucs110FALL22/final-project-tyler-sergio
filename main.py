import pygame
from player import Player
from player import Sprite
from player import Game
from enemy import Enemy
#import your controller

def main():
    pygame.init()
    game = Game()
    game.play()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
