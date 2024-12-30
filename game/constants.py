# Constants for the screen dimensions and other settings
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
SNAKE_SPEED = 15  # Frames per second

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game config
BLOCK_SIZE = 20
SNAKE_SPEED = 15

# RTS-specific constants
UNIT_TYPES = {
    'worker': {
        'health': 100,
        'attack': 10,
        'speed': 5
    },
    'soldier': {
        'health': 200,
        'attack': 20,
        'speed': 3
    }
}

RESOURCE_TYPES = {
    'wood': {
        'amount': 1000
    },
    'gold': {
        'amount': 500
    }
}

RTS_SETTINGS = {
    'max_units': 50,
    'resource_gather_rate': 10
}
