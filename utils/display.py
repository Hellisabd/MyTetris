"""The window and everything that draws the game on screen."""
import tkinter as tk

import config
from utils import state

window = tk.Tk()
window.title("My Tetris")
label = tk.Label(window, text="Score: 0", font=("Arial", 16))
label.pack()
canvas = tk.Canvas(window, width=config.WIDTH * config.CELL_SIZE,
                   height=config.HEIGHT * config.CELL_SIZE, bg=config.BACKGROUND_COLOR)
canvas.pack()


def draw_square(x, y, color):
    canvas.create_rectangle(x * config.CELL_SIZE, y * config.CELL_SIZE,
                            (x + 1) * config.CELL_SIZE, (y + 1) * config.CELL_SIZE,
                            fill=color, outline=config.BACKGROUND_COLOR)


def draw():
    """Redraws the whole game: the grid, the current piece, the score."""
    canvas.delete("all")
    for y in range(config.HEIGHT):
        for x in range(config.WIDTH):
            if state.grid[y][x] is not None:
                draw_square(x, y, state.grid[y][x])
    piece = state.piece
    for sx, sy in piece["squares"]:
        draw_square(piece["x"] + sx, piece["y"] + sy, piece["color"])
    label.config(text="Score: " + str(state.score))
    if state.game_over:
        canvas.create_text(config.WIDTH * config.CELL_SIZE // 2,
                           config.HEIGHT * config.CELL_SIZE // 2,
                           text="GAME OVER!", fill="red", font=("Arial", 32, "bold"))
