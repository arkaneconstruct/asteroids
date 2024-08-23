import pygame
from constants import*
from player import Player

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)
        screen.fill("#000000")
        player.draw(screen)
        
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

    




if __name__ == "__main__":
    main()
