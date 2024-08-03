import pygame
import sys
import os

# Configurações do jogo
BOARD_SIZE = 8
SQUARE_SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)  # Cor cinza para os quadrados escuros

# Inicializa o pygame
pygame.init()
SCREEN = pygame.display.set_mode((BOARD_SIZE * SQUARE_SIZE, BOARD_SIZE * SQUARE_SIZE))
pygame.display.set_caption("Jogo de Xadrez")

# Inicializa o tabuleiro
board = [
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
]

def load_images():
    global IMAGES
    IMAGES = {}
    piece_types = ['w', 'b']
    pieces = ['R', 'N', 'B', 'Q', 'K', 'p']
    for color in piece_types:
        for piece in pieces:
            file_path = f"images/{color}/{color}{piece}.png"
            if os.path.exists(file_path):
                image = pygame.image.load(file_path)
                image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
                IMAGES[f"{color}{piece}"] = image
            else:
                print(f"Image file {file_path} not found.")

def draw_board():
    colors = [WHITE, GRAY]
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            pygame.draw.rect(SCREEN, colors[(r + c) % 2], pygame.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            piece = board[r][c]
            if piece != "--":
                piece_image = IMAGES.get(piece)
                if piece_image:
                    SCREEN.blit(piece_image, (c * SQUARE_SIZE, r * SQUARE_SIZE))

def move_piece(start, end):
    start_row, start_col = start
    end_row, end_col = end
    piece = board[start_row][start_col]
    board[start_row][start_col] = "--"
    board[end_row][end_col] = piece

def main():
    load_images()
    clock = pygame.time.Clock()
    selected_piece = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                col, row = event.pos
                col //= SQUARE_SIZE
                row //= SQUARE_SIZE

                if selected_piece is None:
                    if board[row][col] != "--" and board[row][col].startswith("w"):
                        selected_piece = (row, col)
                else:
                    if (row, col) != selected_piece:
                        move_piece(selected_piece, (row, col))
                        selected_piece = None

        draw_board()
        draw_pieces()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
