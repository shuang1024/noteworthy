import pygame

from constants import *


class Note:
    def __init__(self, x, staff_y, line_interval, line_thickness, note_color, note_type, pitch):
        self.color = note_color
        self.type = note_type
        self.pitch = pitch
        self.index = NOTES.index(self.pitch)
        self.height = line_interval - line_thickness
        self.width = self.height * 1.3
        self.x = x - self.width//2
        self.y = staff_y + line_interval//2*(8-self.index) - self.height//2
        self.thickness = line_thickness
        self.stem_length = line_interval * 3.5

    def draw(self, display):
        pygame.draw.ellipse(display, self.color, (self.x, self.y, self.width, self.height))
        if self.index < 4:
            pygame.draw.line(display, self.color, (self.x + self.width - self.thickness//2, self.y + self.height//2), (self.x + self.width - self.thickness//2, self.y+self.height//2 - self.stem_length), self.thickness)
        else:
            pygame.draw.line(display, self.color, (self.x + self.thickness//2, self.y + self.height//2), (self.x + self.thickness//2, self.y+self.height//2 + self.stem_length), self.thickness)


class Staff:
    def __init__ (self, top_left_x, top_left_y, line_length, line_interval, line_thickness, clef, note_col):
        self.x = top_left_x
        self.y = top_left_y
        self.length = line_length
        self.spacing = line_interval
        self.thickness = line_thickness
        self.clef = clef
        self.note_col = note_col
        self.notes = []

    def draw(self, display):
        for i in range(5):
            pygame.draw.line(display, self.note_col, (self.x, self.y + self.spacing*i), (self.x + self.length, self.y + self.spacing*i), self.thickness)
        for note in self.notes:
            note.draw(display)

    def update(self, speed):
        for note in self.notes:
            note.x -= speed
            if note.x < 860-note.width:
                self.notes.remove(note)

    def add_note(self, start_pos, pitch):
        self.notes.append(Note(start_pos, self.y, self.spacing, self.thickness, self.note_col, "", pitch))