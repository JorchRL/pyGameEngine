
from game.game import Game
from scenes.new_game_scene import NewGameScene
from scenes.gameplay_scene import GameplayScene
from scenes.game_over_scene import GameOverScene

import pygame


# Run the game
if __name__ == "__main__":
    game = Game(800, 600, "Snek Game")


    game.add_scene("main_menu" ,NewGameScene(game))
    game.add_scene("gameplay" ,GameplayScene(game))
    game.add_scene("game_over" ,GameOverScene(game))

    game.set_scene("main_menu")
    game.run()