import pygame
from vars import *
from chessgame import ChessGame
import sys


if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE, pygame.FULLSCREEN)
    mode="BOT"
    if sys.argv[1] == "BOT":
        mode="BOT"
    elif sys.argv[1] == "HUMAN":
        mode="HUMAN"
    chs = ChessGame(win, STARTINGPOSFEN,mode)
    chs.run()
    pygame.quit()

