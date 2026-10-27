"""The moves of the current piece."""
from utils import state
from utils.helpers import collision, lock_piece


def move_down():
    piece = state.piece
    if not collision(piece["squares"], piece["x"], piece["y"] + 1):
        piece["y"] += 1
    else:
        lock_piece()


def move_left():
    piece = state.piece
    if not collision(piece["squares"], piece["x"] - 1, piece["y"]):
        piece["x"] -= 1


def move_right():
    piece = state.piece
    if not collision(piece["squares"], piece["x"] + 1, piece["y"]):
        piece["x"] += 1


def rotate():
    piece = state.piece
    new_squares = [(-y, x) for x, y in piece["squares"]]
    if not collision(new_squares, piece["x"], piece["y"]):
        piece["squares"] = new_squares


# =====================================================================
# BONUS: Rotate the other way!
# The "z" key already calls this function, but it does nothing yet.
# Look at rotate() above: it turns each square (x, y) into (-y, x).
# What should the new square be to turn the other way?
# Don't forget to check for a collision before changing the piece!
# =====================================================================
def rotate_back():
    pass
