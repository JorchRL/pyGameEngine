import pygame

from engine.events import EventDispatcher
from engine.scenefsm import SceneFSM
from engine.data_loader import DataLoader

class Engine:
    """
    The main game engine that drives the game loop.
    - Coordinates FSM, scenes, and the event system.
    - Maintains the gameloop execution: input-handling
    """

    def __init__(self, width, height, title, tick_rate):
        pygame.init()
        # global game state
        self.width = 800
        self.height = 600
        self.running = True

       # Pygame components
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.tick_rate = tick_rate

        self.event_dispatcher = EventDispatcher()
        self.fsm = SceneFSM(self.event_dispatcher)

        self.data_loader = DataLoader('units.json', 'resources.json')
        self.units_data = self.data_loader.load_units()
        self.resources_data = self.data_loader.load_resources()

    def set_scene(self, scene):
        """
        Set the initial FSM state (e.g., NewGameScene, or the main menu)
        :param scene:
        :return:
        """
        self.fsm.set_scene(scene)

    def run(self):
        """
        Main game loop:
        - Process input events
        - Update the current FSM state
        - Render the current scene
        :return:
        """
        while (self.running) :
            # handle events
            events = pygame.event.get()
            # The engine checks when to quit. Maybe should offer a callback instead?
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            # Forward HANDLE_EVENTS request to FSM to call the
            # handle_events method of the current running scene
            self.fsm.handle_events(events)
            # Forward UPDATE request to FSM to call the
            # Update method of the current running scene
            self.fsm.update()

            # Forward the RENDER request to FSM to call the
            # render method of the current running scene
            self.fsm.render(self.screen)
            # Note: the Engine manages the screen, but injects
            # it as a dependency for the scene

            # Then swap buffers
            pygame.display.flip()
            # And advance the clock
            self.clock.tick(self.tick_rate)

