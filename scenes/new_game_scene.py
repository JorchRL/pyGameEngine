import pygame

from game.constants import BLACK, WHITE, WIDTH, HEIGHT
from scenes.gameplay_scene import GameplayScene
from scenes.base_scene import Scene


class NewGameScene(Scene):
    """Scene for the start screen."""

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
            if event.type == pygame.KEYDOWN:
                # Start the game when any key is pressed
                self.game.set_scene(GameplayScene(self.game))

    def draw(self, screen):
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        text = font.render("Press any key to start the game!", True, WHITE)
        screen.blit(text, (WIDTH // 6, HEIGHT // 2))
