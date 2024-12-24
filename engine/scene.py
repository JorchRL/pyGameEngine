class Scene:
    """
    Base class for scenes. Each scene is independent and implements specific game logic.
    Scenes do *not* control state transitions directly.
    A scene should manage scene lifecycle and describe conditions for exiting the scene.
    """
    def __init__(self, game):
        self.game = game  # Reference to the main game instance

    def handle_events(self, events):
        """Handle events for the scene."""
        pass

    def update(self):
        """Update the scene logic (e.g., animations or game objects)."""
        pass

    def draw(self, screen):
        """Render all scene elements to the screen."""
        pass
    def exit_condition_met(self):
        """
        Emit an event to notify the FSM that the scene is ready to exit.
        For example, on game-over or start-game events.
        :return:
        """
    def on_enter(self):
        """Called when this state is entered. Prepare resources or scene setup."""
        pass

    def on_exit(self):
        """Called when this state is exited. Clean up resources if necessary."""
        pass
