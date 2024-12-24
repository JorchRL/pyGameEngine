import random

from game.constants import BLOCK_SIZE


class Fruit:
    def __init__(self, screen_width, screen_height):
        self.position = self.generate_position(screen_width, screen_height)

    def generate_position(self, screen_width, screen_height):
        x = random.randrange(1, (screen_width // BLOCK_SIZE)) * BLOCK_SIZE
        y = random.randrange(1, (screen_height // BLOCK_SIZE)) * BLOCK_SIZE
        return [x, y]

    def respawn(self, screen_width, screen_height):
        self.position = self.generate_position(screen_width, screen_height)
