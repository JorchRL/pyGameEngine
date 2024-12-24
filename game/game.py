
from engine.engine import Engine
from scenes.new_game_scene import NewGameScene


class Game:
    """Main game class, which manages the window and scene transitions."""

    def __init__(self, width, height, title):
        self.engine = Engine(width, height, title, 30)
        self.width = width
        self.height = height
        self.title = title
        self.scenes = {}

    def set_scene(self, identifier):
        """
        Set the current scene by its identifier. Use this to implement
        the scene transition logic from one scene to another. A scene
        should call its parent game.set_scene() method to trigger a transition.
        :param identifier:
        :return:
        """
        if identifier in self.scenes:
            self.engine.set_scene(self.scenes[identifier])
            return
        raise ValueError(f"Scene '{identifier}' does not exist!")

    def add_scene(self, identifier, scene):
        """
        Add a scene to the game
        :param identifier: The key to identify the scene -- a string
        :param scene: The scene object (an instance of a class derived from Scene)
        :return:
        """
        self.scenes[identifier] = scene

    def run(self):
            """
            Starts the execution of the game, which updates
            and renders the current scene continuously until the game ends.
            :return: None
            """
            self.engine.run()