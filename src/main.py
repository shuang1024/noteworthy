import pygame, random, time

from constants import *
from classes import *


def main():
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Noteworthy")

    staff = Staff(0, STAFF_Y, WIDTH, LINE_INTERVAL, LINE_THICKNESS, "treble", NOTE_COLOR)
    start = time.time()

    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key in NOTE_KEYS and 860 < staff.notes[0].x < 1060:
                    if NOTES[NOTE_KEYS.index(event.key)] == staff.notes[0].pitch:
                        staff.notes.pop(0)
        
        display.fill(BACKGROUND)
        if time.time() - start >= NOTE_INTERVAL:
            staff.add_note(WIDTH, random.choice(NOTES))
            start = time.time()
        staff.update(NOTE_SPEED)
        staff.draw(display)


main()
