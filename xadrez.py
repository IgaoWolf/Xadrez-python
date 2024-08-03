import pygame
import sys
import os

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Xadrez")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)  # Cor cinza para os quadrados escuros
RED = (255, 0, 0)  # Cor para o contorno

# Carrega as imagens das peças
IMAGES = {}
pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']

def load_images():
    for piece in pieces:
        if piece.startswith('w'):
            image = pygame.image.load(f"images/white/{piece}.png")
        else:
            image = pygame.image.load(f"images/{piece}.png")
        
        # Redimensiona a imagem para 100x100 pixels
        IMAGES[piece] = pygame.transform.scale(image, (100, 100))

def draw_board(screen):
    colors = [WHITE, GRAY]
    for r in range(8):
        for c in range(8):
            color = colors[((r+c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*100, r*100, 100, 100))

def draw_pieces(screen, board):
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece != "--":
                piece_rect = pygame.Rect(c*100, r*100, 100, 100)
                if piece.startswith('w'):
                    # Adiciona o contorno preto se a peça for branca e estiver em um quadrado branco
                    pygame.draw.rect(screen, BLACK, piece_rect, 2)
                screen.blit(IMAGES[piece], piece_rect)

def main():
    clock = pygame.time.Clock()
    screen = SCREEN
    board = [
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    ]
    load_images()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_board(screen)
        draw_pieces(screen, board)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
