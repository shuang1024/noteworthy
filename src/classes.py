import pygame


class Staff:
    def __init__ (self, top_left_x, top_left_y, line_length, line_interval, line_thickness, clef, note_col):
        self.x = top_left_x
        self.y = top_left_y
        self.length = line_length
        self.spacing = line_interval
        self.thickness = line_thickness
        self.clef = clef
        self.note_col = note_col
        self.bars = []

    def draw(self, display):
        for i in range(5):
            pygame.draw.line(display, self.note_col, (self.x, self.y + self.spacing*i), (self.x + self.length, self.y + self.spacing*i), self.thickness)
