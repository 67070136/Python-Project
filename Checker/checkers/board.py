"""กระดาน"""
import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_king = self.white_king = 0
    
    def draw_squares(self, win): #กำหนดขนาดช่องสี่เหลี่ยม
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        pass
