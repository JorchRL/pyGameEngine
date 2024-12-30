import unittest
from engine.engine import Engine
import pygame

class TestEngine(unittest.TestCase):

    def setUp(self):
        self.engine = Engine(800, 600, "Test Game", 30)

    def test_initialization(self):
        self.assertEqual(self.engine.width, 800)
        self.assertEqual(self.engine.height, 600)
        self.assertEqual(self.engine.tick_rate, 30)
        self.assertTrue(self.engine.running)
        self.assertIsInstance(self.engine.screen, pygame.Surface)
        self.assertIsInstance(self.engine.clock, pygame.time.Clock)
        self.assertIsInstance(self.engine.event_dispatcher, EventDispatcher)
        self.assertIsInstance(self.engine.fsm, SceneFSM)

    def test_set_scene(self):
        scene = unittest.mock.Mock()
        self.engine.set_scene(scene)
        self.assertEqual(self.engine.fsm.current_scene, scene)

    def test_run(self):
        self.engine.running = False
        self.engine.run()
        self.assertFalse(self.engine.running)

if __name__ == '__main__':
    unittest.main()
