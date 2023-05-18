import pygame
import logic
from logic import Color, Square
from vars import *
from typing import Tuple


P_W = 15
P_H = 10



def get_pos():
    W, H = pygame.display.get_surface().get_size()
    m = min(W - 2 * P_W, H - 2 * P_H)
    x = (W - m) // 2
    y = (H - m) // 2
    return x, y, m, m


def coord_from_pos(coord_x, coord_y) -> Tuple[int, int]:
    """
    Fait le lien entre les pixels et les coordonnées de la matrice
    :return: Retourne i,j les coordonnées de la matrice de Board
    """
    x, y, w, h = get_pos()
    i = (coord_y - y) // (h // 8)
    j = (coord_x - x) // (w // 8)
    return i, j


class Board:
    def __init__(self, size):
        self.size = size

        self.board_to_output = [[None for _ in range(8)] for _ in range(8)]

        self.dragged_piece = None
        self.dragged_piece_coord = None  # i,j
        self.dragging = False
        self.flipped = False

    def set_to_gone(self, i, j):
        self.dragged_piece = self.get_piece_at(i, j)
        if not self.dragged_piece:
            return
        self.dragging = True
        self.board_to_output[i][j] = "gone"
        self.clicked_piece_coord = i, j

    def f(self, i, j):
        if self.flipped:
            return i, 7 - j
        else:
            return 7 - i, j

    def set_to_not_gone(self):
        i, j = self.clicked_piece_coord
        self.board_to_output[i][j] = self.dragged_piece
        self.dragged_piece = None
        self.dragged_piece_coord = None
        self.dragged_piece_pos = None
        self.dragging = False

    def get_piece_at(self, i, j):
        return self.board_to_output[i][j]

    def is_empty(self, i, j):
        return (self.get_piece_at(i, j)) is None

    def update(self, logic: logic):
        for i in range(8):
            for j in range(8):
                self.set_piece(i, j, logic.get_piece(Square(i, j)))

    def set_piece(self, i, j, piece):
        self.board_to_output[i][j] = piece

    def clicked(self, pos) -> bool:
        """Called when the mouse is clicked return True if there is a piece at the position"""
        i, j = self.f(*coord_from_pos(*pos))
        if not isInbounds(i, j):
            return False
        if not self.is_empty(i, j):
            self.dragged_piece_pos = pos
            self.set_to_gone(i, j)
            return True
        return False

    def drag(self, pos) -> None:
        """Called only when a piece is already being dragged"""
        self.dragged_piece_pos = pos

    def drop(self, pos) -> Tuple[int, int]:
        """Called when a piece is already being dragged and the mouse is released"""
        i, j = self.f(*coord_from_pos(*pos))
        self.set_to_not_gone()
        return i, j

    def flip_board(self):
        self.flipped = not self.flipped

    # affichage

    def draw(self, win, dots, x, y, w, h):
        """Draws everything"""
        self.draw_board(win, x, y, w, h)
        self.draw_pieces(win, x, y, w, h)
        self.draw_dots(win, dots, x, y, w, h)

    def draw_board(self, win, x, y, w, h):
        case_size = w // 8
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = CASECOLOR1
                else:
                    color = CASECOLOR2
                pygame.draw.rect(win, color, (x + j * case_size, y + i * case_size, case_size, case_size))

    def draw_pieces(self, win, x, y, w, h):
        case_size = w // 8
        board = self.board_to_output
        for i in range(8):
            itab = 7 - i if not self.flipped else i
            for j in range(8):
                jtab = j if not self.flipped else 7 - j
                piece = self.get_piece_at(itab, jtab)
                if piece == "gone":
                    abreviation = self.dragged_piece.abreviation
                    if self.dragged_piece.color == Color.WHITE:
                        abreviation = abreviation.upper()
                    image_p = globals()[f"{self.dragged_piece.abreviation}_image"]
                    image_p = pygame.transform.smoothscale(image_p, (int(case_size * 1.1), int(case_size * 1.1)))
                    win.blit(image_p,
                             (self.dragged_piece_pos[0] - case_size // 2,
                              self.dragged_piece_pos[1] - case_size // 2))
                elif piece is not None:
                    color = piece.color
                    type = piece.__class__.__name__
                    abreviation = dico[type]
                    if color == Color.WHITE:
                        abreviation = abreviation.upper()
                    image_p = globals()[f"{abreviation}_image"]
                    image_p = pygame.transform.smoothscale(image_p, (case_size, case_size))
                    win.blit(image_p, (x + j * case_size, y + i * case_size))

    def draw_dots(self, win, moves, x, y, w, h):
        case_size = w // 8
        for move in moves:
            i, j = move.destination.i, move.destination.j
            i, j = self.f(i, j)
            pygame.draw.circle(win, RED, (x + j * case_size + case_size // 2, y + i * case_size + case_size // 2), 5)


dico = {"Pawn": "p",
        "Rook": "r",
        "Knight": "n",
        "Bishop": "b",
        "Queen": "q",
        "King": "k"
        }
