import pygame
import random
import game_state
from constants import *
from circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"orange",self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            game_state.CURRENT_SCORE += 100
            return
        random_angle = random.uniform(20,50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_x = self.position.x
        new_y = self.position.y
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(new_x, new_y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2 = Asteroid(new_x, new_y, new_radius)
        asteroid2.velocity = new_velocity2 * 1.2
