"""The game state, shared by all the other files."""
import config

score = 0
delay = config.SPEED
grid = [[None] * config.WIDTH for _ in range(config.HEIGHT)]
piece = None
game_over = False
