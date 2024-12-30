import unittest
from unittest.mock import Mock
from engine.scenefsm import SceneFSM
from engine.scene import Scene
from engine.events import EventDispatcher

class TestSceneFSM(unittest.TestCase):

    def setUp(self):
        self.mock_event_dispatcher = Mock(spec=EventDispatcher)
        self.fsm = SceneFSM(self.mock_event_dispatcher)
        self.mock_scene = Mock(spec=Scene)

    def test_set_scene(self):
        self.fsm.set_scene(self.mock_scene)
        self.mock_scene.on_enter.assert_called_once()
        self.assertEqual(self.fsm.current_scene, self.mock_scene)

    def test_set_scene_invalid(self):
        with self.assertRaises(Exception) as context:
            self.fsm.set_scene("invalid_scene")
        self.assertTrue("Invalid scene type." in str(context.exception))

    def test_handle_events(self):
        self.fsm.set_scene(self.mock_scene)
        mock_events = [Mock()]
        self.fsm.handle_events(mock_events)
        self.mock_scene.handle_events.assert_called_once_with(mock_events)

    def test_handle_events_no_scene(self):
        with self.assertRaises(Exception) as context:
            self.fsm.handle_events([Mock()])
        self.assertTrue("No scene set." in str(context.exception))

    def test_update(self):
        self.fsm.set_scene(self.mock_scene)
        self.fsm.update()
        self.mock_scene.update.assert_called_once()

    def test_update_no_scene(self):
        with self.assertRaises(Exception) as context:
            self.fsm.update()
        self.assertTrue("No scene set." in str(context.exception))

    def test_render(self):
        self.fsm.set_scene(self.mock_scene)
        mock_screen = Mock()
        self.fsm.render(mock_screen)
        self.mock_scene.draw.assert_called_once_with(mock_screen)

    def test_render_no_scene(self):
        with self.assertRaises(Exception) as context:
            self.fsm.render(Mock())
        self.assertTrue("No scene set." in str(context.exception))

    def test_no_global_variables(self):
        global_vars = [var for var in globals() if not var.startswith('__')]
        self.assertEqual(global_vars, [])

if __name__ == '__main__':
    unittest.main()
