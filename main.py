import pygame
from pygame.locals import *
import sys
import time
from constants import*
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import game_state

def main():
    #read score
    game_state.Score()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)
    pygame.init()
    pygame.freetype.init()        
    display_score = pygame.freetype.SysFont('droidsansmononerdfont', 40)
    display_score2 = pygame.freetype.SysFont('droidsansmononerdfont', 20)
    display_game_over = pygame.freetype.SysFont('droidsansmononerdfont', 100)
    
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #
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
                game_state.EndScore()
                pygame.event.clear()
                while True:
                    screen.fill("#000000")
                    display_game_over.render_to(screen,(375,300), "GAME OVER", (0,255,0))
                    display_score.render_to(screen,(20,20), "Score: "+ str(game_state.CURRENT_SCORE), (0,255,0))
                    display_score2.render_to(screen,(20,80), "High Score: "+ str(game_state.HIGH_SCORE), (255,0,0))
                    pygame.display.flip()
                    event = pygame.event.wait()
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
        screen.fill("#000000")
        display_score.render_to(screen,(20,20), "Score: "+ str(game_state.CURRENT_SCORE), (0,255,0))
        display_score.render_to(screen,(20,80), "High Score: "+ str(game_state.HIGH_SCORE), (255,0,0))

        #player.draw(screen)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000




if __name__ == "__main__":
    main()
