import pygame
from vars import *
from chessgame import ChessGame

if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE, pygame.FULLSCREEN)
    chs = ChessGame(win, STARTINGPOSFEN)
    chs.run()
    pygame.quit()

