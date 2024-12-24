from engine.scene import Scene

class SceneFSM:
    """
    Manages the current game state and transitions between states.
    - Allows states to be managed dynamically.
    - Uses the EventDispatcher to listen to events and trigger state changes.
    """

    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher
        self.current_scene = None

    def set_scene(self, scene):
        """
        Switch to a new state.
        Calls `on_exit()` on the previous state and `on_enter()` on the new state.
        """
        if self.current_scene:
            self.current_scene.on_exit()
        # verify that the incomming scene is valid
        if not isinstance(scene, Scene):
            raise Exception("Invalid scene type.")
        self.current_scene = scene
        self.current_scene.on_enter()

    def handle_events(self, events):
        """
        Passes an incoming event to the active state's `handle_events()` method.
        :param events:
        :return:
        """
        if self.current_scene:
            self.current_scene.handle_events(events)
        else:
            raise Exception("No scene set.")

    def update(self):
        """
        Calls the `update()` method of the current state.
        Handles the main FSM logic within the game engine loop.
        """
        if self.current_scene:
            self.current_scene.update()
        else:
            raise Exception("No scene set.")

    def render(self, screen):
        """
        Passes the screen surface to the active state's `draw()` method.'
        :param screen:
        :return:
        """
        if self.current_scene:
            self.current_scene.draw(screen)
        else:
            raise Exception("No scene set.")