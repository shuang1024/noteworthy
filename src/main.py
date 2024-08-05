import pygame

from constants import *
from classes import *


def main():
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Noteworthy")



    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        display.fill(BACKGROUND)


main()
