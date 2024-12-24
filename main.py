
from game.game import Game
from scenes.new_game_scene import NewGameScene

import pygame


# Run the game
if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.set_scene(NewGameScene(game))
    game.run()
    pygame.quit()