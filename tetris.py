# Run this file to play!
# Exercise 1 is in config.py, exercise 2 is in the pieces folder,
# exercise 3 is in utils/helpers.py (clear_lines).
from moves import move_down, move_left, move_right, rotate, rotate_back
from utils import state
from utils.display import window, draw
from utils.helpers import new_piece


def game_loop():
    if not state.game_over:
        move_down()
        window.after(state.delay, game_loop)
    draw()


def on_key(event):
    if state.game_over:
        return
    if event.keysym == "Left":
        move_left()
    elif event.keysym == "Right":
        move_right()
    elif event.keysym == "Up":
        rotate()
    elif event.keysym == "z":
        rotate_back()
    elif event.keysym == "Down":
        move_down()
    draw()


window.bind("<Key>", on_key)

new_piece()
game_loop()
window.mainloop()
