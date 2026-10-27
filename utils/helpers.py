"""Behind-the-scenes functions: no need to understand all of it!"""
import random

import config
from pieces import PIECES
from utils import state


def new_piece():
    """Spawns a random piece at the top of the game."""
    chosen = random.choice(PIECES)
    state.piece = {"squares": chosen.SQUARES, "color": chosen.COLOR, "x": config.WIDTH // 2 - 1, "y": 0}
    if collision(state.piece["squares"], state.piece["x"], state.piece["y"]):
        state.game_over = True


def collision(squares, px, py):
    """Returns True if the piece goes outside the game or touches a filled square."""
    for sx, sy in squares:
        x = px + sx
        y = py + sy
        if x < 0 or x >= config.WIDTH or y >= config.HEIGHT:
            return True
        if y >= 0 and state.grid[y][x] is not None:
            return True
    return False


def clear_lines():
    """Removes the complete lines and adds points."""
    kept_lines = [line for line in state.grid if None in line]
    nb = config.HEIGHT - len(kept_lines)
    state.grid = [[None] * config.WIDTH for _ in range(nb)] + kept_lines

    # =================================================================
    # EXERCISE 3: The score!
    # The variable `nb` contains the number of lines we just removed.
    # Give the player points by changing the variable `state.score`.
    # Example syntax:   state.score = state.score + 10
    # Bonus 1: the more lines removed at once, the more points you get.
    # Bonus 2: make the game speed up by decreasing `state.delay`.
    # =================================================================


def lock_piece():
    """The piece touched the bottom: it becomes part of the grid."""
    piece = state.piece
    for sx, sy in piece["squares"]:
        y = piece["y"] + sy
        if y >= 0:
            state.grid[y][piece["x"] + sx] = piece["color"]
    clear_lines()
    new_piece()
