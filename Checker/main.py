"""mainในการเชื่อมcodeเข้าหากัน"""
import pygame
from checkers .constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game

FPS = 60 #ปรับfpsสูงสุดได้

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #ขนาดgame window
pygame.display.set_caption('Checkers') #ชื่อเวลาเปิดwindow

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
    
        game.update()

    pygame.quit()

main()