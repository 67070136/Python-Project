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
        piece.move( row, col)

        if row == ROWS - 1 or row == 0: #Check if the destination promotes the piece
            piece.make_king()
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

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if pieces != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        
        return None
    
    def get_valid_moves(self, piece):# กำหนด dictionary สำหรับเก็บตำแหน่งการเดินที่ถูกต้องทั้งหมดของตัวหมาก
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == RED or piece.king: # ตรวจสอบว่าตัวหมากเป็นสีแดงหรือเป็นตัวคิง (ตัวคิงสามารถเดินได้ทั้งสองทิศทาง)
            moves.update(self._traverse_left(row -1, max(row-3,-1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3,-1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:# ตรวจสอบว่าตัวหมากเป็นสีขาวหรือเป็นตัวคิง
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
    
        return moves
    
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):# กำหนด dictionary สำหรับเก็บตำแหน่งที่สามารถเดินได้ในทิศทางซ้าย
        moves = {} # กำหนด dictionary สำหรับเก็บตำแหน่งที่สามารถเดินได้ในทิศทางซ้าย
        last = []# สร้าง list สำหรับเก็บหมากที่อาจจะถูกข้าม (หรือถูกกิน)
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r , left)] = last + skipped
                else:
                    moves[( r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3 , 0)
                    else:
                        row = min(r+3 , ROWS)

                    moves.update(self._traverse_left(r+step , row, step, color, left-1, skipped = last))
                    moves.update(self._traverse_right(r+step , row, step, color, left+1, skipped = last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves
    
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):# ตำแหน่งนี้สำหรับเขียนโค้ดการหาทางเดินในทิศทางขวา
        moves = {} # กำหนด dictionary สำหรับเก็บตำแหน่งที่สามารถเดินได้ในทิศทางขวา
        last = []# สร้าง list สำหรับเก็บหมากที่อาจจะถูกข้าม (หรือถูกกิน)
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r , right)] = last + skipped
                else:
                    moves[( r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3 , 0)
                    else:
                        row = min(r+3 , ROWS)

                    moves.update(self._traverse_left(r+step , row, step, color, right-1, skipped = last))
                    moves.update(self._traverse_right(r+step , row, step, color, right+1, skipped = last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
