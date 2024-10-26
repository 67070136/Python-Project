"""mainในการเชื่อมcodeเข้าหากัน"""
import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board

pygame.init()

FPS = 60  # Max FPS
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Game window size
pygame.display.set_caption('Checkers')  # Window title

# Load button image
button_image = pygame.image.load('start_button.png')  # นำเข้าpng
button_image = pygame.transform.scale(button_image, (400, 120))  # สเกลปุ่มstart
button_rect = button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))  #ศูนย์กลาง

def game_loop(board, clock):
    # Main game
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse clicks for gameplay
                pass

        # Draw the board and update the display
        board.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()

def main():
    clock = pygame.time.Clock()
    board = Board()
    game_started = False  # Track if the game has started

    while not game_started:
        WIN.fill((200, 200, 200))

        # Draw the button image
        WIN.blit(button_image, button_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    game_started = True  # Start the game when button is clicked

        pygame.display.update()

    # Start the game loop after button is clicked
    game_loop(board, clock)

main()
