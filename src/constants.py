import pygame


WIDTH, HEIGHT = 1920, 1080
FPS = 60

LINE_THICKNESS = 6
LINE_INTERVAL = 60
STAFF_Y = HEIGHT//2 - 2*LINE_INTERVAL

NOTE_SPEED = 4
NOTE_INTERVAL = 0.75
NOTES = ["E", "F", "G", "A", "B", "C", "D", "E", "F1"]
NOTE_KEYS = [pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_SEMICOLON, pygame.K_QUOTE]
NOTE_COLOR = (20, 20, 10)
BACKGROUND = (255, 245, 210)
