import pygame
from .constants import RED, WHITE
from checkers.board import Board

class Game:#  อันนี้เอาไว้ใช้แทนตัวของ Board อีกที
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):#เอาไว้Update Display Board
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):# กำหนดตัวแปรเริ่มต้นของเกม เช่น หมากที่ถูกเลือก กระดาน ผู้เล่นที่ต้องเล่น และการเดินที่ถูกต้อง
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def reset(self): # รีเซ็ตสถานะของเกมโดยเรียกฟังก์ชัน _init() อีกครั้ง
        self._init()

    def select(self, row, col):# ใช้เลือกหมากที่ตำแหน่ง (row, col) หรือทำการเดิน
        if self.select:# ตรวจสอบว่ามีหมากที่ถูกเลือกอยู่หรือไม่
            result = self._move(row, col)
            if not result:# ถ้าไม่สามารถเดินได้ ยกเลิกการเลือกหมาก และเรียก select() ใหม่
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_move(piece)
                return True
        
        return False

    def _move(self, row, col):# ใช้สำหรับการเดินหมากไปยังตำแหน่ง (row, col)
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        
        return True
    
    def change_turn(self):# เปลี่ยนผู้เล่นระหว่าง RED กับ WHITE
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
