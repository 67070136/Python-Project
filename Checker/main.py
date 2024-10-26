"""mainในการเชื่อมcodeเข้าหากัน"""
import pygame
from checkers .constants import WIDTH, HEIGHT
from checkers.board import Board

FPS = 60 #ปรับfpsสูงสุดได้

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #ขนาดgame window
pygame.display.set_caption('Checkers') #ชื่อเวลาเปิดwindow

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()

main()