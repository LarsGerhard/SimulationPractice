import sys

from pygame import display, event, sprite, image, quit
from pygame.locals import *
import pygame as pg
from numpy import cos, sin,pi

def main():
    # Initial Window Setup
    screen = display.set_mode([1280, 720])
    display.set_caption("Test Window")
    speed = [2, 2]
    black = (0, 0, 0)
    green = (0, 255, 60)
    white = (255,255,255)
    screen.fill(white)
    display.flip()
    running = True

    # Main Loop
    Car = car((pi / 2, 1))
    while True:
        Car.update()
        for event in pg.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()

# Car class
class car(sprite.Sprite):

    # Defines inherent attributes (sprite used, position, area)
    def __init__(self,vector):
        sprite.Sprite.__init__(self)
        self.image = image.load("./car.png").convert()
        self.rect = self.image.get_rect()
        screen = display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos
    def calcnewpos(self,rect,vector):
        (angle,v) = vector
        (dx,dy) = (v* cos(angle), v * sin(angle))
        return rect.move(dx,dy)

main()
