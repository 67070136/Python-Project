"""mainในการเชื่อมcodeเข้าหากัน"""
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.game import Game

# Initialize Pygame
pygame.init()

FPS = 60  # ปรับfpsสูงสุดได้

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # ขนาดgame window
pygame.display.set_caption('Checkers')  # ชื่อเวลาเปิดwindow

# Load the PNG start button image
start_button_image = pygame.image.load('assets/start_button.png')  # Replace with the actual image path
start_button_image = pygame.transform.scale(start_button_image, (150, 50))  # Resize the button
start_button_rect = start_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Title font and text
title_font = pygame.font.Font(None, 64)  # Font size for title
title_text = title_font.render("Checkers Game", True, (0, 0, 0))  # Black title text
title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))  # Position above the button

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def start_screen():
    """Displays the start screen with title and PNG start button."""
    while True:
        WIN.fill((200, 200, 200))  # Gray background

        # Draw title and button
        WIN.blit(title_text, title_rect)
        WIN.blit(start_button_image, start_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return True  # Start the game if the button is clicked

        pygame.display.update()

def main():
    clock = pygame.time.Clock()
    game = Game(WIN)

    # Show the start screen and wait for the user to click start
    if not start_screen():
        return  # Exit if the window is closed

    run = True
    while run:
        clock.tick(FPS)

        # Game loop
        if game.winner() is not None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()