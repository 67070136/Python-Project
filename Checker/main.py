"""mainในการเชื่อมcodeเข้าหากัน"""
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.game import Game

pygame.init()

FPS = 60  # ปรับfpsสูงสุดได้

WHITE_WIN_IMG = pygame.image.load('assets/white_win.png')
WHITE_WIN_IMG = pygame.transform.scale(WHITE_WIN_IMG, (800, 800))
WHITE_WIN_rect = WHITE_WIN_IMG.get_rect(center=(WIDTH // 2, HEIGHT // 2))

RED_WIN_IMG = pygame.image.load('assets/red_win.png')
RED_WIN_IMG = pygame.transform.scale(RED_WIN_IMG, (800, 800))
RED_WIN_rect = RED_WIN_IMG.get_rect(center=(WIDTH // 2, HEIGHT // 2))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # ขนาดgame window
pygame.display.set_caption('Checkers')  # ชื่อเวลาเปิดwindow
icon = pygame.image.load('assets/logo.png')
pygame.display.set_icon(icon)

# Menu logo
Menu_logo_image = pygame.image.load('assets/logo.png')
Menu_logo_image = pygame.transform.scale(Menu_logo_image, (200, 200))
Menu_logo_rect = Menu_logo_image.get_rect(midtop=(WIDTH // 2, 80))

# Load the PNG start button image
start_button_image = pygame.image.load('assets/start_button.png')  # Replace with the actual image path
start_button_image = pygame.transform.scale(start_button_image, (150, 50))  # Resize the button
start_button_rect = start_button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Title font and text
title_font = pygame.font.Font('assets/upheavtt.ttf', 64)  # Font size for title
title_text = title_font.render("Checkers Game", True, (0, 0, 0))  # Black title text
title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))  # Position above the button

#SFX 
Red_win_sfx = pygame.mixer.Sound('assets/Red wins.mp3') 
White_win_sfx = pygame.mixer.Sound('assets/White wins.mp3')
click_sound = pygame.mixer.Sound("assets/Click.mp3")

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

        # Draw Logo
        WIN.blit(Menu_logo_image, Menu_logo_rect)

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

    if not start_screen():
        return

    run = True
    while run:
        clock.tick(FPS)

        winner = game.winner()
        if winner is not None:
            if winner == "WHITE":  # Check against string identifiers
                WIN.blit(WHITE_WIN_IMG, WHITE_WIN_rect)
                White_win_sfx.play()
            elif winner == "RED":  # Check against string identifiers
                WIN.blit(RED_WIN_IMG, RED_WIN_rect)
                Red_win_sfx.play()
            print(winner)
            
            pygame.display.update()

            # Wait for user input to close the game after showing the winner
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        waiting = False
            run = False  # Exit the main loop after user closes or presses a key

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()