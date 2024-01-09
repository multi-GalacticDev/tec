import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')

# Create the grid
def draw_grid():
    for i in range(1, ROWS):
        pygame.draw.line(screen, WHITE, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, WHITE, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

draw_grid()

# Game variables
player = "X"
board = [["" for _ in range(COLS)] for _ in range(ROWS)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and player != "":
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == "":
                if player == "X":
                    pygame.draw.line(screen, GREEN, (clicked_col * SQUARE_SIZE, clicked_row * SQUARE_SIZE),
                                     ((clicked_col + 1) * SQUARE_SIZE, (clicked_row + 1) * SQUARE_SIZE), LINE_WIDTH)
                    pygame.draw.line(screen, GREEN, ((clicked_col + 1) * SQUARE_SIZE, clicked_row * SQUARE_SIZE),
                                     (clicked_col * SQUARE_SIZE, (clicked_row + 1) * SQUARE_SIZE), LINE_WIDTH)
                    board[clicked_row][clicked_col] = "X"
                    player = "O"
                else:
                    pygame.draw.circle(screen, BLUE, (clicked_col * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                     clicked_row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5, LINE_WIDTH)
                    board[clicked_row][clicked_col] = "O"
                    player = "X"
    
    pygame.display.update()
