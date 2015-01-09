from vector import Vector2
from pygame.locals import *
from random import random, choice
import pygame
import math


class Ball:
    def __init__(self,position,velocity,radius,color):
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.mass = math.pi*(self.radius**2)
        self.color = color
        self.dampening = .999

    def set_velocity(self,new_velocity):
        self.velocity = new_velocity

    def set_position(self,new_position):
        self.position = new_position

    def get_velocity(self):
        return self.velocity

    def get_position(self):
        return self.position

    def update(self,seconds_passed):
        self.position += self.velocity*seconds_passed
        self.velocity *= self.dampening

    def render(self,screen):
        pygame.draw.circle(screen,self.color,(int(self.position.x),int(self.position.y)),self.radius)


class RandBall(Ball):
    def update(self, seconds_passed):
        if random() < .001:
            self.velocity = Vector2(choice([-175,175]),choice([-175,175]))
        self.position += self.velocity*seconds_passed
        self.velocity *= self.dampening
