import pygame

from game.constants import WIDTH, HEIGHT, BLACK, BLUE, BLOCK_SIZE, GREEN, WHITE
from game.fruit import Fruit
from game.snake import Snake
from engine.scene import Scene


class GameplayScene(Scene):
    """Scene for the gameplay."""

    def __init__(self, game):
        super().__init__(game)
        # Initialize game components
        self.snake = Snake([100, 50])
        self.fruit = Fruit(WIDTH, HEIGHT)
        self.score = 0

    def on_enter(self):
        self.snake = Snake([100, 50])
        self.fruit = Fruit(WIDTH, HEIGHT)
        self.score = 0
        print("Entering GameplayScene")

    def on_exit(self):
        print("Exiting GameplayScene")


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != "DOWN":
                    self.snake.direction = "UP"
                elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                    self.snake.direction = "DOWN"
                elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                    self.snake.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                    self.snake.direction = "RIGHT"

    def update(self):
        self.snake.move()

        # Check if the snake eats the fruit
        if self.snake.body[0] == self.fruit.position:
            self.fruit.respawn(WIDTH, HEIGHT)
            self.score += 1
            self.snake.grow()
        else:
            self.snake.body.pop()

        # Check collisions
        self.snake.check_collision(WIDTH, HEIGHT)

        # If snake is dead, switch to GameOverScene
        if not self.snake.alive:
            # The pass statement is used here as a placeholder.
            # It indicates that no action is taken when the snake is dead.
            # The game will switch to the GameOverScene.
            pass
            self.game.set_scene("game_over")

    def draw(self, screen):
        screen.fill(BLACK)

        # Draw the snake
        for block in self.snake.body:
            pygame.draw.rect(
                screen, BLUE,
                pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE)
            )

        # Draw the fruit
        pygame.draw.rect(
            screen, GREEN,
            pygame.Rect(self.fruit.position[0], self.fruit.position[1], BLOCK_SIZE, BLOCK_SIZE)
        )

        # Draw the score
        font = pygame.font.SysFont(None, 25)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
