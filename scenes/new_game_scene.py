import pygame

from game.constants import BLACK, WHITE, WIDTH, HEIGHT
from engine.scene import Scene


class NewGameScene(Scene):
    """Scene for the start screen."""

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                # Start the game when any key is pressed
                self.game.set_scene("gameplay")

    def on_enter(self):
        print("Entering NewGameScene")

    def on_exit(self):
        print("Exiting NewGameScene")

    def draw(self, screen):
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        text = font.render("Press any key to start the game!", True, WHITE)
        screen.blit(text, (WIDTH // 6, HEIGHT // 2))
