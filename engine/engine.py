import pygame

from engine.events import EventDispatcher
from engine.fsm import FSM


class Engine:
    """
    The main game engine that drives the game loop.
    - Coordinates FSM, scenes, and the event system.
    - Maintains the gameloop execution: input-handling
    """

    def __init__(self):
        self.width = 800
        self.height = 600
        self.running = True
        self.event_dispatcher = EventDispatcher()
        self.fsm = FSM(self.event_dispatcher)

    def set_initial_state(self, state):
        """
        Set the initial FSM state (e.g., NewGameScene, or the main menu)
        :param state:
        :return:
        """
        self.fsm.set_state(state)

    def run(self):
        """
        Main game loop:
        - Process input events
        - Update the current FSM state
        - Render the current scene
        :return:
        """
        while (self.running) :
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            for event in events:
                self.fms.handle_event(event)
            self.fsm.update()
            pygame.display.flip()