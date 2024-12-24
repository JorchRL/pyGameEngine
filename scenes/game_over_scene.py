import pygame

from game.constants import BLACK, RED, WHITE, WIDTH, HEIGHT
from engine.scene import Scene


class GameOverScene(Scene):
    """Scene for the game over screen."""

    def __init__(self, game):
        super().__init__(game)
        self.score = 10

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                pass
                # Return to NewGameScene on any key press
                self.game.set_scene("main_menu")

    def on_enter(self):
        print("Entering GameOverScene")

    def on_exit(self):
        print("Exiting GameOverScene")

    def draw(self, screen):
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        text = font.render("Game Over!", True, RED)
        score_text = font.render(f"Your Score: {self.score}", True, WHITE)
        prompt_text = font.render("Press any key to restart", True, WHITE)
        screen.blit(text, (WIDTH // 3, HEIGHT // 3))
        screen.blit(score_text, (WIDTH // 3, HEIGHT // 2))
        screen.blit(prompt_text, (WIDTH // 4, HEIGHT // 1.5))
