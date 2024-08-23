import pygame
import sys
from constants import*
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #player.update(dt)
        for object in updatable:
            object.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print(f"Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
        screen.fill("#000000")
        #player.draw(screen)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

    




if __name__ == "__main__":
    main()
