# =====================================================================
# EXERCISE 2: Add a new piece!
# Each piece is a file in this folder with:
#   SQUARES = a list of squares (x, y)
#   COLOR   = its color
# x goes to the right, y goes down, (0, 0) is the top-left square.
# Example: look at square.py, the yellow square is made of 4 small squares.
#
# 1. Copy one of the files (for example t_shape.py) and give it a new name.
# 2. Change SQUARES and COLOR in your new file.
# 3. Import it below and add it to the PIECES list.
# =====================================================================
from pieces import bar, square, t_shape, l_shape
# from pieces import my_piece   # <-- IMPORT YOUR PIECE HERE

PIECES = [
    bar,
    square,
    t_shape,
    l_shape,
    # my_piece,   # <-- ADD YOUR PIECE HERE (don't forget the comma!)
]
