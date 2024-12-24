import pygame

from scenes.new_game_scene import NewGameScene
from game.constants import WIDTH, HEIGHT, SNAKE_SPEED


class Game:
    """Main game class, which manages the window and scene transitions."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game with Scene Manager")
        self.clock = pygame.time.Clock()
        self.running = True
        # Set the initial scene
        self.current_scene = NewGameScene(self)

    def set_scene(self, scene):
        """Switch the current scene to a new one."""
        self.current_scene = scene

    def run(self):
        """Main game loop."""
        while self.running:
            events = pygame.event.get()
            self.current_scene.handle_events(events)
            self.current_scene.update()
            self.current_scene.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(SNAKE_SPEED)
