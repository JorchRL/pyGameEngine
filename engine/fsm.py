class State:
    """
    Abstract Base Class for FSM States.
    A state should manage scene lifecycle and describe conditions for exiting the state.
    """

    def on_enter(self):
        """Called when this state is entered. Prepare resources or scene setup."""
        pass

    def on_exit(self):
        """Called when this state is exited. Clean up resources if necessary."""
        pass

    def update(self):
        """
        Update logic for the current game state.
        This method will run within the game loop.
        """
        pass

    def handle_events(self, events):
        """
        Handle external events, such as scene-exit rules.
        Responsible only for observing the event system.
        """
        pass


class FSM:
    """
    Manages the current game state and transitions between states.
    - Allows states to be managed dynamically.
    - Uses the EventDispatcher to listen to events and trigger state changes.
    """

    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher
        self.current_state = None

    def set_state(self, state):
        """
        Switch to a new state.
        Calls `on_exit()` on the previous state and `on_enter()` on the new state.
        """
        pass

    def update(self):
        """
        Calls the `update()` method of the current state.
        Handles the main FSM logic within the game engine loop.
        """
        pass

    def handle_event(self, event):
        """
        Passes an incoming event to the active state's `handle_events()` method.
        """
        pass