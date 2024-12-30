from game.game import Game
from scenes.new_game_scene import NewGameScene
from scenes.gameplay_scene import GameplayScene
from scenes.game_over_scene import GameOverScene
from scenes.rts_gameplay_scene import RTSGameplayScene

import pygame


# Run the game
if __name__ == "__main__":
    game = Game(800, 600, "RTS Game")


    game.add_scene("main_menu" ,NewGameScene(game))
    game.add_scene("gameplay" ,GameplayScene(game))
    game.add_scene("game_over" ,GameOverScene(game))
    game.add_scene("rts_gameplay" ,RTSGameplayScene(game))

    game.set_scene("rts_gameplay")
    game.run()
