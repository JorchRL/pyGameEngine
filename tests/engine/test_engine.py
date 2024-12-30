import unittest
from unittest.mock import patch, Mock
from engine.engine import Engine
from engine.events import EventDispatcher
from engine.scenefsm import SceneFSM
from engine.data_loader import DataLoader

class TestEngine(unittest.TestCase):

    @patch('pygame.display.set_mode')
    @patch('pygame.display.set_caption')
    @patch('pygame.time.Clock')
    @patch('pygame.init')
    def setUp(self, mock_pygame_init, mock_pygame_clock, mock_pygame_set_caption, mock_pygame_set_mode):
        self.mock_pygame_init = mock_pygame_init
        self.mock_pygame_clock = mock_pygame_clock
        self.mock_pygame_set_caption = mock_pygame_set_caption
        self.mock_pygame_set_mode = mock_pygame_set_mode

        self.mock_event_dispatcher = Mock(spec=EventDispatcher)
        self.mock_fsm = Mock(spec=SceneFSM)
        self.mock_data_loader = Mock(spec=DataLoader)
        self.mock_data_loader.load_units.return_value = {}
        self.mock_data_loader.load_resources.return_value = {}

        with patch('engine.engine.EventDispatcher', return_value=self.mock_event_dispatcher), \
             patch('engine.engine.SceneFSM', return_value=self.mock_fsm), \
             patch('engine.engine.DataLoader', return_value=self.mock_data_loader):
            self.engine = Engine(800, 600, 'Test Game', 30)

    def test_engine_initialization(self):
        self.mock_pygame_init.assert_called_once()
        self.mock_pygame_set_mode.assert_called_once_with((800, 600))
        self.mock_pygame_set_caption.assert_called_once_with('Test Game')
        self.assertEqual(self.engine.width, 800)
        self.assertEqual(self.engine.height, 600)
        self.assertTrue(self.engine.running)
        self.assertEqual(self.engine.tick_rate, 30)
        self.assertIsInstance(self.engine.event_dispatcher, EventDispatcher)
        self.assertIsInstance(self.engine.fsm, SceneFSM)
        self.assertIsInstance(self.engine.data_loader, DataLoader)
        self.assertEqual(self.engine.units_data, {})
        self.assertEqual(self.engine.resources_data, {})

    @patch('pygame.event.get')
    def test_run_game_loop(self, mock_pygame_event_get):
        mock_pygame_event_get.return_value = [Mock(type=pygame.QUIT)]
        self.engine.running = True
        self.engine.run()
        self.assertFalse(self.engine.running)

    def test_set_scene(self):
        mock_scene = Mock()
        self.engine.set_scene(mock_scene)
        self.mock_fsm.set_scene.assert_called_once_with(mock_scene)

if __name__ == '__main__':
    unittest.main()
