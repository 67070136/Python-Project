"""กระดาน"""
import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE
from .piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()
    
    def draw_squares(self, win): #กำหนดขนาดช่องสี่เหลี่ยม
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):#I changed ROWS to COLS
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col] # Swapping the position of the piece and the destination
        Piece.move(piece, row, col)

        if row == ROWS or row == 0: #Check if the destination promotes the piece
            Piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])   #interior list for each row
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):#กำหนดตำแหน่งหมากแต่ละสี
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)   #empty space is 0

    def draw(self, win): #draw the board
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def get_valid_moves(self, piece):# กำหนด dictionary สำหรับเก็บตำแหน่งการเดินที่ถูกต้องทั้งหมดของตัวหมาก
        moves = {}
        (4, 5) = [(3, 4)]
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king: # ตรวจสอบว่าตัวหมากเป็นสีแดงหรือเป็นตัวคิง (ตัวคิงสามารถเดินได้ทั้งสองทิศทาง)
            pass
        if piece.color == WHITE or piece.king:# ตรวจสอบว่าตัวหมากเป็นสีขาวหรือเป็นตัวคิง
            pass
    
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):# กำหนด dictionary สำหรับเก็บตำแหน่งที่สามารถเดินได้ในทิศทางซ้าย
        move = {} # กำหนด dictionary สำหรับเก็บตำแหน่งที่สามารถเดินได้ในทิศทางซ้าย
        last = []# สร้าง list สำหรับเก็บหมากที่อาจจะถูกข้าม (หรือถูกกิน)
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board.get_piece(r, left)
            if current == 0:
                if skip_only and not last:
                    break
            left -= 1

    def __traverse_right(self, start, stop, step, color, left, skipped=[]):# ตำแหน่งนี้สำหรับเขียนโค้ดการหาทางเดินในทิศทางขวา
        pass
