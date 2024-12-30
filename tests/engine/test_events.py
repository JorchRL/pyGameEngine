import unittest
from unittest.mock import Mock
from engine.events import EventDispatcher, Event

class TestEventDispatcher(unittest.TestCase):

    def setUp(self):
        self.dispatcher = EventDispatcher()

    def test_subscribe(self):
        mock_callback = Mock()
        self.dispatcher.subscribe(Event, mock_callback)
        self.assertIn(Event, self.dispatcher.subscribers)
        self.assertIn(mock_callback, self.dispatcher.subscribers[Event])

    def test_unsubscribe(self):
        mock_callback = Mock()
        self.dispatcher.subscribe(Event, mock_callback)
        self.dispatcher.unsubscribe(Event, mock_callback)
        self.assertNotIn(mock_callback, self.dispatcher.subscribers[Event])

    def test_publish(self):
        mock_callback = Mock()
        self.dispatcher.subscribe(Event, mock_callback)
        event = Event()
        self.dispatcher.publish(event)
        mock_callback.assert_called_once_with(event)

    def test_no_global_variables(self):
        global_vars = [var for var in globals() if not var.startswith('__')]
        self.assertEqual(global_vars, [])

if __name__ == '__main__':
    unittest.main()
